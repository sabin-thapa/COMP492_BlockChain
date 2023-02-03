import unittest
from server import server
from client import client
from encryption_keys_generator import keys_generator
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generating all the keys and saving to files
keys_generator()

# Importing required keys from the files
server_private_key = RSA.import_key(open('server_private_key.pem').read())
server_private_key = PKCS1_OAEP.new(server_private_key)

server_public_key = RSA.import_key(open('server_public_key.pem').read())
server_public_key = PKCS1_OAEP.new(server_public_key)

client_public_key = RSA.import_key(open('client_public_key.pem').read())
client_public_key = PKCS1_OAEP.new(client_public_key)

client_private_key = RSA.import_key(open('client_private_key.pem').read())
client_private_key = PKCS1_OAEP.new(client_private_key)

msg_from_client = 'I am a client'
msg_from_server = 'I am a server'

#Test Cases 
class TestSecureCommunication(unittest.TestCase):
    def test_server_encryption(self):
        self.ciphertext = server_public_key.encrypt(msg_from_client.encode())
        self.plaintext = server_private_key.decrypt(self.ciphertext)
        self.plaintext = self.plaintext.decode('utf-8')
        self.assertEqual(self.plaintext, msg_from_client)
    
    def test_client_encryption(self):
        self.ciphertext = client_public_key.encrypt(msg_from_server.encode())
        self.plaintext = client_private_key.decrypt(self.ciphertext)
        self.plaintext = self.plaintext.decode('utf-8')
        self.assertEqual(self.plaintext, msg_from_server)

if __name__ == '__main__':
    unittest.main()