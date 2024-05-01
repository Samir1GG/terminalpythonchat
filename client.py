import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("", )) #host, port

done = False

while not done:
    client.send(input("You: ").encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")

    if msg == "quit":
        done = True
    else:
        print("Partner: " + msg)
    

client.close()