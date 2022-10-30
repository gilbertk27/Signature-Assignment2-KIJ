import sys
import os.path
from pathlib import Path
import rsa
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

# python script.py privkey.key MAP.pdf signature.sig

if (len(sys.argv) < 4):
    quit()

key_f = sys.argv[1]
data_f = sys.argv[2]
sig_f = sys.argv[3]

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
with open(key_f, 'rb') as f: key = f.read()

# my_file = Path("/privkey.key")
# if my_file.is_file():
#     # file exists
#     print(my_file)
# else:
#     (pubkey, privkey) = rsa.newkeys(2048)
#     with open ('pubkey.key', 'wb') as key_file:
#         key_file.write(pubkey.save_pkcs1('PEM'))
#     with open('privkey.key', 'wb') as key_file:
#         key_file.write(privkey.save_pkcs1('PEM'))
#         with open(key_f, 'rb') as f: key = f.read()
#         with open(privkey, 'rb') as f: data = f.read()
    
# if (isdir == True):
#     with open(key_f, 'rb') as f: key = f.read()
# elif (isdir == False):
#     (pubkey, privkey) = rsa.newkeys(2048)
#     with open ('pubkey.key', 'wb') as key_file:
#         key_file.write(pubkey.save_pkcs1('PEM'))
#     with open('privkey.key', 'wb') as key_file:
#         key_file.write(privkey.save_pkcs1('PEM'))
#         with open(key_f, 'rb') as f: key = f.read()
#         # with open(privkey, 'rb') as f: data = f.read()
        
generate_signature(key, data, sig_f)