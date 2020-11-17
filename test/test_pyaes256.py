from pyaes256.decrypt import decrypt
from pyaes256.encrypt import encrypt


def test_encrypt_and_decrypt():
    # given:
    secret = 'young cement bubble network scout radio mask output maze alone balance seed party large couch forget' \
             ' paddle swarm person way yard switch open loop\n'
    password = b'abcdefg'
    # when:
    encrypted_text = encrypt(secret, password)
    print(encrypted_text)
    decrypted_text = decrypt(encrypted_text, password)
    print(decrypted_text)
    # then
    assert secret == decrypted_text


def test_decrypt_generated_by_openssl():
    # given:
    expected_output = 'young cement bubble network scout radio mask output maze alone balance seed party large couch' \
                      ' forget paddle swarm person way yard switch open loop\n'
    password = b'abcdefg'
    text_to_decrypt = 'U2FsdGVkX1/HEDOl4/ffIWPNVohxRpJleiPUp4VRKxkoBN2YUny/kFVh/3lp06+WAhnUAxsW5yBtGPZLV6e2314pgi' \
                      'FXbth4nEZ4xOtyNEHlYb3cBcjsDMrmZz4O41iN8lf+Hj6oKl7tD/nnQ5kMFHm1GE+1zDDJ0N0r/M2pvCuSAVXPFWD7' \
                      'F1NlsVjG9g9I8rz2/9CdpYiM8d7sAa0CeMNRauUqYegMY+X5NlB/rXY='
    # when:
    decrypted_text = decrypt(text_to_decrypt, password)
    # then:
    assert decrypted_text == expected_output
