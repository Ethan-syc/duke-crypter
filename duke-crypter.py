#! /usr/bin/python3.7
import argparse
import sys
import cryptography
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

parser = argparse.ArgumentParser(prog="duke-crypter", description="duke-crypter by Ethan Shi to encrypt/decrypt a file")
parser.add_argument("-e", nargs=2, help="encryption mode", metavar=("<input_file>", "<output_file>"))
parser.add_argument("-d", nargs=2, help="decryption mode", metavar=("<input_file>", "<output_file>"))
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    exit(1)
if args.e is not None:
    password = input("enter your private key: ").encode('utf-8')
    backend = default_backend()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'1342454395842834',
        iterations=100000,
        backend=backend)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    encrypt_cipher_suite = Fernet(key)
    try:
        plain_text_file = open(args.e[0], "rb")
        plain_text_bytes = plain_text_file.read()
        plain_text_file.close()
        cipher_text_bytes = encrypt_cipher_suite.encrypt(plain_text_bytes)
        output_file = open(args.e[1], "wb")
        output_file.write(base64.urlsafe_b64decode(cipher_text_bytes))
        output_file.close()
        print("encryption succeed")
        exit(0)
    except OSError:
        print("can't open file", args.e[0])
        exit(1)

if args.d is not None:
    try:
        file_need_decrypt = open(args.d[0], "rb")
        password = input("enter your private key: ").encode('utf-8')
        backend = default_backend()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'1342454395842834',
            iterations=100000,
            backend=backend)
        key = base64.urlsafe_b64encode(kdf.derive(password))
        decrypt_cipher_suite = Fernet(key)
        plain_text = decrypt_cipher_suite.decrypt(base64.urlsafe_b64encode(file_need_decrypt.read()))
        output_file = open(args.d[1], "wb")
        output_file.write(plain_text)
        print("decryption succeed")
        exit(0)
    except OSError:
        print("can't open file", args.d[0])
        exit(1)
    except cryptography.fernet.InvalidToken:
        print("decryption failure, exiting, the key could be wrong or the encrypted message could be modified")
        exit(1)