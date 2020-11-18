from Crypto.Cipher import AES
import secrets
import base64

from pyaes256.common import SALT_LENGTH_BYTES, SALT_PREFIX, pbkdf2_derive_key_iv


def encrypt(text, password, salt=None, show_key=False):
    """
    Encrypts a text the same way as running openssl enc
    :param show_key: log derived key and iv if set to true
    :param text: your text you want to encrypt
    :param password: your password to encrypt with. We are using pkdfd2 to derive the aes key from the password
    :param salt:
    :return: base64 encoded encrypted text
    """
    if salt is None:
        salt = secrets.token_bytes(SALT_LENGTH_BYTES)
    else:
        salt = bytearray.fromhex(salt)

    aes_key, iv = pbkdf2_derive_key_iv(password, salt, show_key=show_key)
    print(f'\nsalt={salt.hex()}')
    cypher = AES.new(aes_key, AES.MODE_CBC, iv)
    padded = pad(text.encode())
    msg = cypher.encrypt(padded)
    base64_msg = base64.b64encode(SALT_PREFIX + salt + msg)
    return base64_msg.decode('utf-8')


def pad(byte_string):
    """
    Pad an input bytestring according to PKCS#7
    :param byte_string:
    :return: padded string
    """
    val = AES.block_size - (len(byte_string) % AES.block_size)
    return byte_string + bytearray([val] * val)
