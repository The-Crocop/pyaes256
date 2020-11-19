import hashlib

SALT_PREFIX = b'Salted__'
SALT_LENGTH_BYTES = 8


def pbkdf2_derive_key_iv(password, salt, show_key=False):
    """
    derives key and iv according to AES256-CBC
    :param show_key: log derived key and iv if set to true
    :param password:
    :param salt:
    :return: aes_key, iv
    """
    derived_key = hashlib.pbkdf2_hmac('sha256', password, salt, 10000, 48)
    aes_key = derived_key[0:32]
    iv = derived_key[32:48]
    if show_key:
        print(f'key={aes_key.hex().upper()}\niv={iv.hex().upper()}\nlen={len(aes_key.hex())}')
    return aes_key, iv
