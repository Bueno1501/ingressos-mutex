import socket
import threading

ingressos_disponiveis = 100

lock = threading.Lock()

def processar_cliente(conn, addr):
    global ingressos_disponiveis

    print(f"[NOVA CONEXÃO] {addr} conectado.")

    try:
        data = conn.recv(1024).decode()

        if not data:
            return

        resposta = ""

        with lock:
            if ingressos_disponiveis > 0:
                ingressos_disponiveis -= 1
                resposta = f"✅ Ingresso comprado com sucesso! Restam {ingressos_disponiveis}"
            else:
                resposta = "❌ Ingressos esgotados!"

        conn.sendall(resposta.encode())

    except Exception as e:
        print(f"[ERRO] {addr}: {e}")

    finally:
        conn.close()
        print(f"[DESCONECTADO] {addr}")

def iniciar_servidor():
    host = "0.0.0.0"
    porta = 5000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()

    print(f"[SERVIDOR] Rodando em {host}:{porta}")

    while True:
        conn, addr = servidor.accept()

        thread = threading.Thread(target=processar_cliente, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()
