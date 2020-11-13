from setuptools import setup

setup(name='pyaes256',
      version='0.1',
      entry_points={
          'console_scripts': ['pyaes256=pyaes256.__main__:run']
      }
      )
