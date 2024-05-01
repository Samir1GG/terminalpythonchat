import socket
import rsa
import threading

choise = input("Host(1) or connect(2): ")
public_key, private_key = rsa.newkeys(1024)
public_partner = None


if choise == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("",)) #host, port
    server.listen()
    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
elif choise == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("", )) #host, port
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))
else:
    exit()


def sending_message(c):
    while True:
        message = input("")
        c.send(message.encode("utf-8"))
        print("You: " + message)

def recv_message(c):
    while True:
        data = c.recv(1024)
        print("Partner:" + data.decode("utf-8"))

threading.Thread(target=sending_message,args=(client,)).start()
threading.Thread(target=recv_message,args=(client,)).start()