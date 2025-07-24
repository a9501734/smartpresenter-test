# mock_tcp_server.py
import socket  
import threading

HOST = '127.0.0.1'  # Localhost
PORT = 6000        # Port to listen on (non-privileged ports are >

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if data == b'ping':
                conn.sendall(b'pong')
            else:
                print(f"Received unexpected data: {data}")
                conn.sendall(b'unknown command')

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"TPC Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
if __name__ == "__main__":
    run_server()
    