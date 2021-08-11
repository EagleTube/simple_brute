import requests
import json
import sys
from urllib.parse import urlparse

def reqURL(target,path):
    url = target + path
    payload = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    # Adding empty header as parameters are being sent in payload
    headers = {}
    r = requests.get(url, data=json.dumps(payload), headers=headers)
    return (r.status_code)


def cleanURL(target):
    urlArr = urlparse(target)
    if(urlArr.path==target and urlArr.scheme==""):
        return "http://" + target + "/"
    elif(urlArr.path==""):
        return target + "/"
    else:
        return target

def checkArgv(x):
    if(x.lower()=="-w" or x.lower()=="--wordlist"):
        return True
    else:
        return False

if(len(sys.argv)>4):
    print("Unknown command {}".format(sys.argv[4]))
else:
    if checkArgv(sys.argv[2]):
        try:
            words = open(sys.argv[3],"r")
            lines = words.readlines()
            target = cleanURL(sys.argv[1])
            for line in lines:
                if(reqURL(target,line.strip())==200):
                    print("Found : {}".format(target+line.strip()))
                elif(reqURL(target,line.strip())==403):
                    print("Forbidden : {}".format(target+line.strip()))
                elif(reqURL(target,line.strip())==404):
                    print("Not Found : {}".format(target+line.strip()))
                elif(reqURL(target,line.strip())==400):
                    print("Bad Request : {}".format(target+line.strip()))
                elif(reqURL(target,line.strip())>=500 and reqURL(target,line.strip())<=599):
                    print("Internal Error : {}".format(target+line.strip()))
                elif(reqURL(target,line.strip())>=300 and reqURL(target,line.strip())<=399):
                    print("Redirected : {}".format(target+line.strip()))
                else:
                    print("Unknown : {}".format(target+line.strip()))

        except:
            print("ERROR : Wordlist may be too large or Wordlist not existen!")
    else:
        print("Unknown command '{}' , -h/--help for Help ".format(sys.argv[2]))

