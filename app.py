from ppadb.client import Client as AdbClient
from os import system as cmd
from time import sleep
from random import randint
from threading import Thread
from sys import exit

# Global var
HOST = "127.0.0.1"
PORT = 5037
SERIAL = "AU4HIZOV6LZ95LX8"
SPAM = True

# Screen size 1080x2400

# Coordinates
PLAYER = 150, 2360
PLAYER_UPGRADE = 920, 1675
BUILDING = 400, 2360
B1 = 920, 1675


def start_server():
    cmd("adb start-server")
    cmd("adb usb")


def spam_money():
    money_position = randint(1, 1080), 1080
    print(money_position)
    device.input_tap(money_position[0], money_position[1])


def kill_server():
    cmd('adb kill-server')


if __name__ == '__main__':
    start_server()  # Start server and connect device
    client = AdbClient(host=HOST, port=PORT)
    device = client.device(SERIAL)

    input("Press ENTER to continue...")

    while SPAM:
        try:
            spam_money()
            sleep(0.0000001)
        except KeyboardInterrupt:
            SPAM = False

    kill_server()
    exit(0)
