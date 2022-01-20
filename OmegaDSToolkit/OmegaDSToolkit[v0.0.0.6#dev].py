#---[Metadata]-----------------------------------------------------#
#  Filename ~ OmegaDSToolkit[v0.0.0.6#dev]    [Update: 11-01-2022] #
#---[Info]---------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}#
#                                                                  #
#  OmegaDSTookit ~ A massive penetration testing toolkit           #
#  Language      ~ Python3                                         #
#---[Author]-------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                  #
#---[Operating System]---------------------------------------------#
#  Developed for linux                                             #
#  Compatible with Windows 10 (for the moment)                     #
#---[Licence]------------------------------------------------------#
#  GNU General Public License v3.0                                 #
#------------------------------------------------------------------#





version = "v0.0.0.6"

from time import sleep

def cls():                                                  # check if the user use windows or linux for the "clear" or "cls" function
    os.system('cls' if os.name=='nt' else 'clear')          #

#-Check module is installed------------------------------------------#
def checkmodules():
    cls()
    import sys
    sys.stdout.write("\x1b]2;Checking if all modules are [OK]\x07")

    print("Checking if the current modules of ODST are installed...")
    print()
    sleep(1)

# for time
    try:
        import time
        print("[OK]     Time is installed")
    except ImportError:
        print("     [ERROR]     Time isn't installed")
        print("     [ERROR]     Time module note detected, run the setup.py to install it.")

# for progress
    try:
        import progress
        print("[OK]     Progress is installed")
    except ImportError:
        print("     [ERROR]     Progress isn't installed")
        print("     [ERROR]     Progress module not detected, run the setup.py to install it")

# for colored
    try:
        import colored
        print("[OK]     Colored is installed")
    except ImportError:
        print("     [ERROR]     Colored isn't installed")
        print("     [ERROR]     Colored module not detected, run the setup.py to install it")

# for nslookup
    try:
        import nslookup
        print("[OK]     NSLookup is installed")
    except ImportError:
        print("     [ERROR]     Nslookup isn't installed")
        print("     [ERROR]     Nslookup module not detected, run the setup.py to install it")

# for keyboard
    try:
        import keyboard
        print("[OK]     Keyboard is installed")
    except ImportError:
        print("     [ERROR]     Keyboard isn't installed")
        print("     [ERROR]     Keyboard module not detected, run the setup.py to install it")
        exit()

# for pythonping
    try:
        import pythonping
        print("[OK]     Pythonping is installed")
    except ImportError:
        print("     [ERROR]     Pythonping isn't installed")
        print("     [ERROR]     Pythonping module not detected, run the setup.py to install it")
        exit()

    sleep(1.5)
#-END-OF-MODULES-CHECKER---------------------------------------------#

#-Import section-----------------------------------------------------#
import ctypes, urllib.request, os, shutil

from progress.bar import Bar
from colored import fg, attr                        # fg = la couleur de départ // attr = la fin de la couleur, pour pas que tout le texte qui suit sera en couleur
from pythonping import ping                        #   https://www.ictshore.com/python/python-ping-tutorial/
#-END-OF-IMPORT-SECTION----------------------------------------------#

#-Colors section-----------------------------------------------------#

# Les bleus
bC = fg('#1d89f3')      # bleu
bC2 = fg('#0B4D8F')     # bleu (foncé)

# Les rouges
rC = fg('#F44336')      # rouge
rC2 = fg('#ec5a0d')     # orange (orange claire)

# Les verts
gC = fg('#39CC3F')      # vert

# Les jaunes
yC = fg('#EDFF00')



r = attr('reset') # pour terminer le formatage de la couleur
#--------------------------------------------------------------------#

#-Fonctions----------------------------------------------------------#

#########################################################
def connection(host='http://google.com'):               #
    global connectionstatus                             #
    try:                                                #
        urllib.request.urlopen(host)                    #
        return True                                     #
    except:                                             #   Check if the user have an Internet connection 
        return False                                    #
if connection() == True:                                #
    connectionstatus = (gC+"Connected"+r)               #
else:                                                   #
    connectionstatus = (rC+"No Internet"+r)             #
#########################################################

### if the user doesn't choose option
def error():
    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Choose a option"+bC+"]"+r)
    input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)


