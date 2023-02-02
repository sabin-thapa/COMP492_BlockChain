from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def keys_generator():
    key_for_server = RSA.generate(1024)
    key_for_client = RSA.generate(1024)

    '''Keys Generation'''

    #SERVER
    server_private_key = key_for_server.exportKey('PEM')
    server_public_key = key_for_server.publickey().exportKey('PEM')

    #CLIENT
    client_private_key = key_for_server.exportKey('PEM')
    client_public_key = key_for_server.publickey().exportKey('PEM')

    '''Keys Storage'''

    # SERVER - PRIVATE KEY
    with open('server_private_key.pem', 'wb') as file: #'wb' for writing in the binary file
        file.write(server_private_key)
        file.close()
    
    # SERVER - PUBLIC KEY
    with open('server_public_key.pem', 'wb') as file:
        file.write(server_public_key)
        file.close()

    # CLIENT - PRIVATE KEY
    with open('client_private_key.pem', 'wb') as file:
        file.write(client_private_key)
        file.close()
    # CLIENT - PUBLIC KEY
    with open('client_public_key.pem', 'wb') as file:
        file.write(client_public_key)
        file.close()

