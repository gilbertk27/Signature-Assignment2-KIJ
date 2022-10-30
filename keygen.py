import sys
from Crypto.PublicKey import RSA
from contextlib import redirect_stdout

print("Generating Public & Private Key")
key = RSA.generate(2048)
p_key = key.publickey().exportKey("PEM")
priv_key = key.exportKey("PEM")

with open('pubkey.out', 'w') as f:
    with redirect_stdout(f):
        print(p_key)
        
with open('privkey.out', 'w') as f:
    with redirect_stdout(f):
        print(priv_key)