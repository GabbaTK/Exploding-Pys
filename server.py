import socket
from os import system
from json import load
from time import sleep

ASSETS = {}
PLAYERS = []

with open("assets.json", "r", encoding="utf-8") as ASSETS_FILE:
    ASSETS = load(ASSETS_FILE)

PORT = 8651
IP = socket.gethostbyname(socket.gethostname())
SERVER_ADDRESS = (IP, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT!"
HEADER = 64

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(SERVER_ADDRESS)

def sendData(PLAYER, MESSAGE):
    MESSAGE = MESSAGE.encode(FORMAT)
    MESSAGE_LENGHT = str(len(MESSAGE)).encode(FORMAT) + b" " * (HEADER - (len(str(len(MESSAGE)).encode(FORMAT))))
    PLAYER.send(MESSAGE_LENGHT)
    PLAYER.send(MESSAGE)

def receiveData(PLAYER):
    LENGHT = PLAYER.recv(HEADER).decode(FORMAT)
    DATA = PLAYER.recv(int(LENGHT)).decode(FORMAT)

    return DATA

def startServer():
    SERVER.listen()

    print(ASSETS["LOGO"]["LOGO"])
    print()
    print(f"SERVER IS LISTENING ON {IP}")
    PLAYER_AMMOUNT = input("How many players will be joining >>>")

    for PLAYER_INDEX in range(int(PLAYER_AMMOUNT)):
        PLAYER, ADDRESS = SERVER.accept()
        print(f"NEW CONNECTION FROM {ADDRESS[0]}")
        NAME = receiveData(PLAYER)
        print(f"Player name is {NAME}")
        PLAYERS.append([PLAYER, NAME])

    print("STARTING GAME")

    print("...5", end="\r")
    sleep(1)
    print("...4", end="\r")
    sleep(1)
    print("...3", end="\r")
    sleep(1)
    print("...2", end="\r")
    sleep(1)
    print("...1")
    sleep(1)

    system("cls")

if __name__ == "__main__":
    startServer()