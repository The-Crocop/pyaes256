import platform
import subprocess
from datetime import datetime
import os

import qrcode
from string import Template
from weasyprint import HTML
import markdown as markdown


def open_file(filepath):
    if platform.system() == 'Darwin':       # macOS
        subprocess.Popen(['open', filepath], start_new_session=True)
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.Popen(['xdg-open', filepath], start_new_session=True)


def generate_paper_wallet(cyphertext, output_file='output/paperKey.pdf', open_pdf=False, title=None, notes=None):
    """
    generates a pdf containing a QR Code with the cyphertext, the cyphertext as text and explanations on how to decrypt
    :param open: open the file in the default program
    :param cyphertext:
    :param output_file: if True opens the file in your default pdf program
    :return:
    """
    now = datetime.now()  # generate timestamp for file generation and to show in generated pdf

    if output_file is None:
        output_file = f'paperKey_{now.strftime("%Y%m%d%H%M%S")}.pdf'

    #  NamedTempFile has issues in windows, as does using an absolute directory and referencing it in markdown.
    #  Therefore we handle creation and deletion of the file ourselves
    qr_tmp_filename = f"{os.urandom(24).hex()}.png"

    try:
        with open(qr_tmp_filename, 'wb') as fp:
            img = qrcode.make(cyphertext).resize((250, 250))
            img.save(fp)

            d = {
                'cyphertext': cyphertext,
                'aesMode': 'AES-256 CBC PBKDF2',
                'qrCodeFile': fp.name,
                'generationDateTime': now.strftime("%m/%d/%Y, %H:%M:%S"),
                'title': f"### {title} " if title else '',
                'notes': f"#### Notes\n{notes}" if notes else ''
            }
            with open(os.path.join(os.path.dirname(__file__), 'templates/printTemplate.md'), 'r') as templateFile:
                with open(os.path.join(os.path.dirname(__file__), 'templates/styles.css'), mode="r", encoding="utf-8") as css_file:

                    src = Template(templateFile.read())
                    result = src.substitute(d)
                    input_html = markdown.markdown(
                        result, extensions=["markdown.extensions.abbr",
                                            "markdown.extensions.attr_list",
                                            "markdown.extensions.def_list",
                                            "markdown.extensions.fenced_code",
                                            "markdown.extensions.footnotes",
                                            "markdown.extensions.tables",
                                            "markdown.extensions.md_in_html"]
                    )
                    css_input = css_file.read()

                    output_html = f"""
                        <html>
                            <head>
                                <style>{css_input}</style>
                            </head>
                            <body class="markdown-body">{input_html}</body>
                        </html>
                        """
                    html = HTML(string=output_html, base_url='output')

                    html.write_pdf(output_file)
                    print("--------------------")
                    print(f"encrypted paper generated in\n file://{os.path.abspath(output_file)}")
                    if open_pdf:
                        open_file(os.path.abspath(output_file))

    finally:
        os.remove(qr_tmp_filename)
