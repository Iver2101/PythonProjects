import socket
import thread

host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Ready...')

s.bind((host, port))
print('Bind Ready...')

print('Listening...')
s.listen(1)

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data: break
        print('Client says: ' + data)
        print('Sending: ' + data)
        client_socket.send(data)
    client_socket.close()

while True:
    client_socket, addr = s.accept()
    print('Conexion from: '+str(addr))
    thread.start_new_thread(handle_client ,(client_socket,))
s.close()