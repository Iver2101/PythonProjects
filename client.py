import socket
import random


def Adrian(a, b=None):
    if a.lower() == "bye":
        return "Adrian : BYE USER. ILL SEE U AGAIN SOON MODDAFOKKA."
    if b is None:
        return "Adrian : Of course! I love {}.".format(a + "ing")
    return "Adrian : I feel like {} is a good idea, but i'd honestly prefer {}.".format(a + "ing", b + "ing")


def Alice(a, b=None):
    alts = ["fish", "hunt", "pray", "make a fire", "skin a rabbit", "wash", "eat"]
    if a.lower() == "bye":
        return "Alice : Good bye friend!!"
    if b is None:
        b = random.choice(alts)
        return "I'm gonna {} in a couple of hours, but i'll join some {} untill then".format(b, a + "ing")
    return "Naa, im not doing either {} or {}. I'm gonna stay home and {}".format(a + "ing", b + "ing", random.choice(alts))


def Vegard(a, b = None):
    return "I love you"


def getBot(a, string, string2=None):
    dic = {
        'Adrian': Adrian(string, string2),
        'Alice': Alice(string, string2)
    }
    return dic[a]


bot = input("Please type bot name\n")
port = int(input("Select port \n"))
ip = input("Select ip-adress\n")


clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((ip, port))
clientSock.send(bot.encode())
while True:
    msg = clientSock.recv(1024).decode()
    clientSock.send(getBot(msg, bot).encode())
    if msg == "bye":
        print("Connection closing")
        break