### if the user enter a bad option (if the option type by the user are)
def invalid_option():
    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Invalid option"+bC+"]"+r)
    input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)

#--------------------------------------------------------------------#

### Wireless Atack | main page
def wireless_mainpage():
    cls()
    print(gC+"         ________ __              __                         __                __        "+r)
    print(gC+"        |  |  |  |__|.----.-----.|  |.-----.-----.-----.    |  |_.-----.-----.|  |.-----."+r)
    print(gC+"        |  |  |  |  ||   _|  -__||  ||  -__|__ --|__ --|    |   _|  _  |  _  ||  ||__ --|"+r)
    print(gC+"        |________|__||__| |_____||__||_____|_____|_____|    |____|_____|_____||__||_____|"+r)
    print(bC+"     ╓────────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)




#--------------------------------------------------------------------#

### Information Gathering | main page ###
def informationgathering_mainpage():
    cls() 
    print(rC2+"      _______         ___                             __   __                    "+r)
    print(rC2+"     |_     _|.-----.'  _|.-----.----.--------.---.-.|  |_|__|.-----.-----.      "+r)
    print(rC2+"      _|   |_ |     |   _||  _  |   _|        |  _  ||   _|  ||  _  |     |      "+r)
    print(rC2+"     |_______||__|__|__|  |_____|__| |__|__|__|___._||____|__||_____|__|__|      "+r)
    print(bC+"   ◄════════════════════════════════════════════════════════════════════════►    "+r)
    print(rC2+"          _______         __   __                __ ")
    print(rC2+"         |     __|.---.-.|  |_|  |--.-----.----.|__|.-----.-----.                "+r)
    print(rC2+"         |    |  ||  _  ||   _|     |  -__|   _||  ||     |  _  |                "+r)
    print(rC2+"         |_______||___._||____|__|__|_____|__|  |__||__|__|___  |                "+r)
    print(bC+"       ╔═════════════════════════════════════════════════╗"+r+rC2+"|_____|        "+r)
    print(bC+"       ╚═════╗                                           ╚════════►               "+r)
    print(bC+"             ║"+r)
    print(bC+"             ║"+r+"   In this category you will find tools to collect information,")
    print(bC+"             ║"+r+"              such as port scan, SQL injections etc")
    print(bC+"             ║"+r)
    print(bC+"             ╟──── ["+r+gC+"  Made by   "+r+bC+"] ───"+r+gC+"► "+r+rC+"Thomas Pellissier"+r+bC2+" (© Delta_Society™)"+r)
    print(bC+"             ╟──── ["+r+gC+"  Codename  "+r+bC+"] ───"+r+gC+"► "+r+bC2+"@"+r+rC+"MyMeepSQL")
    print(bC+"             ╟──── ["+r+gC+"  Version   "+r+bC+"] ───"+r+gC+"► "+r+bC2+"v"+r+rC+"0.0.1"+r)
    print(bC+"             ║"+r)
    print(bC+"             ╟────"+r+gC+"► "+r+"["+bC+"1"+r+"]"+gC+"    Scan"+r)
    print(bC+"             ╟────"+r+gC+"► "+r+"["+bC+"2"+r+"]"+gC+"    "+r)
    print(bC+"             ╟────"+r+gC+"► "+r+"["+bC+"X"+r+"]"+gC+"    Return to the main page\n"+r)
     
    while True:
        try:
            print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Information Gathering"+r+bC+"]")
            infogathering_mainpage = str(input(bC+"└╼"+rC+"$ "+r))
            break
        except:
            error()
            cls()
            informationgathering_mainpage()

    if infogathering_mainpage == "1":
        scan_mainpage()
    elif infogathering_mainpage == "X":
        cls()
        main_page()
    elif infogathering_mainpage == "x":
        print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"For this page, the correct command is 'x' and not 'X' for return to the main page"+bC+"]"+r)
        input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
        informationgathering_mainpage()
    else:
        invalid_option()
        cls()
        informationgathering_mainpage()

