# PyAes256

This project aims to encrypt text with AES-256 and put it into a pdf similar to a paperwallet.
It is useful for example to encrypt seeds or passwords to a piece of paper and print it.
The output is base64 encoded and follows the same scheme that is generated by openssl.
Eg. the base64 string starts with "Salt__" followed by 8 bytes of salt. The Rest is the ciphertext.

## Getting Started
1. Install python >3.8
1. Install [pipenv](https://pypi.python.org/pypi/pipenv) by executing `pip install pipenv`.
1. Create a new virtual environment with all dependencies by executing `pipenv install`.
1. Important: PyAes256 uses [weasyprint](https://github.com/Kozea/WeasyPrint) to generate the pdf with the encrypted QR Code.
   In order to make it work on different Operating Systems it is required  to install certain libraries, that are needed for rendering..
   
   For Windows you have to install the GTK+ Libraries.
   You can download it here https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
   
   Pick the gtk3 runtime and install it. After that restart your terminal. Also select the PATH option
   
   More information at:
   [https://weasyprint.readthedocs.io/en/stable/install.html#step-4-install-the-gtk-libraries](https://weasyprint.readthedocs.io/en/stable/install.html#step-4-install-the-gtk-libraries)
   
## Activating the virtual environment
Before executing any of the commands below, you need to activate the virtual environment.
You can do so by executing `pipenv shell`.
Your command prompt should now indicate that you've activated the virtual environment.
It can be deactivated by executing `exit`.  

## Build single executable
run `pyinstaller pyaes256.spec`

the executable will be generated in dist folder.
Run it with in linux
`./dist/pyaes256  encrypt --input "hhhhh" --password "abcdefg"`

On Windows: 
`dist/pyaes256.exe  encrypt --input "hhhhh" --password "abcdefg"`

The paper wallet is generated into the output folder.

## Generating encrypted passwords 
to encode text with aes256-ecb. Pick any password.

## Additional Notes
To verify that this script outputs the same cyphertexts as other tools and it is reproducible you can verify the output with openssl

generate with openssl:
`echo -n 'mysupersecretseedphrase' | openssl enc  -aes-256-ecb -base64 -salt -pbkdf2 -out secretphrase-enc.txt`

Then type in your password.

to decode it run: 
`openssl enc -aes-256-ecb -d -base64 -salt -pbkdf2  -in secretphrase-enc.txt`

### Parameters used for AES-256 encryption

1. pbkdf2 with 10000 iterations: to derive the pass
1. pkcf#7 to pad the plaintext to the correct blocksize which must be multiple of 16
