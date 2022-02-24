#---[Metadata]-------------------------------------------------------#
#  Filename ~ OmegaDSToolkit[v0.0.0.6#dev]     [Update: 24-02-2022]  #
#---[Info]-----------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}  #
#                                                                    #
#  OmegaDSTookit ~ A massive penetration testing toolkit             #
#  Language  ~  Python3                                              #
#---[Author]---------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                    #
#---[Operating System]-----------------------------------------------#
#  Developed for linux                                               #
#---[Licence]--------------------------------------------------------#
#  GNU General Public License v3.0                                   #
#--------------------------------------------------------------------

version = "0.0.0.8"

import os
from time import sleep

def cls():                                                  # check if the user use windows or linux for the "clear" or "cls" function
    os.system('cls' if os.name=='nt' else 'clear')              #

#-Check module is installed------------------------------------------#
######################################################################
import ctypes                                                        #
try:                                                                 #
    is_admin = os.getuid() == 0                                      #
except AttributeError:                                               #
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0            #
if is_admin == False:                                                #
    if os.name=='nt':                                                #
        systemname = "administrator"                                 #   check if the user run ODST with root/admin privilege
    else:                                                            #   if user are on windows, he sayed "administrator", on linux he sayed "root"
        systemname = "root"                                          #
    print(f"Run it as {systemname}")                                 #
    exit()                                                           #
elif is_admin == True:                                               #
    cls()                                                            ######### checking if modules are installed
    import sys                                                               #
    sys.stdout.write("\x1b]2;Checking if all modules are [OK]\x07")          #
    try:                                                                     #
        print("Checking if the current modules of ODST are installed...")    #
        print()                                                              #
        sleep(1.5)                                                           #
        import progress                                                      #
        import colored                                                       #
        import nslookup                                                      #
        import keyboard                                                      #
        import pythonping                                                    #
        import urllib.request                                                #
        import shutil                                                        #
        import time                                                          #
        print("[OK]         All modules are install !")                      #
        print("[>>]         Launching of ODST...")                           #
        from colored import fg, attr                                         #
        from pythonping import ping                                          #
        sleep(1)                                                             #
    except KeyboardInterrupt:                                                #
        print()                                                              #
        abortmsg = "[ERROR]      User aborted"                               #
        exit(abortmsg)                                                       #
    except ImportError:                                                      ####################################
        criticalmsg = "[CRITICAL]   A current(s) module(s) was not installed, run the 'setup.py' for install it"#
        exit(criticalmsg)                                                    ####################################
##############################################################################

#-END-OF-MODULES-CHECKER---------------------------------------------#

#-Colors section-----------------------------------------------------#

# The blues
bC = fg('#1d89f3')      # blue
bC2 = fg('#0B4D8F')     # dark blue

# The reds
rC = fg('#F44336')      # red
rC3 = fg('#ffa000')     # light orange
rC2 = fg('#ec5a0d')     # orange

# The greens
gC = fg('#39CC3F')      # green

# The yellows
yC = fg('#EDFF00')


r = attr('reset')       # pour terminer le formatage de la couleur
#--------------------------------------------------------------------#

#-Fonctions----------------------------------------------------------#
#########################################################
def connection(host='https://google.com'):              #
    try:                                                #
        urllib.request.urlopen(host)                    #
        return True                                     #
    except:                                             #   Check if the user have an Internet connection 
        return False                                    #
if connection() == True:                                #
    connectionstatus = (gC+"Connected"+r)               #
else:                                                   #
    connectionstatus = (rC3+"No Internet"+r)            #
#########################################################

