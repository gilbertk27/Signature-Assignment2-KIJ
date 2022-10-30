import sys
from threading import Timer
import time
import os.path as path
from pathlib import Path
import rsa
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

# python 2_generate_edit.py MAP.pdf signature.sig

if path.exists("privkey.key"): 
    path = "privkey.key"
    with open(path, mode='r', encoding="utf-8" ) as key:
        key_f = key.read()
        print(key_f)
else: 
    (pubkey, key_f) = rsa.newkeys(2048)

    with open ('pubkey.key', 'wb') as key_file:
        key_file.write(pubkey.save_pkcs1('PEM'))
        print("Public Key Created")

    
    with open('privkey.key', 'wb') as key_file:
        key_file.write(key_f.save_pkcs1('PEM'))    
        print("Private Key Created")
        time.sleep(5)
    with open('privkey.key', mode='rb') as key:
        key_f = key.read()
        print(key_f)   
    
data_f = sys.argv[1]
sig_f = sys.argv[2]

def generate_signature(key, data, sig_f):
    print("Generating Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open(sig_f, 'wb') as f: f.write(signature)
    print("Signature Generated")

print("Checking Key")

with open(data_f, 'rb') as f: data = f.read()

generate_signature(key_f, data, sig_f)