### Information Gathering | Scan tools ### 
def scan_mainpage():
    cls()
    print(gC+"       _____             _____         _               "+r)
    print(gC+"      |   __|___ ___ ___|_   _|___ ___| |___           "+r)
    print(gC+"      |__   |  _| .'|   | | | | . | . | |_ -|          "+r)
    print(gC+"      |_____|___|__,|_|_| |_| |___|___|_|___|          "+r)
    print(bC+"     ╓────────────────────────────────────────"+gC+"►"+r)
    print(bC+"     ║"+r+"   Some tools for scanning target") 
    print(bC+"     ╙────╖")
    print(bC+"          ╟──────"+gC+"►"+r+bC2+" Created by :"+r+rC+"  Thomas Pellissier"+bC2+" (© Delta_Society™)"+r)
    print(bC+"          ╟──────"+gC+"►"+r+bC2+" Codename   :  @"+r+rC+"MyMeepSQL"+r)
    print(bC+"          ╟──────"+gC+"►"+r+bC2+" Version    :"+r+rC+"  0.0.1"+r)
    print(bC+"          ╙─────╖"+r)
    print(bC+"                ╟────"+gC+"► "+r+"["+bC+"1"+r+"]"+gC+"    Nmap"+r)
    print(bC+"                ╟────"+gC+"► "+r+"["+bC+"2"+r+"]"+gC+"    sqlmap"+r)
    print(bC+"                ╟────"+gC+"► "+r+"["+bC+"x"+r+"]"+gC+"    Return to the"+rC+" Information Gathering"+gC+" main page"+r)
    print(bC+"                ╟────"+gC+"► "+r+"["+bC+"X"+r+"]"+gC+"    Return to the"+rC+" OmegaDSToolkit"+gC+" main page\n"+r)

    while True:
        try:
            print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"ScanTools"+r+bC+"]")
            scan_mainpage_ = str(input(bC+"└╼"+rC+"$ "+r))
            break
        except:
            error()
            cls()
            scan_mainpage()
            
    # if scan_mainpage_ == 2:


    if scan_mainpage_ == "x":
        cls()
        informationgathering_mainpage()
    elif scan_mainpage_ == "X":
        cls()
        main_page()
    else:
        invalid_option()
        cls()
        scan_mainpage()
        
#--------------------------------------------------------------------#     



#--------------------------------------------------------------------#

### Usefull Windows tool | main page ###
def windowstools_mainpage():
    cls()
    print(rC2+"      _____ _ _ _ _____         _      "+r)
    print(rC2+"     |  |  | | | |_   _|___ ___| |___  "+r)
    print(rC2+"     |  |  | | | | | | | . | . | |_ -| "+r)
    print(rC2+"     |_____|_____| |_| |___|___|_|___| "+r)
    print(bC+"    ╔════════════════════════════════════"+r+gC+"►"+r)
    print(bC+"    ╚════╗")
    print(bC+"         ║"+r+"   UsefulWindowsTools include several  ")
    print(bC+"         ║"+r+"          useful windows tools")       
    print(bC+"         ║ ")
    print(bC+"         ╟──── ["+r+gC+"  Made by   "+r+bC+"] ───"+r+gC+"►"+r+rC+" Thomas Pellissier"+r+bC2+" (© Delta_Society™)"+r)
    print(bC+"         ╟──── ["+r+gC+"  Codename  "+r+bC+"] ───"+r+gC+"►"+r+bC2+" @"+r+rC+"MyMeepSQL")
    print(bC+"         ╟──── ["+r+gC+"  Version   "+r+bC+"] ───"+r+gC+"►"+r+bC2+" v"+r+rC+"0.0.1"+r)
    print(bC+"         ║ ")
    print(bC+"         ╚════╗   ")
    print(bC+"              ╟────"+r+r+gC+"► "+r+"["+bC+"1"+r+"]"+gC+"     Backup tool (for make backup quickly)"+r)
    print(bC+"              ╟────"+r+r+gC+"► "+r+"["+bC+"2"+r+"]"+gC+"     Network commands (ping, telnet etc)"+r)
    print(bC+"              ╟────"+r+r+gC+"► "+r+"["+bC+"x"+r+"]"+gC+"     Return to the main page\n"+r)

    while True:
        try:
            print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"UWTools"+r+bC+"]")
            windowsT_mainpage = str(input(bC+"└╼"+rC+"$ "+r))
            break
        except:
            error()
            cls()
            windowstools_mainpage()
    if windowsT_mainpage == "1":
        windowstools_backup()
    if windowsT_mainpage == "2":
        windowstools_networkC_main_page()
    elif windowsT_mainpage == "x":
        cls()
        main_page()
    elif windowsT_mainpage == "X":
        print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"For this page, the correct command is 'x' and not 'X' for return to the main page"+bC+"]"+r)
        input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
        windowstools_mainpage()
    else:
        invalid_option()
        cls()
        windowstools_mainpage()
        
