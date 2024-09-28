import socket

def start_server(ip, port):
    s = socket.socket()
    s.bind((ip, port))
    s.listen(5)
    return s

s = start_server('127.0.0.1', 8000)

while True:
    c, adr = s.accept()
    print (c.recv(1024).decode('utf-8'))
    print(adr)
    body = '<html><body><h1>Hello world!!!</h1></body></html>'
    CRLF = '\r\n'
    header = 'HTTP/1.1 200 OK'
    response = header + CRLF + CRLF + body
    c.send(response.encode('utf-8'))
    c.close()
    print('---')
