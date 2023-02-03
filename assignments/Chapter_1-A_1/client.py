import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def client(HOST, PORT):
    server_public_key = RSA.import_key(open('server_public_key.pem').read())
    server_public_key = PKCS1_OAEP.new(server_public_key)

    client_private_key = RSA.import_key(open('client_private_key.pem').read())
    client_private_key = PKCS1_OAEP.new(client_private_key)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        data = client.recv(1024)
        data = client_private_key.decrypt(data)
        data = data.decode("utf-8")

        print('Server : ' + data)
        msg = input('  Message: ')

        while msg.lower().strip() != 'end':
            msg = server_public_key.encrypt(msg.encode())
            client.sendall(msg)
            data = client.recv(1024)
            data = client_private_key.decrypt(data)
            data = data.decode("utf-8")
            print(' Server : ' + data)
            msg = input(' Message: ')
        
        msg = server_public_key.encrypt(msg.encode())
        client.sendall(msg)
        client.close()      

if __name__ == '__main__':
    
    HOST = input('Enter the HOST IP: (default: 127.0.0.1): ')
    if HOST == '':
        HOST = '127.0.0.1'
    PORT = int(input('Enter the PORT number: '))

    #run the client
    client(HOST, PORT)