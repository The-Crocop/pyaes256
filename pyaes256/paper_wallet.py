import base64
import os
from io import BytesIO

import qrcode
from string import Template
from weasyprint import HTML
import markdown as markdown
import pathlib


def pil2datauri(img):
    """
    converts PIL image to datauri
    :param img: PIL image
    :return: data uri string
    """
    data = BytesIO()
    img.save(data, "png")
    data64 = base64.b64encode(data.getvalue())
    return u'data:img/png;base64,'+data64.decode('utf-8')


def generate_paper_wallet(cyphertext, output_file='output/paperKey.pdf'):
    """
    generates a pdf containing a QR Code with the cyphertext, the cyphertext as text and explanations on how to decrypt
    :param cyphertext:
    :param output_file:
    :return:
    """
    qr_output_path = pathlib.Path().absolute() / 'output'
    qr_output_path.mkdir(parents=True, exist_ok=True)

    img = qrcode.make(cyphertext).resize((250, 250))
    img_data_uri=pil2datauri(img)
    d = {
        'cyphertext': cyphertext,
        'aesMode': 'AES-256 ECB PBKDF2',
        'qrCodeFile': img_data_uri
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
            # opener ="open" if sys.platform == "darwin" else "xdg-open"
            # subprocess.call([opener, paperKeyFile])

            # targetFile = open("output/paperKey.html", "w", encoding="utf-8", errors="xmlcharrefreplace")
            # targetFile.write(result)
