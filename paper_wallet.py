import qrcode
from string import Template
from weasyprint import HTML
import markdown as markdown


def generate_paper_wallet(cyphertext, output_file='output/paperKey.pdf'):
    """
    generates a pdf containing a QR Code with the cyphertext, the cyphertext as text and explanations on how to decrypt
    :param cyphertext:
    :param output_file:
    :return:
    """
    img = qrcode.make(cyphertext).resize((250, 250))
    img.save('output/aes_qr.png')
    d = {
        'cyphertext': cyphertext,
        'aesMode': 'AES-256 ECB PBKDF2',
        'qrCodeFile': 'aes_qr.png'
    }
    with open('printTemplate.md', 'r') as templateFile:
        with open('styles.css', mode="r", encoding="utf-8") as css_file:
            src = Template(templateFile.read())
            result = src.substitute(d)
            input_html = markdown.markdown(
                result, extensions=["extra", "meta", "tables"]
            )
            css_input = css_file.read()

            output_html = f"""
                <html>
                    <head>
                        <style>{css_input}</style>
                    </head>
                    <body>{input_html}</body>
                </html>
                """
            html = HTML(string=output_html, base_url='output')

            html.write_pdf(output_file)
            # opener ="open" if sys.platform == "darwin" else "xdg-open"
            # subprocess.call([opener, paperKeyFile])

            # targetFile = open("output/paperKey.html", "w", encoding="utf-8", errors="xmlcharrefreplace")
            # targetFile.write(result)
