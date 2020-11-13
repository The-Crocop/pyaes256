#!/usr/bin/python

import argparse

from pyaes256.decrypt import decrypt
from pyaes256.encrypt import encrypt
from pyaes256.paper_wallet import generate_paper_wallet


def run():
    parser = argparse.ArgumentParser(description='Encrypt and decrypt text with AES-256 ECB and pbkdf2 as base64 like openssl')
    parser.add_argument('--input',
                           metavar='input',
                           type=str,
                           required=True,
                           help='the text to encrypt/decrypt depending on the mode')

    parser.add_argument('--password',
                           metavar='input',
                           type=str,
                           required=True,
                           help='the password')
    parser.add_argument('action', choices=['encrypt', 'decrypt'])

    args = parser.parse_args()
    if 'encrypt' == args.action:
        encryptedText = encrypt(args.input, args.password.encode())
        print(f"Encrypted: {encryptedText}")
        generate_paper_wallet(encryptedText)

    elif 'decrypt' == args.action:
        decryptedText = decrypt(args.input, args.password.encode())
        print(f"Decrypted: {decryptedText}")


if __name__ == "__main__":
    run()
