#!/usr/bin/python

import os
import argparse

import subprocess, sys

from decrypt import decrypt
from encrypt import encrypt
from paper_wallet import generate_paper_wallet

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description='Encrypt and decrypt text with AES-256 ECB and pbkdf2 as base64 like openssl')
    my_parser.add_argument('--input',
                           metavar='input',
                           type=str,
                           required=True,
                           help='the text to encrypt/decrypt depending on the mode')

    my_parser.add_argument('--password',
                           metavar='input',
                           type=str,
                           required=True,
                           help='the password')
    my_parser.add_argument('action', choices=['encrypt', 'decrypt'])

    args = my_parser.parse_args()
    if 'encrypt' == args.action:
        encryptedText = encrypt(args.input, args.password.encode())
        print(f"Encrypted: {encryptedText}")
        generate_paper_wallet(encryptedText)

    elif 'decrypt' == args.action:
        decryptedText = decrypt(args.input, args.password.encode())
        print(f"Decrypted: {decryptedText}")

