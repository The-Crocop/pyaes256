#!/usr/bin/python

import argparse

from pyaes256.decrypt import decrypt
from pyaes256.encrypt import encrypt
from pyaes256.paper_wallet import generate_paper_wallet


def validate_salt(value):
    if len(value) != 16:
        raise argparse.ArgumentTypeError("Salt must be a 16 characters long (hex)")
    return value


def run():
    parser = argparse.ArgumentParser(
        description='Encrypt and decrypt text with AES-256 CBC and pbkdf2 as base64 like openssl')
    required_args = parser.add_argument_group('required named arguments')
    parser.add_argument('action', choices=['encrypt', 'decrypt'])
    required_args.add_argument('-i', '--input',
                               metavar='input',
                               type=str,
                               required=True,
                               help='the text to encrypt/decrypt depending on the mode')

    required_args.add_argument('-p', '--password',
                               metavar='password',
                               type=str,
                               required=True,
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

    args = parser.parse_args()
    if 'encrypt' == args.action:
        print('encrypting with aes256...')
        encrypted_text = encrypt(args.input, args.password.encode(), args.salt)
        print(f"Encrypted: {encrypted_text}")
        generate_paper_wallet(encrypted_text, output_file=args.output)

    elif 'decrypt' == args.action:
        decrypted_text = decrypt(args.input, args.password.encode())
        print(f"Decrypted: {decrypted_text}")


if __name__ == "__main__":
    run()