### Usefull Windows tool  | Network commands ###
def windowstools_networkC_main_page():
    cls()
    print(rC2+"      _______         __                           __         ______                                              __        "+r)
    print(rC2+"     |    |  |.-----.|  |_ .--.--.--..-----..----.|  |--.    |      |.-----..--------..--------..---.-..-----..--|  |.-----."+r)
    print(rC2+"     |       ||  -__||   _||  |  |  ||  _  ||   _||    <     |   ---||  _  ||        ||        ||  _  ||     ||  _  ||__ --|"+r)
    print(rC2+"     |__|____||_____||____||________||_____||__|  |__|__|    |______||_____||__|__|__||__|__|__||___._||__|__||_____||_____|"+r)
    print(bC+"   ╓─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"+gC+"►"+r)
    print(bC+"   ╚═══╗"+r)
    print(bC+"       ║"+r+"    Some windows network commands  "+r)
    print(bC+"       ║"+r)
    print(bC+"       ╟──────"+gC+"►"+bC2+" Created by :"+rC+"  Thomas Pellissier"+bC2+" (© Delta_Society™)"+r)
    print(bC+"       ╟──────"+gC+"►"+bC2+" Codename   : @"+rC+"MyMeepSQL"+r)
    print(bC+"       ╟──────"+gC+"►"+bC2+" Version    :"+rC+"  0.0.1"+r)
    print(bC+"       ║"+r)
    print(bC+"       ╙──────"+gC+"►"+r+" Type -h, --help for all commands\n")
  
    print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands"+r+bC+"]")
    networkC_main_page = str(input(bC+"└╼"+rC+"$ "+r))
    
    if networkC_main_page == "-h" or networkC_main_page == "--help":
        print()
        print("===========================================================================")
        print("Optional arguments:")
        print("        -h, --help                                 show this help message")
        print()
        print(gC+"Network commands"+r)
        print("        nslookup                                   nslookup for DNS domain")
        print("===========================================================================")
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands | Nslookup"+r+bC+"]")
        domain = str(input(bC+"└╼"+rC+"$ "+r))
    elif networkC_main_page == "nslookup":
        print("""==============================================================================
    Type your domain for scan it (type exit for return to the main prompt)
==============================================================================""")
        
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands | Nslookup"+r+bC+"]")
        domain = str(input(bC+"└╼"+rC+"$ "+r))
        if not domain:
            print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands | Nslookup"+r+bC+"]")
            domain = str(input(bC+"└╼"+rC+"$ "+r))
        else:
            try:
                from nslookup import Nslookup
                dns_query = Nslookup(dns_servers=["1.1.1.1"])               # set optional Cloudflare public DNS server
                
                ips_record = dns_query.dns_lookup(domain)
                print(ips_record.response_full, ips_record.answer)
                
                soa_record = dns_query.soa_lookup(domain)
                print(soa_record.response_full, soa_record.answer)
            except:
                print()
                print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands | Nslookup"+r+bC+"]")
                domain = str(input(bC+"└╼"+rC+"$ "+r))
    elif networkC_main_page == "ping":
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands | Ping"+r+bC+"]")
        IP = str(input(bC+"└╼"+rC+"$ "+r))

        while not IP: 
            print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands | Ping"+r+bC+"]")
            IP = str(input(bC+"└╼"+rC+"$ "+r))
            if IP == True:
                try:
                    ping(IP)
                except RuntimeError:
                    print(f"{IP} not found, please ckeck the IP before ping it")
            else:
                print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+f"No IP found, write an IP to ping it"+bC+"]\n"+r)
    while not networkC_main_page:
        print()
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands"+r+bC+"]")
        networkC_main_page = str(input(bC+"└╼"+rC+"$ "+r))
    else:
        print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+f"Command '{networkC_main_page}' not found"+bC+"]\n"+r)
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands"+r+bC+"]")
        networkC_main_page = str(input(bC+"└╼"+rC+"$ "+r))

