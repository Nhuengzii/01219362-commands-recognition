#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('ifile', help='The file to encrypt', type=str)
parser.add_argument('ofile', help='The file to write the encrypted data to', type=str)

if __name__ == "__main__":
    key = os.environ.get('FIREBASE_KEY')
    if key is None:
        exit('No key found')
    args = parser.parse_args()

    fernet = Fernet(key.encode())

    with open(args.ifile, 'r') as f:
        raw = f.read()
        encrypted = fernet.encrypt(raw.encode())
        with open(args.ofile, 'w') as f:
            f.write(encrypted.decode())
        print('File encrypted')
