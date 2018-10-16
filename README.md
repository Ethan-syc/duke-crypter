# duke-crypter
Simple encryption/decryption python command line tool for Duke ECE590 Computer and Information Security HW2 Q11

## Requirement
Python cryptography library: <br>
pip3 install cryptography

## How to use it?
usage: duke-crypter [-h] [-e <input_file> <output_file>]
                    [-d <input_file> <output_file>]

duke-crypter by Ethan Shi to encrypt/decrypt a file

optional arguments:<br>
  -h, --help            show this help message and exit<br>
  encryption mode: python3 ./duke-crypter.py -e <input_file> <output_file> <br>
  decryption mode: python3 ./duke-crypter.py -d <input_file> <output_file> <br>

## Reference
Using PBKDF2HMAC for key stretching and using Fernet for enctyption/decryption<br>
https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/

Fernet is built on top of a number of standard cryptographic primitives. Specifically it uses:<br>
1. AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.<br>
2. HMAC using SHA256 for authentication.<br>
3. Initialization vectors are generated using os.urandom().<br>
https://cryptography.io/en/latest/fernet/
