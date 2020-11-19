from setuptools import setup, find_packages
from os import path
import codecs
import os.path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(name='pyaes256',
      version=get_version("pyaes256/__init__.py"),
      install_requires=['markdown', 'pillow', 'qrcode', 'weasyprint', 'cairocffi', 'pycryptodome'],
      author='Marko Nalis',
      author_email="marko@nalis.dev",
      url='https://github.com/The-Crocop/pyaes256',
      description="Encrypt text with AES256 and create a pdf with QR code that can be printed and stored",
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      package_data={
          'pyaes256': ['templates/*']
      },
      license='MIT',
      include_package_data=True,
      entry_points={
          'console_scripts': ['pyaes256=pyaes256.__main__:run']
      }
      )
