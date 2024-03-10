from cryptography.fernet import Fernet
import os
import json

key = os.environ.get('FIREBASE_KEY')
if key is None:
    exit('No key found')
else:
    key = key.encode()

fernet = Fernet(key)

def decrypt():
    with open("firebase_credent_encrypted.txt", 'r') as f:
        raw_encrpyted = f.read()
        raw_decrypted = fernet.decrypt(raw_encrpyted.encode()).decode()
        cred = json.loads(raw_decrypted)
    return cred
