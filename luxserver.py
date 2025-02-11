import socket
from sys import argv
import sys
import threading

"""
1. Set up socket
2. Listen
3. Accept request
4. Handle
"""
host = ''

"""luxserver.py is an echo program right now, implement later"""

def handle_client(socket):
    """Receives and sends communication with client"""
    while True:
        try:
            # Receive message from the client
            data = socket.recv(1024).decode()
            if not data:
                break  # Exit if no data received
            print(f"Received {data}")

            # Echo the message back to the client
            socket.send(data.encode())

        except ConnectionResetError:
            break  # Handle client disconnection
    print(f"Connection closed")
    socket.close()

def start_server(port):
    """Starts the server on specified port"""
    port = int(argv[1])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Echo Server listening on {host}:{port}")

        while True:
            client_socket, address = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_socket, address)).start()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()

# def main():
#     """Main function."""

if __name__ == "__main__":
    #main()
    try:
        port = int(sys.argv[1])
        if not (1024 <= port <= 65535):
            raise ValueError("Port number must be between 1024 and 65535.")
    except ValueError as e:
        print(f"Invalid port: {e}")
        sys.exit(1)

    start_server(port)