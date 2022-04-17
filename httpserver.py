import socket

host = ""
port = 12570
buff_size = 128
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock_address = (host, port)
sock.bind(sock_address)

sock.listen(5)

while True:
    print("waiting request...")
    data, address = sock.accept()
    message = data.recv(buff_size)
    print(message.decode())

    if message:
        respone = "HTTP/1.1 200 ok\r\nContent-Type: text/html\r\n\r\n<HTML><BODY><H1>Hello, World! </H1></BODY></HTML>"
        data.sendall(respone.encode())

data.close()






