import os
try:
    import ipinfo,pprint
    from configparser import ConfigParser
    import sys
    import time
    from prettytable import PrettyTable
    import platform
    import random
except:
    os.system("pip install ipinfo")
    os.system("pip install configparser")
    os.system("pip install prettytable")
    os.system("pip install goto-statement")


#Dah mamae nmechoka
conf = ConfigParser()
x = PrettyTable()

color = ['\x1b[38;5;118m','\x1b[38;5;33m','\033[0;35m','\033[0;36m','\033[0;32m','\033[0;35m''\e[0;95m','\e[35m','\033[1;33m']
 
pixer = random.choice(color)    

x.field_names = ['NAME','DATA']

conf.read("vitu/config.ini")

def safisha():
    if platform == 'win32':
        os.system("cls")
    else:
        os.system("clear")

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
        x.add_row(["City",f"{details.city}"])
        x.add_row(["Country",f"{details.country}"])
        x.add_row(["Country Name",f"{details.country_name}"])
        x.add_row(["Postal",f"{details.postal}"])
        x.add_row(["Org",f"{details.org}"])
        x.add_row(["IP",f"{details.ip}"])
        x.add_row(["Location",f"{details.loc}"])
        x.add_row(["Region",f"{details.region}"])
        x.add_row(["TimeZone",f"{details.timezone}"])
        x.add_row(["Latitude",f"{details.latitude}"])
        x.add_row(["Longitude",f"{details.longitude}"])
        print(x)
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

