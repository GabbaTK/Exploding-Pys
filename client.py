import socket
from os import system
from json import load

ASSETS = {}

with open("assets.json", "r", encoding="utf-8") as ASSETS_FILE:
    ASSETS = load(ASSETS_FILE)

PORT = 8651
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT!"
HEADER = 64

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendData(MESSAGE):
    MESSAGE = MESSAGE.encode(FORMAT)
    MESSAGE_LENGHT = str(len(MESSAGE)).encode(FORMAT) + b" " * (HEADER - (len(str(len(MESSAGE)).encode(FORMAT))))
    CLIENT.send(MESSAGE_LENGHT)
    CLIENT.send(MESSAGE)

def receiveData():
    LENGHT = CLIENT.recv(HEADER).decode(FORMAT)
    DATA = CLIENT.recv(int(LENGHT)).decode(FORMAT)

    return DATA

def startClient():
    print(ASSETS["LOGO"]["LOGO"])
    print()
    IP = input("Enter the ip of the server >>>")
    ADDRESS = (IP, PORT)
    CLIENT.connect(ADDRESS)
    NAME = input("What is your name >>>")
    sendData(NAME)
    system("cls")

if __name__ == "__main__":
    startClient()