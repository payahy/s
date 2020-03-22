# -*- coding: utf-8 -*-
import xBot
from xBot import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
from akad.ttypes import LoginRequest
from akad import LineService
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from threading import Thread,Event
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize,pytz
from gtts import gTTS
from googletrans import Translator
from pytz import timezone
_session = requests.session()
botStart = time.time()
#WARNA
logIn = codecs.open("unsend.json","r","utf-8")
LoginBot = json.load(logIn)
merah = "#FF2800"
nila = "#4B0082"
kuning = "#FFFD00"
hijau = "#83FF00"
biru = "#00DAFF"
biruTua = "#0000FF"
ungu = "#C323FF"
ping = "#FF17CE"
hitam = "#000000"
putih = "#FFFFFF"
abuabu = "#000000cc"
sp_nila = {"type": "separator","color": nila}
sp_putih = {"type": "separator","color": "#FFFFFF"}
style_biru={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":biru}}
image1 = "https://1.bp.blogspot.com/-zyUmsriCmGE/XVYAO-lsFLI/AAAAAAAAGe8/BsSUwtUfFc0mxRGxE_8fOz3peuxB3t9UwCLcBGAs/s1600/20190816_074821.jpg"
image2 = "https://1.bp.blogspot.com/-zK32-fvqcNw/XVYAUCQhrmI/AAAAAAAAGfA/hXKs0MS2OIMKi09tJ7yCjnjUbMiuV_TIACLcBGAs/s1600/20190816_074438.jpg"
image3 = "https://1.bp.blogspot.com/-OgPmr5eJpYg/XVYAVFAYcaI/AAAAAAAAGfE/Xwh0EqB_SrclP-NZ_DaDqxcYnWBZSa_FgCLcBGAs/s1600/20190816_074311.jpg"
Pabuabu = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcROA9420U3BHcyOg97LAZh_cdGZreFn4rJpfDQV8a7WiGYkQpMW"
Gambar = (image1,image2,image3)
logo = "https://1.bp.blogspot.com/-6T7oMDOIlKA/XVX_8-oO52I/AAAAAAAAGe0/W0MubSIIyUUzw3et2YifTWqxaNRRwWE-ACLcBGAs/s1600/20190816_075636.png"
Warna = (merah,kuning,hijau,biru,ping,ungu)
warnanya1 = random.choice(Warna)
warnanya2 = random.choice(Warna)
warnanya3 = random.choice(Warna)
print("\n____________________________[SELFBOT]____________________________")
me = LINE("")
me.log("Auth Token : " + str(me.authToken))
meM = me.getProfile().mid
me.log("MID : " + str(meM))
print("""
░▀░ █▀▀▄ █▀▀ █░█ █▀▀▄ █▀▀█ ▀▀█▀▀ █▀▀ 
▀█▀ █░░█ █▀▀ ▄▀▄ █▀▀▄ █░░█ ░░█░░ ▀▀█ 
▀▀▀ ▀░░▀ ▀▀▀ ▀░▀ ▀▀▀░ ▀▀▀▀ ░░▀░░ ▀▀▀ 
▄█░ ░█▀█░ ▄ █▀▀█ ▄▀▀▄ ▄ █▀█ █▀▀█ ▄█░ ▄▀▀▄ 
░█░ █▄▄█▄ ░ █▄▀█ █▄▄░ ░ ░▄▀ █▄▀█ ░█░ ▀▄▄█ 
▄█▄ ░░░█░ ▀ █▄▄█ ▀▄▄▀ ▀ █▄▄ █▄▄█ ▄█▄ ░▄▄▀ """)
oepoll = OEPoll(me)
St = "┣"
Zx = [me]
meProfile = me.getProfile()
meSettings = me.getSettings()
set = {
  "Picture": False,
  "bot": True,
  "Conection": "cd7e4add16f8dcbca983d9275506aaa5a",
  "foto": {},
  "PASUKAN":{},
  "keyCommand":"",
  "restartPoint": {},
  "AddstickerTag": {
    "sid": "",
    "spkg": "",
    "status": False
   },
  "Addsticker": {
    "name": "",
    "status": False
  },
  "AddImage": {
    "name": "",
    "status": False
  },
  "Addaudio":{
    "name": "",
    "status":False
   },
  "Addvideo":{
    "name": "",
    "status":False
   },
  "myProfile": {
    "coverId": "711e89750e1b419e97f8847bc252a154",
    "coverStatus": "",
    "displayName": "",
    "pictureStatus": "",
    "statusMessage": "",
    "videoProfile": "{\"category\":\"vp.mp4\",\"extension\":\"jpeg\",\"animated\":false,\"width\":1080,\"height\":1080,\"fileSize\":272586,\"tids\":{\"mp4\":\"vp.small\",\"sjpg\":\"vp.sjpg\"}}"
  },
  "changeProfileVideo": {
    "picture": "tmp/pict.bin",
    "stage": 2,
    "status": False,
    "video": "/tmp/linepy-1562078161-8.bin"
  },
  "changeVideo": False,
  "Img": {},
  "clone": False,
  "like": False,
  "sukaPost": False,
  "groupPicture": False,
  "Hapuschat": False,
  "setKey": False,
  "autoRead": False,
  "changePicture": False,
  "stickerbig": False,
  "MentionSticker": False,
  "owner":{},
  "staff": {},
  "admin":{},
  "Timeline": False,
  "checkPost": False,
  "autoReject": False,
  "addadmin": False,
  "delladmin": False,
  "addstaff": False,
  "dellstaff": False,
  "autoBlock": False,
  "detectMention": True,
  "detectMention2": False,
  "arespon":True,
  "blacklist":{},
  "Talkblacklist":{},
  "jumlah": 5,
  "talkban": False,
  "checkSticker": False,
  "autoJoinTicket": True,
  "autoJoin": True,
  "autoAdd": True,
  "autoLeave": False,
  "limitkick": False,
  "contact": False,
  "autoJoinMessage": "ᴛᴇʀɪᴍᴀᴋᴀsɪʜ ᴋᴀᴋᴀ ᴀᴛᴀs ᴜɴᴅᴀɴɢᴀɴ ɢʀᴜᴘɴʏᴀ.",
  "comment": "ᴀᴜᴛᴏ ʟɪᴋᴇ ɴ ᴄᴏᴍᴍᴇɴᴛ ᴅᴏɴᴇ\nвʏ.ᴛᴇᴀᴍ ⊶ [B.O.G] ⊷",
  "comment2": "┏━━━━━━━━━•❅•°•❈•°•❅•━━━━━━━━┓\n┃┏━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┓\n┃┃     ❀    [ BLACK_OF_GAMER ]    ❀\n┃┗━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┛\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃┏━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┓\n┃┃          LIKE N COMMENT DONE\n┃┃         IKUTAN CORET-CORET\n┃┃                     B.O.G_TEAM\n┃┗━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┛\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃┏━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┓\n┃┃  AciL :\n┃┃  http://line.me/ti/p/~adiputra.95\n┃┃  Denjaka :\n┃┃  http://line.me/ti/p/~denjaka_inex\n┃┗━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┛\n┗━━━━━━━━━•❅•°•❈•°•❅•━━━━━━━━┛",
  "mention":"ᴋᴀʟᴏ ɴɢɪɴᴛɪᴘ ᴛᴇʀᴜs ᴅᴀᴘᴇᴛ ɢᴇʟᴀs ᴘᴇᴄᴀʜ ᴅɪ ᴋᴇᴘᴀʟᴀ...",
  "Respontag":"https://youtube.com/channel/UCu5Aqj6zqJK59pXxNGw8HMg",
  "Respontag2":"ada apa tag saya d grup kak?",
  "tagpm":"subcrabe channelku donk kak\nhttps://youtube.com/channel/UCu5Aqj6zqJK59pXxNGw8HMg",
  "welcome":"ѕєĻαмαт đαтαηg,,,, вυđαуαкαη ¢єк ησтє кαк",
  "message":"тᴇяıмᴀ кᴀsıн suᴅᴀн ᴀᴅᴅ sᴀʏᴀ \nвʏ.ᴛᴇᴀᴍ \n⊶ вĻα¢к●σƒ●gαмєя ⊷",
  "baper":"ѕєĻαмαт тιηggαĻ тємαη,,, ѕємσgα єηgкαυ тєηαηg đι ѕαηα●",
  "userAgent": [
    "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
    "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
    "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
    "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
  ]
}
cctv = {
  "cyduk":{},
  "point":{},
  "sidermem":{}
}
try:
  with open("unsend.json","r",encoding="utf_8_sig") as f:
    msg_dict = json.loads(f.read())
except:
  print("unsend eror")
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
jamtgl = timeNow.strftime('|📆|%d/%B/%Y|⏰|%X|')
jam = timeNow.strftime('⏰ %X')
tgl = timeNow.strftime('📆 %d/%B/%Y')
def runtime(secs):
  mins, secs = divmod(secs,60)
  hours, mins = divmod(mins,60)
  days, hours = divmod(hours, 24)
  return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def backupData():
  try:
    backup = LoginBot
    f = codecs.open('unsend.json','w','utf-8')
    json.dump(backup,f, sort_keys=True, indent=4, ensure_ascii=False)
    return True
  except Exception as error:
    print(error)
    return False
def Run_Xx():
  backupData()
  python = sys.executable
  os.execl(python, python, *sys.argv)
def logError(text):
  me.log("ERROR 404 !\n" + str(text))
  tz = pytz.timezone("Asia/Jakarta")
  timeNow = datetime.now(tz=tz)
  timeHours = datetime.strftime(timeNow,"(%H:%M)")
  day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
  hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
  bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
  inihari = datetime.now(tz=tz)
  hr = inihari.strftime('%A')
  bln = inihari.strftime('%m')
  for i in range(len(day)):
    if hr == day[i]: hasil = hari[i]
  for k in range(0, len(bulan)):
    if bln == str(k): bln = bulan[k-1]
  time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
  with open("errorLog.txt","a") as error:
    error.write("\n[%s] %s" % (str(time), text))
def mentionMembers(to, mid):
  try:
    arrData = ""
    textx = "╭━──────────────━╮\n│➢Total「{}」Members\n╰━──────────────━╯\n╭━──────────────━╮\n│➢ 1. ".format(str(len(mid)))
    arr = []
    no = 1
    num = 2
    for i in mid:
      mention = "@x\n"
      slen = str(len(textx))
      elen = str(len(textx) + len(mention) - 1)
      arrData = {'S':slen, 'E':elen, 'M':i}
      arr.append(arrData)
      textx += mention
      if no < len(mid):
        no += 1
        textx += "│➢ %i. " % (num)
        num=(num+1)
      else:
        try:
          no = "\n╚══[ {} ]".format(str(me.getGroup(to).name))
        except:
          no = "\n╚══[ Success ]"
    me.sendMessage(to, textx+"╰━──────────────━╯", {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  except Exception as error:
    logError(error)
    me.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def changeProfileVideo(to):
  if set['changeProfileVideo']['picture'] == None:
    return me.sendMessage(to, "Foto tidak ditemukan")
  elif set['changeProfileVideo']['video'] == None:
    return me.sendMessage(to, "Video tidak ditemukan")
  else:
    path = set['changeProfileVideo']['video']
    files = {'file': open(path, 'rb')}
    obs_params = me.genOBSParams({'oid': me.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
    data = {'params': obs_params}
    r_vp = me.server.postContent('{}/talk/vp/upload.nhn'.format(str(me.server.LINE_OBS_DOMAIN)), data=data, files=files)
    if r_vp.status_code != 201:
      return me.sendMessage(to, "Gagal update profile")
    path_p = set['changeProfileVideo']['picture']
    set['changeProfileVideo']['status'] = False
    me.updateProfilePicture(path_p, 'vp')
def sendTemplate(to, text):
  data = { "type": "flex","altText": " Black Of Gamers","contents":
  {"type": "bubble","size": "micro",
  "styles":{"body":{"backgroundColor":"#000000"}},"type":"bubble",
  "body": {"cornerRadius": "md","borderWidth": "5px","borderColor": biruTua,
  "contents":[{"contents":[{"type":"separator","color":warnanya1},{"contents":[
  {"type":"separator","color":warnanya1},
  {"text": text ,"size":"xxs","align":"center","color": warnanya1,"wrap":True,"weight":"bold","type":"text"},
  {"type":"separator","color":warnanya1}
  ],"type":"box","spacing":"md","layout":"horizontal"},
  {"type":"separator","color":warnanya1}
  ],"type":"box","layout":"vertical"},
  ],"type":"box","layout":"vertical"}},}
  me.sendFlex(to, data)
def sendTemplate2 (to,text):
  data = { "type": "flex","altText": " Assalamu'alaikumm","contents":
  {"type": "bubble","styles": style_biru,"type":"bubble","size":"kilo","body":
  {"cornerRadius": "md","borderWidth": "5px","borderColor": biruTua,"contents":[{"contents":[{"type":"separator","color":"#ffffff"},
  {"contents":[sp_putih,
  {"text":"вĻα¢к●σƒ●gαмєя","size":"md","align":"center","color":"#BE1700","wrap":True,"weight":"bold","type":"text"},
  sp_putih
  ],"type":"box","spacing":"md","layout":"horizontal"},
  sp_putih],"type":"box","layout":"vertical"},
  {"contents":[sp_putih,
  {"contents":[sp_putih,
  {"type": "image","url": "https://1.bp.blogspot.com/-6T7oMDOIlKA/XVX_8-oO52I/AAAAAAAAGe0/W0MubSIIyUUzw3et2YifTWqxaNRRwWE-ACLcBGAs/s1600/20190816_075636.png","size": "full","aspectRatio": "3:1"},
  sp_putih
  ],"type":"box","spacing":"md","layout":"horizontal"},
  sp_putih],"type":"box","layout":"vertical"},
  {"contents": [sp_putih,
  {"contents":[sp_putih,
  {"text": text,"size":"xs","color":kuning,"wrap":True,"weight":"bold","type":"text"},
  sp_putih],"type":"box","spacing":"md","layout":"horizontal"},
  sp_putih],"type":"box","layout":"vertical"},
  ],"type":"box","spacing":"xs","layout":"vertical"}},}
  me.sendFlex(to, data)
def Fotter(to,text):
  data = {"type": "text","text": text,"sentBy": {"label": "вĻα¢к ● σƒ ● gαмєя","iconUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSi2LaC4ftZz21mtSDA3YkylLb6lgqncx_uxOp-wdyAlIqsVsJ1","linkUrl": "http://line.me/ti/p/~denjaka_inex"}}
  me.sendFlex(to,data)
def RunTheRun(to, mid, firstmessage):
  try:
    arrData = ""
    text = "%s " %(str(firstmessage))
    arr = []
    mention = "@x \n"
    slen = str(len(text))
    elen = str(len(text) + len(mention) - 1)
    arrData = {'S':slen, 'E':elen, 'M':mid}
    arr.append(arrData)
    today = datetime.today()
    future = datetime(2018,7,25)
    hari = (str(future - today))
    comma = hari.find(",")
    hari = hari[:comma]
    teman = me.getAllContactIds()
    gid = me.getGroupIdsJoined()
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    eltime = time.time() - mulai
    bot = runtime(eltime)
    h = me.getContact(meM)
    me.reissueUserTicket()
    My_Id = "http://line.me/ti/p/"+me.getUserTicket().id
    text += mention+"WAKTU :\n"+jamtgl+"\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND : "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nINEX_TEAM. ʟɪɴᴇ ᴠᴇʀ.8.14.2\nRUN : "+bot+"\n\nMY TOKEN :\n"+str(me.authToken)+"\n\nMY MID : \n"+h.mid+"\nMY ID LINE : "+My_Id+"\n\nCHANEL YOUTUBE\n"+set["Respontag"]
    me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  except Exception as error:
    print("Error :\n" + str(error))
def Comt(text):
  pesan = text.lower()
  if pesan.startswith(set["keyCommand"]):
    Pbot = pesan.replace(set["keyCommand"],"")
  else:
    Pbot = "command"
  return Pbot
def bot(op):
  opp1 = op.param1
  opp2 = op.param2
  opp3 = op.param3
  try:
    if op.type is None:
      pass
    else:
      if op.type == 0:
        pass
      else :
        print("[ {} ] {}".format(str(op.type), OpType._VALUES_TO_NAMES[op.type]))
    if op.type == 13:
      if meM in opp3:
        if set["autoJoin"] == True:
          me.acceptGroupInvitation(opp1)
          wr = me.getGroup(opp1)
          ban = [contact.mid for contact in wr.members]
          for x in ban:
            if x in set["blacklist"]:
              try:
                me.kickoutFromGroup(opp1,[x])
              except:pass
            print("blacklist kick ok")
    if op.type in [19,32,17,13]:
      if opp3 in set["PASUKAN"]:
        if opp2 in meM and opp2 in set["PASUKAN"]:
          pass
        else:
          Nam = me.getContact(opp2).displayName
          set["blacklist"][opp2] = True
          try:
            sendTemplate(opp1,Nam+"\nBanlist true")
          except:
            try:
              sendTemplate(opp1,Nam+"\nBanlist true")
            except:pass
  except Exception as X:
    print(X)
while True:
  try:
    ops = oepoll.singleTrace(count=50)
    if ops is not None:
      for op in ops:
        oepoll.setRevision(op.revision)
        thread = threading.Thread(target=bot, args=(op,))
        thread.start()
  except Exception as e:
    print(e)
