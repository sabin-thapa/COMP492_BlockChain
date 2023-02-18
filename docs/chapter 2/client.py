#
# P2P Network - File Transfer Practice - Client Part
# It's complecated to implement the P2P Network in a colab environment
# It's good to run server part in a Linux based terminal and
# client part in separate terminal
#
import socket

def send_file(file_path, host, port):
    # Create a socket and connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # Open the file and send data to the server
    with open(file_path, 'rb') as f:
        sock.sendall(f.read())
    sock.close()
    print("File sent successfully!")

if __name__ == '__main__':
    file_path = input("Enter file path: ")
    host = input("Enter host IP: ")
    port = int(input("Enter port number: "))
    send_file(file_path, host, port)