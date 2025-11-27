from connection import *


def parse_header(header: bytes):
    pass


def build_response():
    pass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print(f"Connection Accepted from {addr}")
        while True:
            data = conn.recv(1024)
            parse_header(data)
            if not data:
                break
            print(data.decode())

    s.close()
