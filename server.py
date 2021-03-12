import socket
from time import sleep
from threading import Thread
import _thread


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = int(input("Select port \n"))
s.bind(('localhost', port))
s.listen()
def handle_client(clientSock):
    while True:
        inp = input()
        send_msg = inp.split()[-1]
        clientSock.send(send_msg.encode())
        ut = clientSock.recv(1024).decode()
        print(ut)
        if inp == "bye":
            return "bye"


while True:
    print("Listening...")
    clientSock, data = s.accept()
    print("connected with {}".format(clientSock.recv(1024).decode()))
    print("Suggest something to do with your friend(s).\nRemember to have the verb as the last word in ur suggestion.\nAnd dont ask them questions!!!\n")
    ut = handle_client(clientSock)
    if ut == "bye":
        break
print("connection closing")
s.close()