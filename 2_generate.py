import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

# python 2_generate.py privkey.key MAP.pdf signature.sig

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

# Read all file contents
with open(key_f, 'rb') as f: key = f.read()
with open(data_f, 'rb') as f: data = f.read()

generate_signature(key, data, sig_f)