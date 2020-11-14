from setuptools import setup, find_packages

setup(name='pyaes256',
      version='0.1',
      install_requires=['markdown', 'pillow', 'qrcode', 'weasyprint', 'cairocffi', 'pycryptodome'],
      author='Marko Nalis',
      author_email="author@email.com",
      url='https://github.com/The-Crocop/pyaes256',
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          'console_scripts': ['pyaes256=pyaes256.__main__:run']
      }
      )
