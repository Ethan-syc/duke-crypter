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
    print("Your private key is", key.decode('utf-8'))
    encrypt_cipher_suite = Fernet(key)
    try:
        plain_text_file = open(args.e[0], "rb")
        plain_text_bytes = plain_text_file.read()
        plain_text_file.close()
        cipher_text_bytes = encrypt_cipher_suite.encrypt(plain_text_bytes)
        output_file = open(args.e[1], "wb")
        output_file.write(cipher_text_bytes)
        output_file.close()
        print("encryption succeed")
        exit(0)
    except OSError:
        print("can't open file", args.e[0])
        exit(1)

if args.d is not None:
    try:
        file_need_decrypt = open(args.d[0], "rb")
        key = input("enter your private key: ")
        decrypt_cipher_suite = Fernet(key)
        plain_text = decrypt_cipher_suite.decrypt(file_need_decrypt.read())
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
