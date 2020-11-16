import base64
from Crypto.Cipher import AES
import hashlib

SALT_PREFIX = b'Salted__'
SALT_LENGTH_BYTES = 8


def unpad(byte_string):
    """
    Remove the PKCS#7 padding from a text bytestring.
    """
    val = byte_string[-1]
    if val > AES.block_size:
        raise ValueError('Input is not padded or padding is corrupt')
    return byte_string[:(len(byte_string) - val)]


def decrypt(encrypted_base64_text, password):
    prefix_bytes = len(SALT_PREFIX) + SALT_LENGTH_BYTES
    decoded_base64_msg = base64.b64decode(encrypted_base64_text)
    salt = decoded_base64_msg[8:16]  # parse salt
    encrypted_text = decoded_base64_msg[prefix_bytes:]
    aes_key = hashlib.pbkdf2_hmac('sha256', password, salt, 10000, 32)
    cypher = AES.new(aes_key, AES.MODE_ECB)
    decrypted_with_pad = cypher.decrypt(encrypted_text)
    decrypted = unpad(decrypted_with_pad).decode('utf-8')
    return decrypted