try:
    def exitodst():
        print(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Exiting ODST..."+bC+"]"+r)
        print(bC+"["+r+rC2+"^_^"+r+bC+"]"+r+bC+"-["+r+gC+" By "+bC+"]"+r)
        exit()
    ### if the user doesn't choose option
    def error():
        print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Choose a option"+bC+"]"+r)
        input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)


    ### if the user enter a bad option (if the option type by the user are not recognized)
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

    ##          coming soon !



    #---Information Gathering--------------------------------------------#

    ### Information Gathering | main page ###
    def informationgathering_mainpage():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/Information_Gathering/\x07")                    #
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
        print(bC+"       ╔═════════════════════════════════════════════════╗"+rC2+"|_____|          "+r)
        print(bC+"       ╚═════╗                                           ╚════════►               "+r)
        print(bC+"             ║"+r)
        print(bC+"             ║"+r+"   In this category you will find tools to collect information,")
        print(bC+"             ║"+r+"              such as port scan, SQL injections etc")
        print(bC+"             ║"+r)
        print(bC+"             ╟──── ["+gC+"  Made by   "+bC+"] ───"+gC+"► "+rC+"Thomas Pellissier"+bC2+" (from © Delta_Society™)"+r)
        print(bC+"             ╟──── ["+gC+"  Codename  "+bC+"] ───"+gC+"► "+bC2+"@"+r+rC+"MyMeepSQL")
        print(bC+"             ╟──── ["+gC+"  Version   "+bC+"] ───"+gC+"► "+bC2+"v"+rC+"0.0.1"+r)
        print(bC+"             ║"+r)
        print(bC+"             ╟────"+gC+"► "+r+"["+bC+"1"+r+"]"+gC+"    Scan"+r)
        print(bC+"             ╟────"+gC+"► "+r+"["+bC+"2"+r+"]"+gC+"    "+r)
        print(bC+"             ╟────"+gC+"► "+r+"["+bC+"x"+r+"]"+gC+"    Return to the"+rC+" OmegaDSToolkit"+gC+" main page"+r)
        print(bC+"             ╙────"+gC+"► "+r+"["+bC+"exit"+r+"]"+gC+" Exit the ODST\n"  +r)
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Information Gathering"+r+bC+"]")
        infogathering_mainpage = str(input(bC+"└╼"+rC+"$ "+r))

        if infogathering_mainpage == "1":
            informationgathering_scan_mainpage()
        elif infogathering_mainpage == "x":
            cls()
            main_page()
        elif infogathering_mainpage == "X":
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"For this page, the correct command is 'X' and not 'x' for return to the"+rC+" OmegaDSToolkit"+gC+" main page"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
            informationgathering_mainpage()
        elif not infogathering_mainpage:
            error()
            cls()
            infogathering_mainpage()
        else:
            invalid_option()
            cls()
            informationgathering_mainpage()

    ### Information Gathering | Scan tools ### 
    def informationgathering_scan_mainpage():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/Information_Gathering/ScanTools\x07")           #
        cls()
        print(gC+"       _____             _____         _               "+r)
        print(gC+"      |   __|___ ___ ___|_   _|___ ___| |___           "+r)
        print(gC+"      |__   |  _| .'|   | | | | . | . | |_ -|          "+r)
        print(gC+"      |_____|___|__,|_|_| |_| |___|___|_|___|          "+r)
        print(bC+"     ╓────────────────────────────────────────"+gC+"►"+r)
        print(bC+"     ╙────╖")
        print(bC+"          ║"+r+"   Some tools for scanning target")
        print(bC+"          ║"+r)
        print(bC+"          ╟──────"+gC+"►"+r+bC2+" Created by :"+r+rC+" Thomas Pellissier"+bC2+" (from © Delta_Society™)"+r)
        print(bC+"          ╟──────"+gC+"►"+r+bC2+" Codename   : @"+r+rC+"MyMeepSQL"+r)
        print(bC+"          ╟──────"+gC+"►"+r+bC2+" Version    : v"+r+rC+"0.0.1"+r)
        print(bC+"          ║"+r)
        print(bC+"          ╙─────╖"+r)
        print(bC+"                ╟────"+gC+"► "+r+"["+bC+"1"+r+"]"+gC+"    Nmap"+r)
        print(bC+"                ╟────"+gC+"► "+r+"["+bC+"2"+r+"]"+gC+"    sqlmap"+r)
        print(bC+"                ╟────"+gC+"► "+r+"["+bC+"x"+r+"]"+gC+"    Return to the"+rC+" Information Gathering"+gC+" main page"+r)
        print(bC+"                ╟────"+gC+"► "+r+"["+bC+"X"+r+"]"+gC+"    Return to the"+rC+" OmegaDSToolkit"+gC+" main page"+r)
        print(bC+"                ╙────"+gC+"► "+r+"["+bC+"exit"+r+"]"+gC+" Exit the ODST\n"  +r)

        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"ScanTools"+r+bC+"]")
        scan_mainpage_ = str(input(bC+"└╼"+rC+"$ "+r))

        # if scan_mainpage_ == 1:
            # informationgathering_nmap()

        # if scan_mainpage_ == 2:
            # informationgathering_sqlmap()

        if scan_mainpage_ == "x":
            cls()
            informationgathering_mainpage()
        elif scan_mainpage_ == "X":
            cls()
            main_page()
        elif scan_mainpage_ == "exit":
            exitodst()
        elif not scan_mainpage_:
                error()
                cls()
                scan_mainpage_()
        else:
            invalid_option()
            cls()
            informationgathering_scan_mainpage()
            

    #---End of Information Gathering-------------------------------------#



    #---Usefull Windows tool---------------------------------------------#

    ### Usefull Windows tool | main page ###
    def usefulltools_mainpage():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/\x07")                                   #
        cls()
        print(rC2+"      _____ _____         _     ")
        print(rC2+"     |  |  |_   _|___ ___| |___ ")
        print(rC2+"     |  |  | | | | . | . | |_ -|")
        print(rC2+"     |_____| |_| |___|___|_|___|")
        print(bC+"   ╔═════════════════════════════"+gC+"►"+r)
        print(bC+"   ╚════╗")
        print(bC+"        ║"+r+"   UsefulTools include several useful")
        print(bC+"        ║"+r+"        tools like Windows tools")
        print(bC+"        ║")
        print(bC+"        ╟──── ["+gC+"  Made by   "+bC+"] ───"+gC+"►"+rC+" Thomas Pellissier"+bC2+" (from © Delta_Society™)"+r)
        print(bC+"        ╟──── ["+gC+"  Codename  "+bC+"] ───"+gC+"►"+bC2+" @"+rC+"MyMeepSQL")
        print(bC+"        ╟──── ["+gC+"  Version   "+bC+"] ───"+gC+"►"+bC2+" v"+rC+"0.0.1"+r)
        print(bC+"        ║")
        print(bC+"        ╟────"+gC+"► "+r+"["+bC+"1"+r+"]"+gC+"     Backup tool (for make backup quickly)"+r)
        print(bC+"        ╟────"+gC+"► "+r+"["+bC+"2"+r+"]"+gC+"     Network commands (ping, telnet etc)"+r)
        print(bC+"        ╟────"+gC+"► "+r+"["+bC+"x"+r+"]"+gC+"     Return to the"+rC+" OmegaDSToolkit"+gC+" main page"+r)
        print(bC+"        ╙────"+gC+"► "+r+"["+bC+"exit"+r+"]"+gC+"  Exit the ODST\n"  +r)

        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"UWTools"+bC+"]")
        windowsT_mainpage = str(input(bC+"└╼"+rC+"$ "+r))

        if windowsT_mainpage == "1":
            usefulltools_backup_main()
        if windowsT_mainpage == "2":
            usefulltools_networkC_main_page()
        elif windowsT_mainpage == "x":
            cls()
            main_page()
        elif windowsT_mainpage == "X":
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"For this page, the correct command is 'x' and not 'X' for return to the main page the"+rC+" OmegaDSToolkit"+gC+" main page"+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
            usefulltools_mainpage()
        elif not windowsT_mainpage:
                error()
                cls()
                usefulltools_mainpage()
        elif windowsT_mainpage == "exit":
            exitodst()
        else:
            invalid_option()
            cls()
            usefulltools_mainpage()
            
    ### Usefull Windows tool  | Network commands ###
    def usefulltools_networkC_main_page():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/NetworkCommands/\x07")                   #
        cls()
        print(rC2+"      _____       _                     _      _____                                 _      ")
        print(rC2+"     |   | | ___ | |_  _ _ _  ___  ___ | |_   |     | ___  _____  _____  ___  ___  _| | ___ ")
        print(rC2+"     | | | || -_||  _|| | | || . ||  _|| '_|  |   --|| . ||     ||     || .'||   || . ||_ -|")
        print(rC2+"     |_|___||___||_|  |_____||___||_|  |_,_|  |_____||___||_|_|_||_|_|_||__,||_|_||___||___|")
        print(bC+"   ╓─────────────────────────────────────────────────────────────────────────────────────────"+gC+"►"+r)
        print(bC+"   ╚════╗"+r)
        print(bC+"        ║"+r+"    Some network commands  "+r)
        print(bC+"        ║"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Created by       :"+rC+" Thomas Pellissier"+bC2+" (from © Delta_Society™)"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Codename         : @"+rC+"MyMeepSQL"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Version          : v"+rC+"0.0.3"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Internet Status  : "+rC+f"{connectionstatus}"+r)
        print(bC+"        ║"+r)
        print(bC+"        ╚══════╗"  )
        print(bC+"               ╟────"+gC+"► "+r+"["+bC+"1"+r+"]"+gC+"     Ping (Just check if the destination is responding)"+r)
        print(bC+"               ╟────"+gC+"► "+r+"["+bC+"2"+r+"]"+gC+"     NSLookup (Find a domain's IP)"+r)
        print(bC+"               ╟────"+gC+"► "+r+"["+bC+"x"+r+"]"+gC+"     Return to the"+rC+" UTools"+gC+" main page"+r)
        print(bC+"               ╟────"+gC+"► "+r+"["+bC+"X"+r+"]"+gC+"     Return to the"+rC+" OmegaDSToolkit"+gC+" main page"+r)
        print(bC+"               ╙────"+gC+"► "+r+"["+bC+"exit"+r+"]"+gC+"  Exit the ODST\n"  +r)
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands"+r+bC+"]")
        networkC_main_page = str(input(bC+"└╼"+rC+"$ "+r))

        if networkC_main_page == "1":
            usefulltools_networkC_ping()
        elif networkC_main_page == "2":
            usefulltools_networkC_nslookup()
        elif networkC_main_page == "exit":
            exitodst()
        elif networkC_main_page == "x":
            usefulltools_mainpage()
        elif networkC_main_page == "X":
            main_page()
        elif not networkC_main_page:
                error()
                cls()
                usefulltools_networkC_main_page()
        else:
            invalid_option()
            cls()
            usefulltools_networkC_main_page()

    def usefulltools_networkC_nslookup():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/NetworkCommands/NSLookup\x07")           #
        cls()
        print(rC2+"      _______ _______ _____                __")
        print(rC2+"     |    |  |     __|     |_.-----.-----.|  |--.--.--.-----.")
        print(rC2+"     |       |__     |       |  _  |  _  ||    <|  |  |  _  |")
        print(rC2+"     |__|____|_______|_______|_____|_____||__|__|_____|   __|")
        print(bC+"   ╓──────────────────────────────────────────────────"+rC2+"|__|"+bC+"────"+gC+"►"+r)
        print(bC+"   ╚════╗"+r)
        print(bC+"        ║"+r+"    Some windows network commands  "+r)
        print(bC+"        ║"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Created by       :"+rC+" Thomas Pellissier"+bC2+" (from © Delta_Society™)"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Codename         : @"+rC+"MyMeepSQL"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Version          : v"+rC+"0.0.3"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Internet Status  : "+rC+f"{connectionstatus}"+r)
        print(bC+"      ╔═╝"+r)
        print(bC+"      ╚════════════════════════════════════════════════════════════════════════════════════╗"+r)
        print("         Write a domain for look the IP he used (type 'exit' for exit the NSLookup tool)"+bC+"   ║"+r)
        print(bC+"      ═════════════════════════════════════════════════════════════════════════════════════╝\n"+r)
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands | Nslookup"+r+bC+"]")
        domain = str(input(bC+"└╼"+rC+"$ "+r))

        if domain == "exit":
            usefulltools_networkC_main_page()
        elif domain:
            if connection() == True:
                try:
                    import socket
                    addresse = socket.gethostbyname(domain)
                    print()
                    print(bC+"  ╔══════════════════════╗")
                    print(bC+"  ║   "+r+"NSLookup respond"+bC+"   ║")
                    print(bC+"  ╚════╦═════════════════╝")
                    print("╔══════╝"+r)
                    print(bC+"╟──────"+gC+"►"+bC2+" Name    :"+rC+f" {domain}")
                    print(bC+"╙──────"+gC+"►"+bC2+" Adresse :"+rC+f" {addresse}")
                    print()
                    input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to write an another domain for nslookup"+bC+"]"+r)
                    usefulltools_networkC_nslookup()
                    # from nslookup import Nslookup

                    # # set optional Cloudflare public DNS server
                    # dns_query = Nslookup(dns_servers=["1.1.1.1"])

                    # ips_record = dns_query.dns_lookup(domain)
                    # print(ips_record.response_full, ips_record.answer)

                    # soa_record = dns_query.soa_lookup(domain)
                    # print(soa_record.response_full, soa_record.answer)

                except socket.gaierror:
                    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+f"'{domain}' not found, please ckeck the domain before lookup it"+bC+"]"+r)
                    input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)
                    usefulltools_networkC_nslookup()
            else:
                print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Can’t reach the destination, check your Internet connection and try again"+bC+"]"+r)
                input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)
                usefulltools_networkC_ping()
        else:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+f"No domain found, write an domain for lookup it"+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)
            usefulltools_networkC_nslookup()

    def usefulltools_networkC_ping():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/NetworkCommands/Ping\x07")               #
        cls()
        print(rC2+"      ______ __               ")
        print(rC2+"     |   __ \__|.-----.-----. ")
        print(rC2+"     |    __/  ||     |  _  | ")
        print(rC2+"     |___|  |__||__|__|___  | ")
        print(bC+"   ╓──────────────────"+rC2+"|_____|"+bC+"──"+gC+"►"+r)
        print(bC+"   ╚════╗"+r)
        print(bC+"        ║"+r+"    Ping IP for verified it's online  "+r)
        print(bC+"        ║"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Created by       :"+rC+" Thomas Pellissier"+bC2+" (from © Delta_Society™)"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Codename         : @"+rC+"MyMeepSQL"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Version          : v"+rC+"0.0.9"+r)
        print(bC+"        ╟──────"+gC+"►"+bC2+" Internet Status  : "+rC+f"{connectionstatus}"+r)
        print(bC+"      ╔═╝"+r)
        print(bC+"      ╚════════════════════════════════════════════════════════╗"+r)
        print("         Write an IP to ping it, press CTRL + C for stop the "+bC+"  ║"+r)
        print("          ping process (type 'exit' for exit the ping tool)"+bC+"    ║"+r)
        print(bC+"      ═════════════════════════════════════════════════════════╝\n"+r)
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+r+gC+"Network commands | Ping"+r+bC+"]")
        IP = str(input(bC+"└╼"+rC+"$ "+r))

        if IP == "exit":
            usefulltools_networkC_main_page()
        elif IP:
            if connection() == True:
                try:
                    hostname = IP
                    response = os.system("ping " + hostname + "-c 4")
                    print(response)

                    # ping(IP, verbose=True, count=6)
                    # print(ping(IP))
                    # print()
                    # input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to write an another IP for pinging"+bC+"]"+r)
                    # usefulltools_networkC_ping()
                    
                    input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to write an another IP for pinging"+bC+"]"+r)
                    usefulltools_networkC_ping()
                except KeyboardInterrupt:
                    print()
                    print(bC+"["+r+rC2+"*"+r+bC+"]"+r+bC+"-["+r+gC+"CTRL + C detected stop the ping."+bC+"]"+r)
                    input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to write an another IP for pinging"+bC+"]"+r)
                    usefulltools_networkC_ping()
                except RuntimeError:
                    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+f"'{IP}' not found, prlease ckeck the IP before ping it"+bC+"]"+r)
                    input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)
                    usefulltools_networkC_ping()
            else:
                print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Can’t reach the destination, check your Internet connection and try again"+bC+"]"+r)
                input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)
                usefulltools_networkC_ping()
        else:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+f"No IP found, write an IP to ping it"+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)
            usefulltools_networkC_ping()

    ### Usefull Windows tool  | Backup tool ###
    def usefulltools_backup_main():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/BackupTool/\x07")                        #
        cls()
        print(rC2+"      _______                              ______              __                  "+r)
        print(rC2+"     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
        print(rC2+"     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
        print(rC2+"     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
        print(rC2+"                             |_____|                                      |__|     "+r)
        print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+gC+"►"+r)
        print(bC+"     ╚════════╗"+r)
        print(bC+"              ║"+r+"  A tool for make backup quickly"+r)
        print(bC+"              ║"+"") 
        print(bC+"              ╟──────"+gC+"►"+bC2+" Created by :"+rC+"  Thomas Pellissier"+bC2+" (from © Delta_Society™)"+r)
        print(bC+"              ╟──────"+gC+"►"+bC2+" Version    :"+rC+"  0.1.1"+r)
        print(bC+"              ╟──────"+gC+"►"+bC2+" Codename   :  @"+rC+"MyMeepSQL"+r)
        print(bC+"     ╔════════╝"+r)
        print(bC+"     ╚═══════════════════════════════════════════╗"+r)
        print("            Do you want make backup (y/n)"+bC+"        ║"+r)
        print(bC+"     ════════════════════════════════════════════╝"+r)
        print()
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
        choiceB = str(input(bC+"└╼"+rC+"$ "+r))

        if choiceB == "y" or choiceB == "Y":
            usefulltools_backup_source()
        elif choiceB == "n":
            usefulltools_mainpage()
        elif not choiceB:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Chose y or n"+bC+"]"+r)                                         # the function for the error with no respond
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)                           #
            usefulltools_backup_main()
        else:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Invalid option, chose y or n"+bC+"]"+r)                         # the function for the error with no respond
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)                           #
            usefulltools_backup_main()

    def usefulltools_backup_source():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/BackupTool/Source\x07")                  #
        cls()
        print(rC2+"        _______                              ______              __                  "+r)
        print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
        print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
        print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
        print(rC2+"                               |_____|                                      |__|     "+r)
        print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
        print(bC+"     ╚═══════════════════════════════════════════╗"+r)
        print(gC+"       Whish folder or file you want backup it ?"+bC+" ║"+r)
        print(rC+"             /!\ "+gC+"Type the source path"+rC+" /!\ "+bC+"       ║"+r)
        print(bC+"     ════════════════════════════════════════════╝"+r)
        print()
        global source
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
        source = str(input(bC+"└╼"+rC+"$ "+r))

        if not source:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Type your source folder/file "+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
            usefulltools_backup_source()
        else:
            usefulltools_backup_destination()

    def usefulltools_backup_destination():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/BackupTool/Destination\x07")             #
        cls()
        print(rC2+"        _______                              ______              __                  "+r)
        print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
        print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
        print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
        print(rC2+"                               |_____|                                      |__|     "+r)
        print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
        print(bC+"     ╚═══════════════════════════════════════════╗"+r)
        print(gC+"             Where you want to backup it ?"+bC+"       ║"+r)
        print(rC+"           /!\ "+gC+"Type the destination  path"+rC+" /!\ "+bC+"   ║"+r)
        print(bC+"     ════════════════════════════════════════════╝"+r)
        print()
        global destination
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
        destination = str(input(bC+"└╼"+rC+"$ "+r))
            
        if not destination:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Type your target folder/file"+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)
            usefulltools_backup_destination()
        else:
            usefulltools_backup_verification()

    def usefulltools_backup_verification():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/BackupTool/Verification\x07")            #
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
        print(bC+"          ╟──────"+gC+"►"+rC+" Source"+bC+" =="+gC+">"+r+f" {source}")
        print(bC+"          ╚──────"+gC+"►"+rC+" Target"+bC+" =="+gC+">"+r+f" {destination}")
        print()
        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
        sure = str(input(bC+"└╼"+rC+"$ "+r))

        if not sure:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Chose y or n"+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] key to continue"+bC+"]"+r)
            usefulltools_backup_verification()

        elif sure == "y" or sure == "Y":
            import sys                                                                                      # Title page
            sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/BackupTool/Backuping...\x07")            #
            cls()
            print(rC2+"        _______                              ______              __                  "+r)
            print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
            print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
            print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
            print(rC2+"                               |_____|                                      |__|     "+r)
            print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
            print(bC+"     ╚══════════════════════╗"+r)
            print(gC+"            Backuping..."+bC+"    ║"+r)
            print(bC+"     ═══════════════════════╝"+r)

            try:
                from datetime import datetime
                from pathlib import Path
                import zipfile
                OBJECT_TO_BACKUP = f'{source}'                      # The file or directory to backup
                BACKUP_DIRECTORY = f'{destination}'                 # The location to store the backups in
                MAX_BACKUP_AMOUNT = 20                              # The maximum amount of backups to have in BACKUP_DIRECTORY


                object_to_backup_path = Path(OBJECT_TO_BACKUP)
                backup_directory_path = Path(BACKUP_DIRECTORY)
                assert object_to_backup_path.exists()               # Validate the object we are about to backup exists before we continue

                # Validate the backup directory exists and create if required
                backup_directory_path.mkdir(parents=True, exist_ok=True)

                # Get the amount of past backup zips in the backup directory already
                existing_backups = [
                    x for x in backup_directory_path.iterdir()
                    if x.is_file() and x.suffix == '.zip' and x.name.startswith('backup-')
                ]

                # Enforce max backups and delete oldest if there will be too many after the new backup
                oldest_to_newest_backup_by_name = list(sorted(existing_backups, key=lambda f: f.name))
                while len(oldest_to_newest_backup_by_name) >= MAX_BACKUP_AMOUNT:  # >= because we will have another soon
                    backup_to_delete = oldest_to_newest_backup_by_name.pop(0)
                    backup_to_delete.unlink()

                # Create zip file (for both file and folder options)
                backup_file_name = f'BACKUP-{datetime.now().strftime("%Y-%m-%d %Hh%M %Ss")} - {object_to_backup_path.name}.zip'
                zip_file = zipfile.ZipFile(str(backup_directory_path / backup_file_name), mode='w')
                if object_to_backup_path.is_file():
                    # If the object to write is a file, write the file
                    zip_file.write(
                        object_to_backup_path.absolute(),
                        arcname=object_to_backup_path.name,
                        compress_type=zipfile.ZIP_DEFLATED
                    )
                elif object_to_backup_path.is_dir():
                    # If the object to write is a directory, write all the files
                    for file in object_to_backup_path.glob('**/*'):
                        if file.is_file():
                            zip_file.write(
                                file.absolute(),
                                arcname=str(file.relative_to(object_to_backup_path)),
                                compress_type=zipfile.ZIP_DEFLATED
                            )
                # Close the created zip file
                zip_file.close()
                import sys                                                                                      # Title page
                sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/BackupTool/Successully_backuped\x07")    #
                cls()
                print(rC2+"        _______                              ______              __                  "+r)
                print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
                print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
                print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
                print(rC2+"                               |_____|                                      |__|     "+r)
                print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
                print(bC+"     ╚══════════════════════════════════════════╗"+r)
                print(gC+"          Folder/file copied successfully !"+bC+"     ║"+r)
                print(bC+"     ═══════════════════════════════════════════╝"+r)
                sleep(1.5)
                usefulltools_backup_reconfig()

            except PermissionError:
                print(bC+"║ ["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Permission denied"+bC+"]"+r)
                print(bC+"║ ["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Please check your permissions with your folder/users"+bC+"]"+r)
                print(bC+"["+r+rC2+"*"+r+bC+"]"+r+bC+"──["+r+gC+"If you want remake the backup config, type y else type n"+bC+"]"+r)
                print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
                permerror = str(input(bC+"└╼"+rC+"$ "+r))

                while not permerror:
                    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Chose y or n"+bC+"]"+r)
                    print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
                    permerror = str(input(bC+"└╼"+rC+"$ "+r))

                if permerror == "y" or permerror == "Y":
                    usefulltools_backup_source()

                if permerror == "n" or permerror == "N":
                    usefulltools_mainpage()
                    
            except:
                print(bC+"║ ["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Error occurred while copying file"+bC+"]"+r)
                print(bC+"║ ["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Check that the files are not corrupted or some other problem and redo the backup configuration"+bC+"]"+r)
                input(bC+"║ ["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] key to remake the backup configuration"+bC+"]"+r)
                usefulltools_backup_source()

        elif sure == "n" or sure =="N":
            usefulltools_backup_reconfig()

        else:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Invalid option, chose y or n"+bC+"]"+r)                             # the function for the error with no respond
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)                               #
            usefulltools_backup_verification()

    def usefulltools_backup_reconfig():
        import sys                                                                                       # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/UTools/BackupTool/Remake_the_backup_config\x07") #
        cls()
        print(rC2+"        _______                              ______              __                  "+r)
        print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
        print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
        print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
        print(rC2+"                               |_____|                                      |__|     "+r)
        print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
        print(bC+"     ╚════════════════════════════════════════════════════╗"+r)
        print(gC+"          Do you want reconfig the backup config ? (y/n)"+bC+"  ║"+r)
        print(bC+"     ═════════════════════════════════════════════════════╝"+r)
        print()
        print(bC+"┌─("+rC+"OmegaDSToolkit"+bC+")-["+yC+"~"+bC+"]-["+gC+"OmegaBackup"+bC+"]")
        choice = str(input(bC+"└╼"+rC+"$ "+r))

        if choice == "y" or choice == "Y":
            usefulltools_backup_source()
        elif choice == "n" or choice == "N":
            usefulltools_mainpage()
        elif not choice:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Choose y or n"+bC+"]"+r)
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)
            usefulltools_backup_reconfig()
        else:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"-["+r+gC+"Invalid option"+bC+"]"+r)                                       # the function for the error with no respond
            input(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"-["+r+gC+"Press [ENTER] key to retry"+bC+"]"+r)                           #
            usefulltools_backup_reconfig()
    #-End-Usefull Windows tool-------------------------------------------#

    #-OmegaDSToolkit-main-page-------------------------------------------#
    def main_page():
        import sys                                                                                      # Title page
        sys.stdout.write("\x1b]2;OmegaDSToolkit | /ODST/\x07")                                          #
        cls()
        print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+gC+"    _____                   ____  _____ _____         _ _   _ _"  +r)                                 # Police = rectangle
        print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+gC+"   |     |_____ ___ ___ ___|    \|   __|_   _|___ ___| | |_|_| |_"  +r)                               #
        print(bC+"        MMMMMMMMMMMMMMMMMNmmmmNNMMMMMMMMMMMMMMMM "+gC+"   |  |  |     | -_| . | .'|  |  |__   | | | | . | . | | '_| |  _|"  +r)                              #
        print(bC+"        MMMMMMMMMMMdy+:.```..```.-/shNMMMMMMMMMM "+gC+"   |_____|_|_|_|___|_  |__,|____/|_____| |_| |___|___|_|_,_|_|_|   "+gC+"v"+rC+f"{version}"+r)        #
        print(bC+"        MMMMMMMNy/``  -ohmNNNNNdy/`  `:smMMMMMMM "+bC+" ╓─────────────────"+gC+"|___|"+bC+"───────────────────────────────────────────────────────"+gC+"►"  +r)
        print(bC+"        MMMMMNo.    :dNMMMMMMMMMMMNo`   `/dMMMMM "+bC+" ║"  +r)
        print(bC+"        MMMMh.     sMMMMMMMMMMMMMMMMd.    `+NMMM "+bC+" ║"+r+"     OmegaDSToolkit factory for penetration testing"  +r)
        print(bC+"        MMMy`     sMMMMMMMMMMMMMMMMMMm`     /MMM "+bC+" ║"  +r)
        print(bC+"        MMm`     :MMMMMMMMMMMMMMMMMMMMy      oMM "+bC+" ╚════╗"  +r)
        print(bC+"        MM-      MMMMMMMMMMMMMMMMMMMMMM+      mM "+bC+"      ╟──────"+gC+"►"+bC2+" Created by       :"+rC+" Thomas Pellissier"+bC2+" (from © Delta_Society™)"  +r)
        print(bC+"        MMo      NMMMMMMMMMMMMMMMMMMMMM/     `MM "+bC+"      ╟──────"+gC+"►"+bC2+" Version          : v"+rC+f"{version}"  +r)
        print(bC+"        MMN`     yMMMMMMMMMMMMMMMMMMMMN`     sMM "+bC+"      ╟──────"+gC+"►"+bC2+" Internet Status  :"+rC+f" {connectionstatus}"  +r)
        print(bC+"        MMMh`    .NMMMMMMMMMMMMMMMMMMM+     /MMM "+bC+"      ╟────╥─"+gC+"►"+bC2+" Codename         : @"+rC+"MyMeepSQL or "+bC2+"@"+bC2+"th300905"  +r)
        print(bC+"        MMMMh.    :NMMMMMMMMMMMMMMMMMs    `oMMMM "+bC+"      ║"+bC+"    ╙──────────────────"+gC+"►"+bC2+rC+"   The"+bC2+" seconde"+rC+" codename is also mine"  +r)
        print(bC+"        MMMMMNo.   -hNMMMMMMMMMMMMMm+   `/dMMMMM "+bC+"      ╚════════╗"  +r)
        print(bC+"        NdMMMMMNy/.` -smMMMMMMMMNy/` `:smMMMMMNm "+bC+"               ║"+r+"                       Developed for linux "  +r)
        print(bC+"        m`hNMMMMMMNdy: `MMMMMMMM+ .shmMMMMMMNm:+ "+bC+"               ║"  +r)
        print(bC+'        m  -/+ooooooo+  mMMMMMMM: .ooooooo+/:` o '+bC+"               ║"+gC+"             Welcome to the OmegaDSToolkit (ODST)."+r)
        print(bC+"        N               hMMMMMMM`              o "+bC+'               ║'+gC+' The toolkit which includes a set of penetration testing tools.'+r)
        print(bC+"        M               yMMMMMMM               s "+bC+"               ║"+r)
        print(bC+"        MNmmmmmmmmmmmmmmMMMMMMMMmmmmmmmmmmmmmmmM "+bC+"               ║"+rC+"         The OmegaDSToolkit is a product of © Delta_Society™"  +r)
        print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+bC+"               ║"+r) ##????## Date | Time : {here i want to make a digital clock in real time if enyone know how to make it, please contact me}
        print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+bC+"               ║"+r)
        print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+bC+"               ║"+r+"                        SELECT AN OPTION"  )
        print()
        print()
        print("                ["+bC+"1"+r+"]"+gC+"    Information Gathering"  +r)
        print("                ["+bC+"2"+r+"]"+gC+"    Wireless attacks"  +r)
        print("                ["+bC+"3"+r+"]"+gC+"    Useful tools (UT)"  +r)
        print("                ["+bC+"exit"+r+"]"+gC+" Exit the ODST\n"  +r)
        print("ODST was not finish and he's totally in development!\n")

        print(bC+"┌──("+rC+"OmegaDSToolkit"+bC+")-["+r+"~"+bC+"]-["+gC+"Menu"+bC+"]")
        choice = str(input(bC+"└╼"+rC+"$ "+r))

        if choice == "1":
            informationgathering_mainpage()
        elif choice == "2":
            wireless_mainpage()
        elif choice == "3":
            usefulltools_mainpage()
        elif choice == "exit":
            exitodst()
        elif not choice:
            error()
            cls()
            main_page()
        else:
            invalid_option()
            cls()
            main_page()

    #-END-OF-MAIN-PAGE---------------------------------------------------#

    main_page()                                                                                     # for show the main page on starts
    input()                                                                                         # for debugging

except KeyboardInterrupt:
    print()
    exitodst()





























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
#       |_______|_________| Build by MyMeepSQL | Please don’t change that. This is my signature.
#                           Codename : MyMeepSQL by © Delta_Society™
