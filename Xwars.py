from wariors import Xbots
import json, threading, codecs
def login(name, auth):
    bot = Xbots(name, auth)


threading.Thread(target=login, args=('b1','TOKEN_BOT')).start()

print("Login sukses")
