import sys
from Crypto.PublicKey import RSA
from contextlib import redirect_stdout

print("Generating Public & Private Key")
key = RSA.generate(2048)
p_key = key.publickey().exportKey(RSA)
priv_key = key.exportKey(RSA)

with open('out.txt', 'w') as f:
    with redirect_stdout(f):
        print('p_key')