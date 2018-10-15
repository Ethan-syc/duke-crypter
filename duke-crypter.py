import argparse
import sys
import cryptography
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(prog="duke-crypter", description="duke-crypter by Ethan Shi to encrypt/decrypt a file")
parser.add_argument("-e", nargs=2, help="encryption mode", metavar=("<input_file>", "<output_file>"))
parser.add_argument("-d", nargs=2, help="decryption mode", metavar=("<input_file>", "<output_file>"))
args = parser.parse_args()
if len(sys.argv) == 1:
    parser.print_help()
    exit(1)
if args.e is not None:
    key = Fernet.generate_key()
    print(key)
    print("Your private key is", key.decode('utf-8'))
    encrypt_cipher_suite = Fernet(key)
    print(encrypt_cipher_suite)
    encrypted_file_bytes = open("plain_text.txt", "rb").read()
    cipher_text = encrypt_cipher_suite.encrypt(encrypted_file_bytes)
    output_file = open("encrypted.txt", "wb")
    output_file.write(cipher_text)
    exit(0)
if args.d is not None:
    key = input("enter your private key: ")
    print(key)
    print(key.encode('utf-8'))
    decrypt_cipher_suite = Fernet(key.encode('utf-8'))
    file_need_decrypt = open("encrypted.txt", "rb")
    try:
        plain_text = decrypt_cipher_suite.decrypt(file_need_decrypt)
        output_file = open("decrypted.txt", "wb")
        output_file.write(plain_text)
        exit(0)
    except cryptography.fernet.InvalidToken:
        exit(1)
