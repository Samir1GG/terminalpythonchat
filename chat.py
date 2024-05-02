import socket

def start_server(port=4444):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    server.listen()
    print(f"Server was started {port}...")
    conn, addr = server.accept()
    print(f"Device was connected with IP: {addr[0]}")
    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"{addr[0]}: {data}")
    conn.close()
    server.close()

def start_client(server_ip, port=4444):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))
    print(f"Connected to the server {server_ip}:{port}")
    while True:
        message = input("Enter your message (or 'exit' to quit the program): ")
        if message.lower() == 'exit':
            break
        client.sendall(message.encode('utf-8'))
    client.close()

if __name__ == '__main__':
    mode = input("Choose: 'server' or 'client': ").lower()
    if mode == 'server':
        start_server()
    elif mode == 'client':
        server_ip = input("Enter server's IP: ")
        start_client(server_ip)
    else:
        print("Error. Try again")