#!/usr/bin/python

import argparse
import codecs
import os
from getpass import getpass

from pyaes256 import __version__
from pyaes256.decrypt import decrypt
from pyaes256.encrypt import encrypt


def validate_salt(value):
    if len(value) != 16:
        raise argparse.ArgumentTypeError("Salt must be a 16 characters long (hex)")
    return value


def get_version():
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, '__init__.py'), 'r') as fp:
        for line in fp.read().splitlines():
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")


def read_password(confirm=True):
    password = getpass()
    confirmed_password = getpass('Confirm Password:') if confirm else password
    if password != confirmed_password:
        raise Exception('Passwords do not match!')
    if len(password) < 1:
        raise Exception('Passwords is too short!')
    return password


def run():
    parser = argparse.ArgumentParser(
        description='Encrypt and decrypt text with AES-256 CBC and pbkdf2 as base64 like openssl')
    parser.add_argument('action', choices=['encrypt', 'decrypt'])
    parser.add_argument('input',
                        metavar='input',
                        type=str,
                        help='the text to encrypt/decrypt depending on the mode')

    parser.add_argument('-p', '--password',
                        metavar='password',
                        type=str,
                        help='the password')
    parser.add_argument('-o', '--output',
                        metavar='output',
                        type=str,
                        required=False,
                        help='target filename and path')
    parser.add_argument('-s', '--salt',
                        metavar='salt',
                        type=validate_salt,
                        required=False,
                        help='you can optionally specify a salt (in hex format) 16 characters')
    parser.add_argument('-sk', '--show-key',
                        help='shows the key and iv', action='store_const', const=True)
    parser.add_argument('--no-open',
                        help='do not automatically open the pdf', action='store_const', const=True)
    parser.add_argument('-t', '--title',
                        metavar='title',
                        type=str,
                        required=False,
                        help='optionally specify a title for the paper wallet')
    parser.add_argument('-n', '--notes',
                        metavar='notes',
                        type=str,
                        required=False,
                        help='optionally specify some notes that will be rendered in the notes section')
    parser.add_argument('--version', action='version', version=__version__)

    args = parser.parse_args()
    if 'encrypt' == args.action:
        if args.password is None:
            args.password = read_password()
        print('encrypting with aes256...')
        encrypted_text = encrypt(args.input, args.password.encode(), args.salt, show_key=args.show_key is not None)
        print(f"Encrypted: {encrypted_text}")
        from pyaes256.paper_wallet import generate_paper_wallet
        generate_paper_wallet(encrypted_text, output_file=args.output, open_pdf=args.no_open is None, title=args.title,
                              notes=args.notes)

    elif 'decrypt' == args.action:
        if args.password is None:
            args.password = read_password(confirm=False)
        decrypted_text = decrypt(args.input, args.password.encode(), show_key=args.show_key is not None)
        print(f"Decrypted: {decrypted_text}")


if __name__ == "__main__":
    run()
