# -*- coding: utf-8 -*-
from xBot import *
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
Helps ="""\n╭┉┉┅┄┄┈•◦ೋ•◦❥•◦ೋ• ╮
┊    ✧ *:･xᴛᴄ ᴍᴇɴᴜ:･ﾟ✧
╰ •◦ೋ•◦❥•◦ೋ•┈┄┄┅┉┉╯
╭┉┉┅┄┄┈•◦ೋ•◦❥•◦ೋ•╮
┊ೋ ᴀᴅᴅ
┊ೋ ᴀᴅᴅᴀᴅᴍɪɴ @
┊ೋ ᴅᴇʟᴀᴅᴍɪɴ @
┊ೋ ᴀᴅᴍɪɴʟɪsᴛ
┊ೋ sᴘᴇᴇᴅ-sᴘ
┊ೋ ᴋᴇʟᴜᴀʀ(,)/ᴍᴀsᴜᴋ(.)
┊ೋ ᴘɪɴɢ
┊ೋ ᴄᴇᴋ
┊ೋ ᴍʏᴋᴇʏ
┊ೋ sᴇᴛᴋᴇʏ:
┊ೋ ʀᴇsᴇᴛᴋᴇʏ
┊ೋ˚❁ೃೀ๑۩۞۩๑ೃೀ❁ೋ˚
┊ೋ ᴄʀᴏᴛ @
┊ೋ ᴊᴇᴍʙᴜᴛ 「ɴᴀᴍᴇ」
┊ೋ˚❁ೃೀ๑۩۞۩๑ೃೀ❁ೋ˚
┊ೋ ʙᴀɴʟɪsᴛ
┊ೋ ᴄʟᴇᴀʀʙᴀɴ
┊ೋ /ʀᴇʀsᴛᴀʀᴛ
┊ೋ ᴊᴏɪɴ ᴏɴ-ᴏғғ
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
      Pbot = pesan.replace(mode["keyCommand"],"")
    else:
      Pbot = "Undefined command"
  else:
    Pbot = text.lower()
  return Pbot
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
    opp1 = op.param1
    opp2 = op.param2
    opp3 = op.param3
    Admin = mode["admin"]
    me = self.client
    meM = self.mid
    try:
      if op.type is None:
        pass
      else:
        if op.type == 0:
          pass
        else :
          print("[ {} ] {}".format(str(op.type), OpType._VALUES_TO_NAMES[op.type]))
      if op.type == 11:
        if opp2 not in mode["blacklist"]:pass
        else:
          X = me.getGroup(opp1)
          if X.preventedJoinByTicket == False:
            X.preventedJoinByTicket = True
            me.updateGroup(X)
            me.kickoutFromGroup(opp1,[opp2])
      if op.type == 13:
        if meM in opp3:
          if mode["autoJoin"] == True:
            if opp2 not in InexBots and opp2 not in Admin and opp2 not in Pasukan:
              me.rejectGroupInvitation(opp1)
            else:
              me.acceptGroupInvitation(opp1)
              wr = me.getGroup(opp1)
              ban = [contact.mid for contact in wr.members]
              for Z in ban:
                if Z in mode["blacklist"]:
                  try:
                    me.kickoutFromGroup(opp1,[Z])
                  except:pass
              print("blacklist kick ok")
        if opp3 in mode["blacklist"]:
          if opp2 in InexBots or opp2 in Admin or opp2 in Pasukan:pass
          else:
            invit1 = opp3.replace('\x1e',',')
            invit2 = invit1.split(',')
            for _mid in invit2:
              me.cancelGroupInvitation(opp1,[_mid])
            me.kickoutFromGroup(opp1, [opp2])
            mode["blacklist"][opp2] = True
        if opp2 in mode["blacklist"]:
          if opp3 in InexBots or opp3 in Admin or opp3 in Pasukan:pass
          else:
            invit1 = opp3.replace('\x1e',',')
            invit2 = invit1.split(',')
            for _mid in invit2:
              if _mid not in InexBots and _mid not in Pasukan and _mid not in Admin:
                me.cancelGroupInvitation(opp1,[_mid])
            me.kickoutFromGroup(opp1,[opp2])
      if op.type in [55,17]:
        if opp2 in mode["blacklist"]:
          if opp2 not in InexBots and opp2 not in Admin and opp2 not in Pasukan:
            me.kickoutFromGroup(op.param1, [op.param2])
          else:pass
      if op.type == 32:
        if opp3 in InexBots or opp3 in Admin or opp3 in Pasukan:
          if opp2 not in InexBots and opp2 not in Admin and opp2 not in Pasukan:
            mode["blacklist"][opp2] = True
            me.kickoutFromGroup(opp1,[opp2])
            me.inviteIntoGroup(opp1, Pasukan)
          else:pass
      if op.type == 19:
        if opp3 in InexBots or opp3 in Admin or opp3 in Pasukan:
          if opp2 not in InexBots and opp2 not in Admin and opp2 not in Pasukan:
            mode["blacklist"][opp2] = True
            try:
              me.acceptGroupInvitation(opp1)
              me.kickoutFromGroup(opp1, [opp2])
              me.inviteIntoGroup(opp1,[opp3])
            except:pass
        if opp3 in Admin:
          if opp2 in InexBots and opp2 in Admin and opp2 in Pasukan:
            pass
          else:
            mode["blacklist"][opp2] = True
            try:
              me.findAndAddContactsByMid(Admin)
              me.inviteIntoGroup(opp1, Admin)
              me.kickoutFromGroup(opp1,[opp2])
            except:pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      if op.type in [25,26]:
        msg = op.message
        text = msg.text
        msg_id = msg.id
        sender = msg._from
        if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
          if msg.toType == 0:
            if sender != me.profile.mid:
              to = sender
            else:
              to = receiver
          elif msg.toType == 1:
            to = receiver
          elif msg.toType == 2:
            to = receiver
          if msg.contentType == 0:
            if text is None:
              return
            else:
              Pbot = command(text)
              if cmd == "menu":
                if sender in InexBots or sender in Admin:
                  me.sendMessage(msg.to, Helps)
              elif Pbot == "/reboot" or Pbot == "/restart":
                if sender in InexBots or sender in Admin:
                  try:
                    me.sendMessage(msg.to, "ᴡᴀɪᴛɪɴɢ ᴀ sᴇᴄᴏɴᴅ.")
                    restartBot()
                  except:
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
              elif Pbot == "ping" or Pbot == "respon":
                if sender in InexBots or sender in Admin:
                  me.sendMessage(msg.to, None, contentMetadata={'mid': meM}, contentType=13)
              elif "addadmin" in Pbot:
                if sender in InexBots:
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  targets = []
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    if target in Admin:
                      me.sendMessage(msg.to, "Dia sudah admin bos")
                    else:
                      try:
                        Admin[target] = True
                        me.sendMessage(msg.to, "succes add admin")
                      except Exception as e:
                        me.sendMessage(msg.to, "[ ERROR ] \n" + str(e))
              elif "deladmin" in Pbot:
                if sender in InexBots:
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  targets = []
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    if target not in InexBots:
                      me.sendMessage(msg.to, "sebelumnya dia bukan admin")
                    else:
                      try:
                        del Admin[target]
                        me.sendMessage(msg.to, "succes delete admin")
                      except Exception as e:
                        me.sendMessage(msg.to, "[ ERROR ] \n" + str(e))
              elif Pbot == "adminlist":
                if sender in InexBots or sender in Admin:
                  if Admin == {}:
                    me.sendMessage(msg.to,"Admin List empty")
                  else:
                    mc = "╭━━━━━━━━━━━━━━━━─\n├─━━━━━━━━━━━━━━─"
                    num=1
                    lists = me.getContacts(Admin)
                    for mas in lists:
                      mc+="\n│  %i. %s" % (num, mas.displayName)
                      num=(num+1)
                    mc+="\n│\n│  Total %i Admin " % len(lists)
                    me.sendMessage(msg.to, mc + "\n╰━━━━━━━━━━━━━━━━─")
              elif Pbot == "add":
                if sender in InexBots or sender in Admin:
                  for Allbots in me:
                    for Creator in InexBots:
                      try:
                        Allbots.findAndAddContactsByMid(Creator)
                      except:pass
                    for Kickers in Pasukan:
                      try:
                        Allbots.findAndAddContactsByMid(Kickers)
                      except:pass
              elif Pbot == "mykey":
                if sender in InexBots or sender in Admin:
                  me.sendMessage(msg.to, "「 Status Setkey 」\nSetkey saat ini「 " + str(mode["keyCommand"]) + " 」")
              elif Pbot.startswith("setkey: "):
                if sender in InexBots or sender in Admin:
                  sep = text.split(" ")
                  key = text.replace(sep[0] + " ","")
                  if key in [""," ","\n",None]:
                    me.sendMessage(msg.to, "Gagal mengganti key")
                  else:
                    mode["keyCommand"] = str(key).lower()
                    me.sendMessage(msg.to, "「 Change Setkey 」\nSetkey diganti jadi「{}」".format(str(key).lower()))
              elif Pbot == "resetkey":
                if sender in InexBots or sender in Admin:
                  mode["keyCommand"] = ""
                  me.sendMessage(msg.to, "「 Resetkey 」\nSetkey mu telah direset")
              elif Pbot == "cek":
                if sender in InexBots or sender in Admin:
                  try:me.kickoutFromGroup(To, ["u951e70feab1a2b4f38fc1390f776a31b"]);mod = "OK"
                  except:mod = "NO"
                  try:me.cancelGroupInvitation(To, ["u951e70feab1a2b4f38fc1390f776a31b"]);mod1 = "OK"
                  except:mod1 = "NO"
                  try:me.inviteIntoGroup(To, ["u951e70feab1a2b4f38fc1390f776a31b"]);mod2 = "OK"
                  except:mod2 = "NO"
                  if mod == "OK":sil = "██████████ ᴋɪᴄᴋ : 100%"
                  else:sil = "██░░░░░░░░ ᴋɪᴄᴋ : 20%"
                  if mod1 == "OK":sil1 = "██████████ ᴄᴀɴsᴇʟ : 100%"
                  else:sil1 = "██░░░░░░░░ ᴄᴀɴsᴇʟ : 20%"
                  if mod2 == "OK":sil2 = "██████████ ɪɴᴠɪᴛᴇ : 100%"
                  else:sil2 = "██░░░░░░░░ ɪɴᴠɪᴛᴇ : 20%"
                  me.sendMessage(msg.to, "{}\n".format(sil)+"{}\n".format(sil1)+"{}".format(sil2))
              elif Pbot == "sp" or Pbot == "speed":
                if sender in InexBots or sender in Admin:
                  start = time.time()
                  me.getProfile()
                  elapsed_time = time.time() - start
                  me.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
              elif Pbot == "banlist":
                if sender in InexBots or sender in Admin:
                  if mode["blacklist"] == []:
                    me.sendMessage(msg.to,"ᴇᴍᴘᴛʏ ʙʟᴀᴄᴋʟɪsᴛ")
                  else:
                    ma = ""
                    a = 0
                    for m_id in mode["blacklist"]:
                      a = a + 1
                      end = '\n'
                      ma += str(a) + ". " +me.getContact(m_id).displayName +end
                    me.sendMessage(msg.to,"ʙʟᴀᴄᴋʟɪsᴛ\n"+ma+"\nᴛᴏᴛᴀʟ %s ʙʟᴀᴄᴋʟɪsᴛ " %(str(len(mode["blacklist"]))))
              elif Pbot == "cban" or Pbot == "clearban":
                if sender in InexBots or sender in Admin:
                  mode["blacklist"] = {}
              elif Pbot == "," or Pbot == "keluar":
                if sender in InexBots or sender in Admin:
                  me.leaveGroup(msg.to)
              elif Pbot.startswith("jembut "):
                if sender in InexBots or sender in Admin:
                  nk0 = text.replace("jembut ","")
                  nk1 = nk0.lstrip()
                  nk2 = nk1.replace("@","")
                  nk3 = nk2.rstrip()
                  _name = nk3
                  gs = me.getGroup(to)
                  targets = []
                  for s in gs.members:
                    if _name in s.displayName:
                      targets.append(s.mid)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      if target not in InexBots:
                        if target not in Pasukan:
                          try:
                            mode["blacklist"][target] = True
                            me.kickoutFromGroup(msg.to,[target])
                            print (to, [s.mid])
                          except Exception as A:
                            print(A)
              elif Pbot.startswith("crot "):
                if sender in InexBots or sender in Admin:
                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    lists = []
                    for mention in mentionees:
                      if mention["M"] not in lists:
                        lists.append(mention["M"])
                    for ls in lists:
                      try:
                        mode["blacklist"][ls] = True
                        me.kickoutFromGroup(msg.to,[ls])
                      except:
                        me.sendMessage(msg.to, "limit")
              elif Pbot == "joinqr:on" or Pbot == 'joinqr on':
                if sender in InexBots or sender in Admin:
                  mode["autoJoinTicket"] = True
                  me.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ ᴀʟʟʀᴇᴅʏ ᴏɴ")
              elif Pbot == "joinqr:off" or Pbot == 'joinqr off':
                if sender in InexBots or sender in Admin:
                  mode["autoJoinTicket"] = False
                  me.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ ᴀʟʟʀᴇᴅʏ ᴏғғ")
              elif Pbot == "join:on" or Pbot == 'join on':
                if sender in InexBots or sender in Admin:
                  mode["autoJoin"] = True
                  me.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴀʟʟʀᴇᴅʏ ᴏɴ")
              elif Pbot == "join:off" or Pbot == 'join off':
                if sender in InexBots or sender in Admin:
                  mode["autoJoin"] = False
                  me.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴀʟʟʀᴇᴅʏ ᴏғғ")
              elif '/ti/g/' in msg.text.lower():
                if mode["autoJoinTicket"] == True:
                  link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                  links = link_re.findall(text)
                  n_links = []
                  for l in links:
                    if l not in n_links:
                      n_links.append(l)
                  for ticket_id in n_links:
                    group = me.findGroupByTicket(ticket_id)
                  me.acceptGroupInvitationByTicket(group.id,ticket_id)
                  me.sendMessage(group.id, "Hallo semuanya... salam kenal")
                  me.sendMessage(msg.to,"ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ ᴀʟʟʀᴇᴅʏ "+group.name)
    except Exception as xbots:
      lix = str(xbots)
      if "reason=None" in lix:
        print (lix)
        time.sleep(0.0001)
        restart_program()

