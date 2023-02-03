import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from encryption_keys_generator import keys_generator


# PKCS1_OAEP is an asymmetric cipher based on RSA and the OAEP padding
#OAEP - Optimal Assymetric Encryption Padding
def server(HOST, PORT):
   
    server_private_key = RSA.import_key(open('server_private_key.pem').read())
    server_private_key = PKCS1_OAEP.new(server_private_key)

    client_public_key = RSA.import_key(open('client_public_key.pem').read())
    client_public_key = PKCS1_OAEP.new(client_public_key)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f'Server has started listening at: {HOST}:{PORT}')
        print('Waiting for client ...')

        conn, addr = server.accept()

        with conn:
            print(f'Connection established with {addr}')
            init_msg = b'Server waves hi!'
            init_msg = client_public_key.encrypt(init_msg)

            conn.sendall(init_msg)

            while True:
                data = conn.recv(2048)
                data = server_private_key.decrypt(data)
                data = data.decode('utf-8')
                if not data:
                    print('Connection Terminated! No data from client!')
                    break 
                print('Client: ' + data)
                data = input('Message: ')
                data = client_public_key.encrypt(data.encode())
                conn.sendall(data)
            conn.close()

if __name__ == '__main__':
    
    HOST = input('Enter the HOST IP: (default: 127.0.0.1): ')
    if HOST == '':
        HOST = '127.0.0.1'
    PORT = int(input('Enter the PORT number: '))

    #call key generator method
    keys_generator()

    #run the server
    server(HOST, PORT)