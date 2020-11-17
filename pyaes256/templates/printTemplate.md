### ${aesMode} PaperWallet ($generationDateTime) 

####Base64 CypherText:

<p class="blocktext">$cyphertext</p>

![$qrCodeFile]($qrCodeFile?style=centerme)

`The algorithm this was generated with is AES-256-CBC. It is the same openssl is using in this config.`
`PBKDF2 is used for derivating the AES key from the password. We were using 10000 iterations`

####Decryption:

##### With Python:
1. Install Python
2. Get Code from github `git clone https://github.com/The-Crocop/pyaes256`
3. pip install all dependencies
4. Scan or copy over the Cyphertext or scan the QR Code
5. run: `python aes256.py decrypt --input <cyphertext> --password <password>`

##### With OpenSSL:
Hint: `openssl is using "Salt__" to start of the cyphertext followed by 8 bytes of the actual salt.`

1. Create File `cypher.txt`
2. Add cyphertext to file eg. `echo "<cyphertext>\n" > cypher.txt` 
   Be Careful remove all linebreaks from cyphertext.
   Put one linebreak at the end of the file as indicated above (`\n`). 
    Openssl relies on that else you get an error.
3. openssl aes-256-cbc -d -base64 -pbkdf2 -in cypher.txt -out cypher_decrypted.txt
4. read content of file `cypher_decrypted.txt`
