import threading
import socket


def cliente():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5000))
    client.sendall("comprar".encode())

    resposta = client.recv(1024).decode()
    print(resposta)

    client.close()


threads = []

for i in range(20):  # 20 clientes simultâneos
    t = threading.Thread(target=cliente)
    threads.append(t)
    t.start()

for t in threads:
    t.join()