to encode text with aes256-ecb. Pick any password.
Example password = `abcdefghijklmnopqrstuvwxyz`

generate with openssl:
`echo -n 'mysupersecretseedphrase' | openssl enc  -aes-256-ecb -base64 -salt -pbkdf2 -out secretphrase-enc.txt`

Then type in your password.

to decode it run: 
`openssl enc -aes-256-ecb -d -base64 -salt -pbkdf2  -in secretphrase-enc.txt`

pbkdf2:
iterations: 10000
salt: 025A48E77BA0C755


Python:

`pip install pycrypto`
