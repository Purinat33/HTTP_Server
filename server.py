from connection import *
from datetime import datetime


def get(url='/'):
    if url == '/':
        # / for index.html
        return build_response(200)
    else:
        # Else we go with 404 for now
        # In the future we might have other files/pages
        return build_response(404)


def parse_header(header: bytes):
    # Split into Lines
    header_str = header.decode()
    lines = header_str.split('\n')

    # Line 0
    if 'GET' in lines[0]:
        targets = lines[0].split(' ')  # GET / HTTP/1.1
        return get(targets[1])  # /
    # POST PUT DELETE etc. logic


def parse_body(body: bytes):
    pass


def build_response(status):
    now = datetime.now()
    day_idx = now.weekday()
    day_lst = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    day = day_lst[day_idx]

    if status == 200:
        header = f"""HTTP/1.1 200 OK
        Content-Type: text/html; charset=utf-8
        Date: {day}, 
        """
    # Same thing as the get comments
    # 201, 301 etc. etc. For now these two are suffice
    else:
        header = f"""HTTP/1.0 404 Not Found
        """

    # Maybe we only do that first line and connect to the rest of the header outside the if-else
    # Need more study of headers
    return header.encode()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print(f"Connection Accepted from {addr}")
        while True:
            data = conn.recv(1024)
            res = parse_header(data)
            if not data:
                break
            conn.sendall(res)
            break

    s.close()

# Can OOP deal with the connection between the functions?


class HTTPServer:
    def __init__(self, Host, Port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