### Usefull Windows tool  | Backup tool ###
def windowstools_backup_error():                                                                    #
    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Chose y or n"+bC+"]"+r)                         # the function for the error with no respond
    input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)        #

def windowstools_backup():
    cls()
    print(rC2+"      _______                              ______              __                  "+r)
    print(rC2+"     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
    print(rC2+"     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
    print(rC2+"     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
    print(rC2+"                             |_____|                                      |__|     "+r)
    print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+gC+"►"+r)
    print(bC+"     ╚════════╗"+r)
    print(bC+"              ║"+r+"    A tool for make backup by file or "+r)
    print(bC+"              ║"+r+"          folder with robocopy"+r)
    print(bC+"              ║"+"") 
    print(bC+"              ╟──────"+gC+"►"+bC2+" Created by :"+rC+"  Thomas Pellissier"+bC2+" (© Delta_Society™)"+r)
    print(bC+"              ╟──────"+gC+"►"+bC2+" Version    :"+rC+"  0.0.2"+r)
    print(bC+"              ╟──────"+gC+"►"+bC2+" Codename   : @"+rC+"MyMeepSQL"+r)
    print(bC+"     ╔════════╝"+r)
    print(bC+"     ╚═══════════════════════════════════════════╗"+r)
    print("            Do you want make backup (y/n)"+bC+"        ║"+r)
    print(bC+"     ════════════════════════════════════════════╝"+r)
    print()
    print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
    choiceB = str(input(bC+"└╼"+rC+"$ "+r))
    
    if choiceB == "y":
        windowstools_backup_config()
    elif choiceB == "n":
        windowstools_mainpage()
    else:
        windowstools_backup_error()
        windowstools_backup()

def windowstools_backup_config():
        cls()
        print(rC2+"        _______                              ______              __                  "+r)
        print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
        print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
        print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
        print(rC2+"                               |_____|                                      |__|     "+r)
        print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
        print(bC+"     ╚═══════════════════════════════════════════╗"+r)
        print(gC+"       Whish folder or file you want backup it ?"+bC+" ║"+r)
        print(rC+"           /!\ "+gC+"Type the folder/file path"+rC+" /!\ "+bC+"    ║"+r)
        print(bC+"     ════════════════════════════════════════════╝"+r)
        print()
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
        source = str(input(bC+"└╼"+rC+"$ "+r))
        if not source:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Type your source folder/file "+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
            windowstools_backup_config()
            
        cls()        
        print(rC2+"        _______                              ______              __                  "+r)
        print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
        print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
        print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
        print(rC2+"                               |_____|                                      |__|     "+r)
        print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
        print(bC+"     ╚═══════════════════════════════════════════╗"+r)
        print(gC+"             Where you want to backup it ?"+bC+"       ║"+r)
        print(rC+"              /!\ "+gC+"Type the target path"+rC+" /!\ "+bC+"      ║"+r)
        print(bC+"     ════════════════════════════════════════════╝"+r)
        print()
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
        target = str(input(bC+"└╼"+rC+"$ "+r))
        
        while not target:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Type your target folder/file"+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
            cls()        
            print(rC2+"        _______                              ______              __                  "+r)
            print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
            print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
            print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
            print(rC2+"                               |_____|                                      |__|     "+r)
            print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
            print(bC+"     ╚═══════════════════════════════════════════╗"+r)
            print(gC+"             Where you want to backup it ?"+bC+"       ║"+r)
            print(rC+"              /!\ "+gC+"Type the target path"+rC+" /!\ "+bC+"     ║"+r)
            print(bC+"     ════════════════════════════════════════════╝"+r)
            print()
            print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
            target = str(input(bC+"└╼"+rC+"$ "+r))
    
        cls()
        print(rC2+"        _______                              ______              __                  "+r)
        print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
        print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
        print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
        print(rC2+"                               |_____|                                      |__|     "+r)
        print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
        print(bC+"     ╚═══════════════════════════════════════════╗"+r)
        print(gC+"          Are you sure you want backup (y/n)"+bC+"     ║"+r)
        print(bC+"     ╔═══════════════════════════════════════════╝"+r)
        print(bC+"     ╚════╗"+r)
        print(bC+"          ╟──────"+gC+"►"+rC+" Source"+bC+" ="+gC+">"+r+f" {source}")
        print(bC+"          ╚──────"+gC+"►"+rC+" Target"+bC+" ="+gC+">"+r+f" {target}")
        print()
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
        sure = str(input(bC+"└╼"+rC+"$ "+r))

        while not sure:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Chose y or n"+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
            cls()
            print(rC2+"        _______                              ______              __                  "+r)
            print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
            print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
            print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
            print(rC2+"                               |_____|                                      |__|     "+r)
            print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
            print(bC+"     ╚═══════════════════════════════════════════╗"+r)
            print(gC+"          Are you sure you want backup (y/n)"+bC+"     ║"+r)
            print(bC+"     ╔═══════════════════════════════════════════╝"+r)
            print(bC+"     ╚════╗"+r)
            print(bC+"          ╟──────"+gC+"►"+rC+" Source"+bC+" ="+gC+">"+r+f" {source}")
            print(bC+"          ╚──────"+gC+"►"+rC+" Target"+bC+" ="+gC+">"+r+f" {target}")
            print()
            print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
            sure = str(input(bC+"└╼"+rC+"$ "+r))
            if sure == "y":
                try:
                    print(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Backuping..."+bC+"]"+r)
                    shutil.copy(source, target)
                    print(bC+"["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Folder/file copied successfully"+bC+"]"+r)
                except shutil.SameFileError:
                    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Source and destination represents the same file."+bC+"]"+r)
                    
                    windowstools_backup_config()
                except PermissionError:
                    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Permission denied"+bC+"]"+r)
                    print(bC+"["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Please check your permissions with your folder/users"+bC+"]"+r)
                    print(bC+"["+r+rC2+"*"+r+bC+"]"+r+bC+"──["+r+gC+"If you want remake the backup config, type y else type n"+bC+"]\n"+r)
                    print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
                    permerror = str(input(bC+"└╼"+rC+"$ "+r))
                    if permerror == "y":
                        windowstools_backup_config()
                    if permerror == "n":
                        print()
                        print(bC+"["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Exiting backup tool..."+bC+"]"+r)
                        sleep(2.5)
                        windowstools_mainpage()
                                    
                    
                except:
                    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Error occurred while copying file"+bC+"]"+r)
                    
                print(bC+"["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Backup finish !"+bC+"]"+r)
                print(bC+"["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Check if the folder's copy it's all good, else remake the config"+bC+"]"+r)
                input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
            elif sure == "n":
                cls()
                print(rC2+"        _______                              ______              __                  "+r)
                print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
                print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
                print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
                print(rC2+"                               |_____|                                      |__|     "+r)
                print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
                print(bC+"     ╚════════════════════════════════════════════════════╗"+r)
                print(gC+"          Do you want reconfig the backup config ? (y/n)"+bC+"       ║"+r)
                print(bC+"     ═════════════════════════════════════════════════════╝"+r)
                print()
                print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
                choice2 = str(input(bC+"└╼"+rC+"$ "+r))
                while not choice2:
                    print(rC2+"        _______                              ______              __                  "+r)
                    print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
                    print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
                    print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
                    print(rC2+"                               |_____|                                      |__|     "+r)
                    print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
                    print(bC+"     ╚════════════════════════════════════════════════════╗"+r)
                    print(gC+"          Do you want reconfig the backup config ? (y/n)"+bC+"       ║"+r)
                    print(bC+"     ═════════════════════════════════════════════════════╝"+r)
                    print()                 
                    print(bC+"┌─("+rC+"OmegaDSToolkit"+bC+")-["+yC+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
                    choice2 = str(input(bC+"└╼"+rC+"$ "+r))
                    
                if choice2 == "y":
                    input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
                    windowstools_backup_config()
                elif choice2 == "n":
                    print()
                    print(bC+"["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Exiting backup tool..."+bC+"]"+r)
                    sleep(2.5)
                    windowstools_mainpage()
#-END-OF-BACKUP-TOOL-------------------------------------------------#



#-Main page----------------------------------------------------------#
# def print_time_date():                                                    #
#     import time                                                           #
#     from time import strftime                                             #
#     while True:                                                           #   Try to make a digital clock direcly in the main page
#         print(strftime("%a, %b %d, %Y | "), end="", flush=True)           #   Look under the last phrase at the "##????##"
#         print(strftime("%H:%M:%S"), end="", flush=True)                   #
#         print("\r", end="", flush=True)                                   #
#         time.sleep(1)                                                     #

def main_page():
    cls()
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+gC+"       _____                   ____  _____ _____         _ _   _ _"  +r)                                 # Police = rectangle
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+gC+"      |     |_____ ___ ___ ___|    \|   __|_   _|___ ___| | |_|_| |_"  +r)                               #
    print(bC+"        MMMMMMMMMMMMMMMMMNmmmmNNMMMMMMMMMMMMMMMM "+r+gC+"      |  |  |     | -_| . | .'|  |  |__   | | | | . | . | | '_| |  _|"  +r)                              #
    print(bC+"        MMMMMMMMMMMdy+:.```..```.-/shNMMMMMMMMMM "+r+gC+f"      |_____|_|_|_|___|_  |__,|____/|_____| |_| |___|___|_|_,_|_|_| "+r)                                #
    print(bC+"        MMMMMMMNy/``  -ohmNNNNNdy/`  `:smMMMMMMM "+r+gC+"                      |___|"+rC+f"                                          {version}"+r)                #
    print(bC+"        MMMMMNo.    :dNMMMMMMMMMMMNo`   `/dMMMMM "+r+bC+" ╓──────────────────────────────────────────────────────────────────────────"+gC+"►"  +r)
    print(bC+"        MMMMh.     sMMMMMMMMMMMMMMMMd.    `+NMMM "+r+bC+" ║"  +r)
    print(bC+"        MMMy`     sMMMMMMMMMMMMMMMMMMm`     /MMM "+r+bC+" ║"+r+"     OmegaDSToolkit factory for penetration testing"  +r)
    print(bC+"        MMm`     :MMMMMMMMMMMMMMMMMMMMy      oMM "+r+bC+" ║"  +r)
    print(bC+"        MM-      MMMMMMMMMMMMMMMMMMMMMM+      mM "+r+bC+" ╚════╗"  +r)
    print(bC+"        MMo      NMMMMMMMMMMMMMMMMMMMMM/     `MM "+r+bC+"      ╟──────"+gC+"►"+bC2+" Created by       :"+rC+" Thomas Pellissier"+bC2+" (© Delta_Society™)"  +r)
    print(bC+"        MMN`     yMMMMMMMMMMMMMMMMMMMMN`     sMM "+r+bC+"      ╟──────"+gC+"►"+bC2+" Version          :"+rC+f" {version}"  +r)
    print(bC+"        MMMh`    .NMMMMMMMMMMMMMMMMMMM+     /MMM "+r+bC+"      ╟──────"+gC+"►"+bC2+" Internet Status  :"+rC+f" {connectionstatus}"  +r)
    print(bC+"        MMMMh.    :NMMMMMMMMMMMMMMMMMs    `oMMMM "+r+bC+"      ╟────╥─"+gC+"►"+bC2+" Codename         : @"+rC+"MyMeepSQL or "+bC2+"@"+bC2+"th300905"  +r)
    print(bC+"        MMMMMNo.   -hNMMMMMMMMMMMMMm+   `/dMMMMM "+r+bC+"      ║"+bC+"    ╙──────────────────"+gC+"►"+bC2+rC+"   The"+bC2+" seconde"+rC+" codename is also mine"  +r)
    print(bC+"        NdMMMMMNy/.` -smMMMMMMMMNy/` `:smMMMMMNm "+r+bC+"      ╚════════╗"  +r)
    print(bC+"        m`hNMMMMMMNdy: `MMMMMMMM+ .shmMMMMMMNm:+ "+r+bC+"               ║"+r+"                       Developed for linux "  +r)
    print(bC+'        m  -/+ooooooo+  mMMMMMMM: .ooooooo+/:` o '+r+bC+"               ║"  +r)
    print(bC+"        N               hMMMMMMM`              o "+r+bC+"               ║"+gC+"             Welcome to the OmegaDSToolkit (ODST)."+r)
    print(bC+"        M               yMMMMMMM               s "+r+bC+'               ║'+gC+' The toolkit which includes a set of penetration testing tools.'+r)
    print(bC+"        MNmmmmmmmmmmmmmmMMMMMMMMmmmmmmmmmmmmmmmM "+r+bC+"               ║"+r)
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+bC+"               ║"+rC+"         The OmegaDSToolkit is a product of Delta_Society™"  +r)
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+bC+"               ║"+r) ##????## Date | Time : {here i want to make a digital clock in real time if enyone know how to make it, please contact me}
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+bC+"               ║"+r)
    print(bC+"                                                                ║"+r+"                        SELECT AN OPTION"  +r)
    print()
    print()
    print() 
    print("                ["+bC+"1"+r+"]"+gC+"    Information Gathering"  +r)
    print("                ["+bC+"2"+r+"]"+gC+"    Wireless attacks"  +r)
    print("                ["+bC+"3"+r+"]"+gC+"    Useful Windows tools"  +r)
    print("                ["+bC+"X"+r+"]"+gC+"    Exit\n"  +r)
    print("Not finish\n")

    while True:
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"Menu"+bC+"]")
        choice = str(input(bC+"└╼"+rC+"$ "+r))
        break
    
    if choice == "1":
       informationgathering_mainpage()
    elif choice == "2":
        wireless_mainpage()
    elif choice == "3":
        windowstools_mainpage()
    elif choice == "X":
        choice = str(choice)
        print(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Exiting..."+bC+"]"+r)
        sleep(0.5)
        exit()
    elif choice == "x":
        print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"For the main page, the correct command is 'X' and not 'x' for exit"+bC+"]"+r)
        input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
        main_page()
    elif not choice:
        error()
        cls()
        main_page()
    else:
        invalid_option()
        cls()
        main_page()
        
