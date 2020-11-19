import base64
from Crypto.Cipher import AES

from pyaes256.common import SALT_PREFIX, SALT_LENGTH_BYTES, pbkdf2_derive_key_iv


def decrypt(encrypted_base64_text, password, show_key=False):
    prefix_bytes = len(SALT_PREFIX) + SALT_LENGTH_BYTES
    decoded_base64_msg = base64.b64decode(encrypted_base64_text)
    salt = decoded_base64_msg[8:16]  # parse salt
    encrypted_text = decoded_base64_msg[prefix_bytes:]
    aes_key, iv = pbkdf2_derive_key_iv(password, salt, show_key=show_key)
    cypher = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_with_pad = cypher.decrypt(encrypted_text)
    decrypted = unpad(decrypted_with_pad).decode('utf-8')
    return decrypted


def unpad(byte_string):
    """
    Remove the PKCS#7 padding from a text bytestring.
    """
    val = byte_string[-1]
    if val > AES.block_size:
        raise ValueError('Input is not padded or padding is corrupt')
    return byte_string[:(len(byte_string) - val)]
