from connection import *


def build_request(url=HOST):
    header = f"""GET / HTTP/1.1
Host: {HOST}

    
    """

    return header.encode()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(build_request())
