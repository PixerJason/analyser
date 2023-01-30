import os
try:
    import ipinfo,pprint
    from configparser import ConfigParser
    import sys
    import time
    import paltform
    from prettytable import PrettyTable
    import random
except:
    os.system("pip install ipinfo")
    os.system("pip install configparser")
    os.system("pip install prettytable")
    os.system("pip install goto-statement")


#Dah mamae nmechoka
conf = ConfigParser()
ghostcracker = PrettyTable()

color = ['\x1b[38;5;118m','\x1b[38;5;33m','\033[0;35m','\033[0;36m','\033[0;32m','\033[0;35m''\e[0;95m','\e[35m','\033[1;33m']
 
pixer = random.choice(color)    

def safisha():
    if platform == 'win32:
        os.system('cls')
    else:
        os.system('clear')


ghostcracker.field_names = ["city","country","country_name","postal","org","ip","loc","region","timezone","latitude","longitude"]

conf.read("vitu/config.ini")

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.1)

def banner():
    print(f"""{pixer}
 █████  ███    ██  █████  ██      ██    ██ ███████ ███████ ██████  
██   ██ ████   ██ ██   ██ ██       ██  ██  ██      ██      ██   ██ 
███████ ██ ██  ██ ███████ ██        ████   ███████ █████   ██████  
██   ██ ██  ██ ██ ██   ██ ██         ██         ██ ██      ██   ██ 
██   ██ ██   ████ ██   ██ ███████    ██    ███████ ███████ ██   ██     
    
    """)
def fucktoken():
    ing = input("Enter The fuckn Token: ")
    bibi = open("vitu/config.ini",'w')
    mbuzi = f'[TOKEN]\naccess_token = {ing}'
    bibi.write(mbuzi)
    bibi.close()

def ass(num):
    try: 
        handler = ipinfo.getHandler(conf.get("TOKEN","access_token"))
        details = handler.getDetails(num)
        ghostcracker.add_row([f"{details.city}",f"{details.country}",f"{details.country_name}",f"{details.postal}",f"{details.org}",f"{details.ip}",f"{details.loc}",f"{details.region}",f"{details.timezone}",f"{details.latitude}",f"{details.longitude}"])
        print(ghostcracker)
        typing("Telegram: https://t.me/PixerJason")
    except:
        fucktoken()

def main():
    try:
      safisha()
      typing("\t\t\t0\t\tCoded By Pixer Jason!")
      banner()
      num = input("Enter The Fuckn IP: ")
      ass(num)
    except KeyboardInterrupt:
        typing("\nGoodbye!")      

if __name__ == '__main__':
    main()        

