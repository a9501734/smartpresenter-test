import socket

TCP_HOST = '127.0.0.1'
TCP_PORT = 6000

def test_tcp_ping():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        s.connect((TCP_HOST, TCP_PORT))
        s.sendall(b'ping')
        data = s.recv(1024)
    assert data == b'pong', f"Expected 'pong', got {data}"

def test_tcp_unkown_command():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        s.connect((TCP_HOST, TCP_PORT))
        s.sendall(b'unknown_command')
        data = s.recv(1024)
    assert data == b'unknown command', f"Expected 'Unknown command', got {data}"