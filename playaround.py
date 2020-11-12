#!/usr/bin/python
import hashlib
import base64
from Crypto.Cipher import AES
import secrets
import argparse
import qrcode
from PIL import Image

SALT_PREFIX = b'Salted__'
SALT_LENGTH_BYTES = 8

def pad(bytestring):
    """
    Pad an input bytestring according to PKCS#7
    :param bytestring:
    :return: padded string
    """
    l = len(bytestring)
    val = AES.block_size - (l % AES.block_size)
    return bytestring + bytearray([val] * val)

def unpad(bytestring):
    """
    Remove the PKCS#7 padding from a text bytestring.
    """
    val = bytestring[-1]
    if val > AES.block_size:
        raise ValueError('Input is not padded or padding is corrupt')
    l = len(bytestring) - val
    return bytestring[:l]


def encrypt(text, password, salt=None):
    """
    Encrypts a text the same way as running openssl enc
    :param text: your text you want to encrypt
    :param password: your password to encrypt with. We are using pkdfd2 to derive the aes key from the password
    :param salt:
    :return: base64 encoded encrypted text
    """
    if salt is None:
        salt = secrets.token_bytes(SALT_LENGTH_BYTES)
    else:
        salt = bytearray.fromhex(salt)
    aesKey = hashlib.pbkdf2_hmac('sha256', password, salt, 10000, 32)
    print(f'key={aesKey.hex().upper()},\nlen={len(aesKey.hex())}\nsalt={salt.hex()}')
    cypher = AES.new(aesKey, AES.MODE_ECB)
    padded = pad(text.encode())
    msg = cypher.encrypt(padded)
    base64Msg = base64.b64encode(SALT_PREFIX + salt + msg)
    return base64Msg.decode('utf-8')

def decrypt(encryptedBase64Text, password):
    prefixBytes = len(SALT_PREFIX) + SALT_LENGTH_BYTES
    decodedBase64Msg = base64.b64decode(encryptedBase64Text)
    salt = decodedBase64Msg[8:16] # parse salt
    encryptedText = decodedBase64Msg[prefixBytes:]
    aesKey = hashlib.pbkdf2_hmac('sha256', password, salt, 10000, 32)
    cypher = AES.new(aesKey, AES.MODE_ECB)
    decryptedWithPad = cypher.decrypt(encryptedText)
    decrypted = unpad(decryptedWithPad).decode('utf-8')
    return decrypted


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
        img = qrcode.make(encryptedText)
        img.save('aes_qr.png')
        img.show()

    elif 'decrypt' == args.action:
        decryptedText = decrypt(args.input, args.password.encode())
        print(f"Decrypted: {decryptedText}")



    # DEMO_SALT = 'BC7A4EA3759E8988'
    # secret = 'young cement bubble network scout radio mask output maze alone balance seed party large couch forget paddle swarm person way yard switch open loop\n'
    # password = b'abcdefg'
    # encryptedText = encrypt(secret, password)
    # print(encryptedText)
    #
    # textToDecrypt = 'U2FsdGVkX191+tp3e4BHcqh0mnsQpXJeOyEmkRR4Rha7bQR3EYsiCZsUrWjHv3LEWXnP1rUheLIxf3cbBNQSzR1MRIv8CMfXVi81X9VjrsbsvGJuSPT8G9cmG3RHrcWBQUdaHsl8bsHUMNTqgp/AMtivDT1WHkLnNFKYvOj3Fn9rk8gUL3I7Wl1afbmHcXj939C9VpkRmvjZedsSWCeSLGq4Qnf8le4eBTNx0Ewa2SI='
    # decryptedText = decrypt(textToDecrypt, password)
    # print(decryptedText)
