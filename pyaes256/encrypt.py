from Crypto.Cipher import AES
import secrets
import hashlib
import base64

SALT_PREFIX = b'Salted__'
SALT_LENGTH_BYTES = 8


def pad(byte_string):
    """
    Pad an input bytestring according to PKCS#7
    :param byte_string:
    :return: padded string
    """
    val = AES.block_size - (len(byte_string) % AES.block_size)
    return byte_string + bytearray([val] * val)


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
    aes_key = hashlib.pbkdf2_hmac('sha256', password, salt, 10000, 32)
    print(f'key={aes_key.hex().upper()}\nlen={len(aes_key.hex())}\nsalt={salt.hex()}')
    cypher = AES.new(aes_key, AES.MODE_ECB)
    padded = pad(text.encode())
    msg = cypher.encrypt(padded)
    base64_msg = base64.b64encode(SALT_PREFIX + salt + msg)
    return base64_msg.decode('utf-8')
