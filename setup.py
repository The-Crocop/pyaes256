from setuptools import setup, find_packages
import codecs
import os.path


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
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          'console_scripts': ['pyaes256=pyaes256.__main__:run']
      }
      )
