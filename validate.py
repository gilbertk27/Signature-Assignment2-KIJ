import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

# python validate.py pubkey.key MAP.pdf signature.sig

if (len(sys.argv) < 4):
    quit()

key_f = sys.argv[1]
data_f = sys.argv[2]
sig_f = sys.argv[3]

def verify_signature(key, data, sig_f):
    print("Verifying Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open(sig_f, 'rb') as f: signature = f.read()
    rsp = "Verification Success" if (signer.verify(h, signature)) else " Verification Failed"
    print(rsp)

# Read all file contents
with open(key_f, 'rb') as f: key = f.read()
with open(data_f, 'rb') as f: data = f.read()

verify_signature(key, data, sig_f)
    