import unittest

from pyaes256.decrypt import decrypt
from pyaes256.encrypt import encrypt


class Test(unittest.TestCase):

    def test_encrypt_and_decrypt(self):
        # given:
        secret = 'young cement bubble network scout radio mask output maze alone balance seed party large couch forget paddle swarm person way yard switch open loop\n'
        password = b'abcdefg'
        # when:
        encrypted_text = encrypt(secret, password)
        print(encrypted_text)
        decrypted_text = decrypt(encrypted_text, password)
        print(decrypted_text)
        # then
        self.assertEqual(secret, decrypted_text)
        # decryptedText = decrypt(textToDecrypt, password)
        # print(decryptedText)

    def test_decrypt_generated_by_openssl(self):
        # given:
        expected_output = 'young cement bubble network scout radio mask output maze alone balance seed party large couch forget paddle swarm person way yard switch open loop\n'
        password = b'abcdefg'
        text_to_decrypt = 'U2FsdGVkX191+tp3e4BHcqh0mnsQpXJeOyEmkRR4Rha7bQR3EYsiCZsUrWjHv3LEWXnP1rUheLIxf3cbBNQSzR1MRIv8CMfXVi81X9VjrsbsvGJuSPT8G9cmG3RHrcWBQUdaHsl8bsHUMNTqgp/AMtivDT1WHkLnNFKYvOj3Fn9rk8gUL3I7Wl1afbmHcXj939C9VpkRmvjZedsSWCeSLGq4Qnf8le4eBTNx0Ewa2SI='
        # when:
        decrypted_text = decrypt(text_to_decrypt, password)
        # then:
        self.assertEqual(decrypted_text, expected_output)


if __name__ == '__main__':
    unittest.main()
