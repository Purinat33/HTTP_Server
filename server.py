from connection import *


def get(url='/'):
    if url == '/':
        pass


def parse_header(header: bytes):
    # Split into Lines
    header_str = header.decode()
    lines = header_str.split('\n')

    # Line 0
    if 'GET' in lines[0]:
        targets = lines[0].split(' ')  # GET / HTTP/1.1
        get(targets[1])  # /


def build_response(method, target, data):
    """_summary_

    Args:
        method (_type_): _description_
        target (_type_): _description_
        data (_type_): _description_
    """
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
            # build_response()
            print(data)
            break

    s.close()
