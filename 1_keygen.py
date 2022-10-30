import rsa
from cryptography.hazmat.primitives import serialization as crypto_serialization
# from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

# # source tutorial-env/bin/activate
(pubkey, privkey) = rsa.newkeys(2048)

with open ('pubkey.key', 'wb') as key_file:
    key_file.write(pubkey.save_pkcs1('PEM'))
    print("Public Key Created")

    
with open('privkey.key', 'wb') as key_file:
    key_file.write(privkey.save_pkcs1('PEM'))    
    print("Private Key Created")

