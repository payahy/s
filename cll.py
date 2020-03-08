# -*- coding: utf-8 -*-
from xBots import *
from multiprocessing import Pool, Process
from subprocess import check_output
from datetime import datetime
from threading import Thread
from time import sleep
from bs4 import BeautifulSoup
import time, random, pytz, atexit, ctypes, livejson, sys, shutil, json, codecs, ast, threading, glob, re, string, asyncio, os, traceback, requests, six, urllib, urllib.parse
botStart = time.time()
InexBots = ["MID KONTROL"] #MID INDUK
Pasukan = ["MID BOT"] #MID BOT
Help1 ="""\n╭┉┉┅┄┄┈•◦ೋ•◦❥•◦ೋ• ╮
┊    ✧ *:･xᴛᴄ ᴍᴇɴᴜ:･ﾟ✧
╰ •◦ೋ•◦❥•◦ೋ•┈┄┄┅┉┉╯
╭┉┉┅┄┄┈•◦ೋ•◦❥•◦ೋ•╮
┊ೋ ᴀᴅᴅᴀᴅᴍɪɴ @
┊ೋ ᴀᴅᴅʙᴏᴛ @
┊ೋ ᴄʙᴏᴛ
┊ೋ ʙᴀᴄᴋᴜᴘ ᴏɴ-ᴏғғ
┊ೋ sᴘᴇᴇᴅ-sᴘ
┊ೋ ᴋᴇʟᴜᴀʀ(,)/ᴍᴀsᴜᴋ(.)
┊ೋ ᴘɪɴɢ/ᴀʟʟʙᴏᴛs
┊ೋ ᴄᴇᴋ ʙᴏᴛ/ᴄᴇᴋ
┊ೋ˚❁ೃೀ๑۩۞۩๑ೃೀ❁ೋ˚
┊ೋ ᴄʀᴏᴛ @
┊ೋ ᴊᴇᴍʙᴜᴛ 「ɴᴀᴍᴇ」
┊ೋ˚❁ೃೀ๑۩۞۩๑ೃೀ❁ೋ˚
┊ೋ ʙᴀɴʟɪsᴛ
┊ೋ ᴄʟᴇᴀʀʙᴀɴ
┊ೋ /ʀᴇʀsᴛᴀʀᴛ
┊ೋ ᴀᴜᴛᴏᴊᴏɪɴ ᴏɴ-ᴏғғ
┊ೋ ᴊᴏɪɴǫʀ ᴏɴ-ᴏғғ
╰ •◦ೋ•◦❥•◦ೋ•┈┄┄┅┉┉╯
      https://bit.ly/2SXahi7"""
main = codecs.open("mode.json","r","utf-8")
mode = json.load(main)
with open('mode.json', 'r') as fp:
  mode = json.load(fp)
def restart_program():
  time.sleep(0.1)
  python = sys.executable
  os.execl(python, python, *sys.argv)
def backupData():
  try:
    backup = mode
    f = codecs.open('mode.json','w','utf-8')
    json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
    return True
  except Exception as xbots:
    lix = str(xbots)
    if "reason=None" in lix:
      print (lix)
      time.sleep(0.001)
      restart_program()
    return False
def command(text):
  pesan = text.lower()
  if mode["setKey"] == True:
    if pesan.startswith(mode["keyCommand"]):
      cmd = pesan.replace(mode["keyCommand"],"")
    else:
      cmd = "Undefined command"
  else:
    cmd = text.lower()
  return cmd
def restartBot():
  backupData()
  time.sleep(0.1)
  python = sys.executable
  os.execl(python, python, *sys.argv)
class Xbots(object):
  def __init__(self, name, authQR=None):
    self.name    = name
    self.name    = self.name+' '
    self.authQR = authQR
    self.login(authQR)
    self.run()
  def login(self, auth):
    try:
      self.client = LINE(idOrAuthToken=auth)
      self.client.log(str(self.client.authToken))
    except Exception as error:
      traceback.print_tb(error.__traceback__)
    self.mid = self.client.getProfile().mid
  def run(self):
    while True:
      try:
        self.operations = self.client.poll.fetchOperations(self.client.revision, 10)
        for op in self.operations:
          if (op.type != OpType.END_OF_OPERATION):
            self.client.revision = max(self.client.revision, op.revision)
            self.bot(op)
      except Exception as error:
        print(error)
  def bot(self, op):
    try:
      if op.type is None:
        pass
      else:
        if op.type == 0:
          pass
        else :
          print("[ {} ] {}".format(str(op.type), OpType._VALUES_TO_NAMES[op.type]))
