from connection import *

# https://developer.mozilla.org/en-US/docs/Glossary/Request_header


def build_request(url=HOST):
    header = f"""GET / HTTP/1.1
Host: {HOST}
    
    """

    return header.encode()


def parse_response(response: bytes):
    pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(build_request())

    res = s.recv(1024)
    data = parse_response(res)
