# P2P Network - File Transfer Praceice - Server Part
# It's complecated to implement the P2P Network in a colab environment
# It's good to run server part in a Linux based terminal and
# client part in separate terminal
import socket

def receive_file(file_path, host, port):
    # Create a socket and bind to the host and port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    print("Server listening on {}:{}...".format(host, port))

    # Wait for a client to connect
    conn, addr = sock.accept()
    print("Connection from {} established.".format(addr))

    # Open the file and receive data from the client
    with open(file_path, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    conn.close()
    print("File received successfully!")

if __name__ == '__main__':
    file_path = input("Enter file path: ")
    host = input("Enter host IP: ")
    port = int(input("Enter port number: "))
    receive_file(file_path, host, port)
