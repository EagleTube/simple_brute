import cloudscraper, sys, os, colorama, time, ctypes, datetime, sys, platform, threading
from urllib.parse import urlparse
from colorama import Fore, Back, Style
from datetime import date
from time import gmtime, strftime

today = date.today()
d2 = today.strftime("%B %d, %Y")

if platform.system()=='Linux':
    os.system('clear')
    sys.stdout.write("\x1b]2;SPAM-PHISHING MAIL DFM {}\x07".format(d2))
else:
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'SPAM-PHISHING MAIL DFM | {d2}')

print(f"""{Style.BRIGHT + Fore.RED}
 ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
 ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
 ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
 ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
 ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 
                                                                                                             
{Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
{Style.BRIGHT + Fore.YELLOW}  
                                                 Coded by Eagle Eye
                                              Web Directory Bruteforcer
                                    https://dragonforce.io | Telegram: dragonforceio
                                   Get Started With (pip install -r requirements.txt)                                                                                            

{Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")
def helpdesk():
    print(Style.BRIGHT+Fore.WHITE+"Usage : python dirbrute.py -u http://example.com/ -w wordlist.txt")

def checkUrl(url):
    web_arr = urlparse(url)
    if(web_arr.scheme=="" and web_arr.path==url):
        return "http://" + url + "/"
    elif(web_arr.path=="/"):
        return url
    else:
        return url + "/"

def loadTxt(word):
    try:
        f = open(word,'r')
        return f.readlines()
    except FileNotFoundError:
        print(Style.BRIGHT+Fore.RED+"File you request doesn't exist!")

def connectURL(url):
    scraper = cloudscraper.create_scraper(
    browser = {
        'browser' : 'chrome',
        'platform' : 'darwin',
        'mobile': False
    }
)
    try:
        try:
            conn = scraper.get(url,timeout=3)
            if(conn.status_code>=200 and conn.status_code<=299):
                print(Style.BRIGHT+Fore.GREEN+"{} -> {}".format(conn.status_code,url))
            elif(conn.status_code>=400 and conn.status_code<=499):
                print(Style.BRIGHT+Fore.BLUE+"{} -> {}".format(conn.status_code,url))
            elif(conn.status_code>=100 and conn.status_code<=199):
                print(Style.BRIGHT+Fore.WHITE+"{} -> {}".format(conn.status_code,url))
            elif(conn.status_code>=300 and conn.status_code<=399):
                print(Style.BRIGHT+Fore.YELLOW+"{} -> {}".format(conn.status_code,url))
            else:
                print(Style.BRIGHT+Fore.RED+"{} -> {}".format(conn.status_code,url))
        except KeyboardInterrupt:
            print(Style.BRIGHT+Fore.YELLOW+"Process stopped!")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
    except:
        print(Style.BRIGHT+Fore.RED+"No connection! -> {}".format(url))
        sys.exit(0)

def startX(url,word):
    load = loadTxt(word)
    for line in load:
        fullURL = url+line.replace("\n","")
        connectURL(fullURL)

def position(arr,types):
    if(types=="-u" or types=="-w"):
        return arr.index(types) + 1
    else:
        print(Style.BRIGHT+Fore.WHITE+"No such option for {}".format(types))

def main():
    start = time.perf_counter()

    url = sys.argv[position(sys.argv,'-u')]
    word = sys.argv[position(sys.argv,'-w')]
    startX(url,word)

if __name__ == '__main__':
    main()
