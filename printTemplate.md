## ${aesMode} PaperWallet

###Base64 CypherText:

<code class="blocktext">
$cyphertext</code>

![$qrCodeFile]($qrCodeFile?style=centerme)

`The algorithm this was generated with is AES-256-ECB. It is the same openssl is using in this config.`
`PBKDF2 is used for derivating the AES key from the password. We were using 10000 iterations`

###Decryption:
1. Install Python
2. pip install all depenndencies
3. Scan or copy over the Cyphertext or scan the QR Code
4. run: `playaround.py --input <cyphertext> --password <password>`

Hint: `openssl is using "Salt__" to start of the cyphertext followed by 8 bytes of the actual salt.`
