from setuptools import setup

setup(name='pyaes256',
      version='0.1',
      install_requires=['markdown', 'pillow', 'qrcode', 'weasyprint'],
      py_modules=['pyaes256'],
      packages=['pyaes256'],
      entry_points={
          'console_scripts': ['pyaes256=pyaes256.__main__:run']
      }
      )