#################################################################
try:                                                            #
    is_admin = os.getuid() == 0                                 #
except AttributeError:                                          #
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0       #
if is_admin == False:                                           #
    if os.name=='nt':                                           #
        systemname = "administrator"                            #   check if the user run ODST with root/admin privilege
    else:                                                       #   if user are on windows, he sayed "administrator", on linux he sayed "root"
        systemname = "root"                                     #
    print(f"Run it as {systemname}")                            #
    input("Press [ENTER] key to continue")                      #
    exit()                                                      #
                                                                #
elif is_admin == True:                                          #
    checkmodules()                                              ### checking if modules are installed
#################################################################

import sys                                                                                      # Title page
sys.stdout.write("\x1b]2;OmegaDSToolkit coded by @MyMeepSQL for Delta_Scoiety\x07")             #

main_page()                                                                                     # for show the main page on starts
input()                                                                                         # for debugging
#-END-OF-MAIN-PAGE---------------------------------------------------#
































#      _______________________
#     |                       |
#     |    ____      ____     |
#     |   |____|    |____|    |
#     |                       |
#     |   __           __     |
#     |   \ \         / /     |
#     |    \ \_______/ /      |
#     |     \_________/       |
#     |_______________________|
#             |       |
#             |       |
#  ___________|       |____________
# |                                |
# |                                |
# |                                |
# |                                |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |_____|                 |________|
#       |                 |
#       |                 |
#       |                 |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       | ____  | ______j |
#       |_______|_________| build by MyMeepSQL | Please don’t change that. This is my signature
#                           Codename MyMeepSQL in © Delta_Society��
