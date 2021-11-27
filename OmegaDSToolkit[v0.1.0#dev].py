
#-[Metadata]----------------------------------------------------#
#  Filename: OmegaDSToolkit[v0.1.0#dev]    [Update: 26-11-2021] #
#                                                               #
#-[Info]--------------------------------------------------------#
#  OmegaDSTookit - Factory for penetration testing              #
#  Language   - Python3                                         #
#                                                               #
#-[Author{s}]---------------------------------------------------#
#  Thomas Pellissier ~ @Meep                                    #
#-[Operating System]--------------------------------------------#
#  Developed for linux and windows                              #
#-[Licence]-----------------------------------------------------#
#  GNU General Public License v3.0                              #
#---------------------------------------------------------------#

version = "0.1.0"

#-Import section-----------------------------------------------------#
import time
import os
from progress.bar import Bar
from typing import Text
from colored import fg, attr                    # fg = la couleur de départ // attr = la fin de la couleur, pour pas que tout le texte qui suit sera en couleur
from pythonping import ping                     #   https://www.ictshore.com/python/python-ping-tutorial/
clear = lambda: os.system("cls")
clear = lambda: os.system("clear")
import shutil


#--------------------------------------------------------------------#


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
## Progress bas when the tool starting
def startbar():
    with Bar(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Starting the OmegaDSToolkit..."+bC+"]"+r) as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()
    print(bC+"["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Done"+bC+"]"+r)
    time.sleep(1)
    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
### if the user doesn't choose option
def error():
    print()
    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Choose a option"+bC+"]"+r)

### if the user enter a bad option (if the option type by the user are)
def invalid_option():
    print()
    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Invalid option"+bC+"]"+r)

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
    print(bC+"             ╟────"+r+gC+"► "+r+"["+bC+"01"+r+"]"+gC+"    Scan"+r)
    print(bC+"             ╟────"+r+gC+"► "+r+"["+bC+"02"+r+"]"+gC+"    "+r)
    print(bC+"             ╟────"+r+gC+"► "+r+"["+bC+"99"+r+"]"+gC+"    Return to the main page\n"+r)
     
    while True:
        try:
            print(bC+"┌─("+r+rC+"OmegaDSToolkit"+r+bC+")─["+r+yC+"~"+r+bC+"]─["+r+gC+"Information Gathering"+r+bC+"]")
            infogathering_mainpage = int(input(bC+"└───"+r+yC+"$ "+r))
            break
        except:
            error()
            input()
            cls()
            informationgathering_mainpage()

    if infogathering_mainpage == 1:
        scan_mainpage()
    elif infogathering_mainpage == 99:
        cls()
        main_page()
    else:
        invalid_option()
        input()
        cls()
        informationgathering_mainpage()
        
### Information Gathering | Scan tools ### 
def scan_mainpage():
    cls()
    print(gC+"       _____             _____         _               "+r)
    print(gC+"      |   __|___ ___ ___|_   _|___ ___| |___           "+r)
    print(gC+"      |__   |  _| .'|   | | | | . | . | |_ -|          "+r)
    print(gC+"      |_____|___|__,|_|_| |_| |___|___|_|___|          "+r)
    print(bC+"     ╓────────────────────────────────────────"+r+gC+"►"+r)
    print(bC+"     ║"+r+"   Some tools for scanning target") 
    print(bC+"     ╙────╖")
    print(bC+"          ╟──────"+r+gC+"►"+r+bC2+" Created by :"+r+rC+"  Thomas Pellissier"+r+bC2+" (© Delta_Society™)"+r)
    print(bC+"          ╟──────"+r+gC+"►"+r+bC2+" Codename   : @"+r+rC+"MyMeepSQL"+r)
    print(bC+"          ╟──────"+r+gC+"►"+r+bC2+" Version    :"+r+rC+"  0.0.1"+r)
    print(bC+"          ╙─────╖"+r)
    print(bC+"                ╟────"+r+gC+"► "+r+"["+bC+"01"+r+"]"+gC+"    Nmap"+r)
    print(bC+"                ╟────"+r+gC+"► "+r+"["+bC+"88"+r+"]"+gC+"    Return to the"+r+bC2+" Information Gathering"+r+gC+" main page"+r)
    print(bC+"                ╟────"+r+gC+"► "+r+"["+bC+"99"+r+"]"+gC+"    Return to the main page\n"+r)    

    while True:
        try:
            print(bC+"┌─("+r+rC+"OmegaDSToolkit"+r+bC+")─["+r+yC+"~"+r+bC+"]─["+r+gC+"Information Gathering | ScanTools"+r+bC+"]")
            fyodor_mainpage = int(input(bC+"└───"+r+yC+"$ "+r))
            break
        except:
            error()
            input()
            cls()
            scan_mainpage()
            
    if fyodor_mainpage == 88:
        cls()
        informationgathering_mainpage()
        
    elif fyodor_mainpage == 99:
        cls()
        main_page()
    else:
        invalid_option()
        input()
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
    print(bC+"     ┌──────────────────────────────────"+r+gC+"►"+r)
    print(bC+"     └──┐")
    print(bC+"        │"+r+"   UsefulWindowsTools include several  ")
    print(bC+"        │"+r+"          useful windows tools")       
    print(bC+"        │ ")
    print(bC+"        ├──── ["+r+gC+"  Made by   "+r+bC+"] ───"+r+gC+"►"+r+rC+" Thomas Pellissier"+r+bC2+" (© Delta_Society™)"+r)
    print(bC+"        ├──── ["+r+gC+"  Codename  "+r+bC+"] ───"+r+gC+"►"+r+bC2+" @"+r+rC+"MyMeepSQL")
    print(bC+"        ├──── ["+r+gC+"  Version   "+r+bC+"] ───"+r+gC+"►"+r+bC2+" v"+r+rC+"0.0.1"+r)
    print(bC+"        │ ")
    print(bC+"        └────┐   ")
    print(bC+"             ├────"+r+r+gC+"► "+r+"["+bC+"01"+r+"]"+gC+"     Backup commands"+r)
    print(bC+"             ├────"+r+r+gC+"► "+r+"["+bC+"02"+r+"]"+gC+"     Network commands"+r)
    print(bC+"             ├────"+r+r+gC+"► "+r+"["+bC+"99"+r+"]"+gC+"     Return to the main page\n"+r)

    while True:
        try:
            print(bC+"┌─("+r+rC+"OmegaDSToolkit"+r+bC+")─["+r+yC+"~"+r+bC+"]─["+r+gC+"UWTools"+r+bC+"]")
            windowsT_mainpage = int(input(bC+"└───"+r+yC+"$ "+r))
            break
        except:
            error()
            input()
            cls()
            windowstools_mainpage()

    if windowsT_mainpage == 1:
        cls()
        windowstools_backup_charging()
    
    elif windowsT_mainpage == 99:
        cls()
        main_page()
    else:
        invalid_option()
        input()
        cls()
        windowstools_mainpage()
        

### Usefull Windows tool  | Backup tool ###
def windowstools_backup_error():        # the function for the error with no respond
    print()
    print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Type y or n "+bC+"]"+r)
    
def windowstools_backup_charging():
    cls()
    print(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Starting the backup tool..."+bC+"]"+r)
    time.sleep(3)
    print(bC+"["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Done"+bC+"]"+r)
    time.sleep(1)
    windowstools_backup()
def windowstools_backup():
    cls()
    print
    print(rC2+"        _______                              ______              __                  "+r)
    print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
    print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
    print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
    print(rC2+"                               |_____|                                      |__|     "+r)
    print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+gC+"►"+r)
    print(bC+"     ╚════════╗"+r)
    print(bC+"              ║"+r+"    A tool for make backup by file or "+r)
    print(bC+"              ║"+r+"          folder with robocopy"+r)
    print(bC+"              ║"+"") 
    print(bC+"              ╟──────"+gC+"►"+bC2+" Created by :"+rC+"  Thomas Pellissier"+bC2+" (© Delta_Society™)"+r)
    print(bC+"              ╟──────"+gC+"►"+bC2+" Version    :"+rC+"  0.0.7"+r)
    print(bC+"              ╟──────"+gC+"►"+bC2+" Codename   : @"+rC+"MyMeepSQL"+r)
    print(bC+"     ╔════════╝"+r)
    print(bC+"     ╚═══════════════════════════════════════════╗"+r)
    print("            Do you want make backup (y/n)"+bC+"        ║"+r)
    print(bC+"     ════════════════════════════════════════════╝"+r)
    print()
    print(bC+"┌─("+rC+"OmegaDSToolkit"+bC+")─["+yC+"~"+bC+"]─["+gC+"OmegaBackup"+bC+"]")
    choiceB = str(input(bC+"└───"+yC+"$ "+r))
    
    if choiceB == "y":
        windowstools_backup_source()
        
    elif choiceB == "n":
        print()
        print(bC+"["+r+rC2+"+"+r+bC+"]"+r+bC+"──["+r+gC+"Exiting backup tool..."+bC+"]"+r)
        time.sleep(2.5)
        windowstools_mainpage()
    else:
        windowstools_backup_error()
        input()
        cls()
        windowstools_backup()

def windowstools_backup_source():
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
        print(bC+"┌─("+rC+"OmegaDSToolkit"+bC+")─["+yC+"~"+bC+"]─["+gC+"OmegaBackup"+bC+"]")
        source = str(input(bC+"└───"+yC+"$ "+r))
        if not source:
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Type your source folder/file "+bC+"]"+r)
            print(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] to continue"+bC+"]"+r)
            input()
            windowstools_backup_source()
        else:
            windowstools_backup_target()
        
def windowstools_backup_target():
        cls()        
        print(rC2+"        _______                              ______              __                  "+r)
        print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
        print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
        print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
        print(rC2+"                               |_____|                                      |__|     "+r)
        print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
        print(bC+"     ╚═══════════════════════════════════════════╗"+r)
        print(gC+"             Where you want to backup it ?"+bC+"       ║"+r)
        print(rC+"           /!\ "+gC+"Type the folder/file path"+rC+" /!\ "+bC+"    ║"+r)
        print(bC+"     ════════════════════════════════════════════╝"+r)
        print()
        print(bC+"┌─("+rC+"OmegaDSToolkit"+bC+")─["+yC+"~"+bC+"]─["+gC+"OmegaBackup"+bC+"]")
        target = str(input(bC+"└───"+yC+"$ "+r))
        if not target:
            print()
            print(bC+"["+r+rC2+"!"+r+bC+"]"+r+bC+"──["+r+gC+"Type your source folder/file "+bC+"]"+r)
            print(bC+"["+r+rC2+"-"+r+bC+"]"+r+bC+"──["+r+gC+"Press [ENTER] to continue"+bC+"]"+r)
            input()
            windowstools_backup_target()
        else:
            windowstools_backup_sure()()
def windowstools_backup_sure(target,source):
        cls()
        print(rC2+"        _______                              ______              __                  "+r)
        print(rC2+"       |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
        print(rC2+"       |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
        print(rC2+"       |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
        print(rC2+"                               |_____|                                      |__|     "+r)
        print(bC+"     ╓────────────────────────────────────────────────────────────────────────────"+r+gC+"►"+r)  
        print(bC+"     ╚═══════════════════════════════════════════╗"+r)
        print(gC+"          Are you sure you want backup (y/n)"+bC+" ║"+r)
        print(bC+"     ╔═══════════════════════════════════════════╝"+r)
        print(bC+"     ╚════╗"+r)
        
        

            

    # print()
    # print("Were you want to copy ?")
    # print(bC+"┌─("+r+rC+"OmegaDSToolkit"+r+bC+")─["+r+yC+"~"+r+bC+"]─["+r+gC+"OmegaBackup"+r+bC+"]")
    # target = input(bC+"└───"+r+yC+"$ "+r)
    # print()
    # print("Backuping...")
    # shutil.copy(folderfile, target)
    

#--------------------------------------------------------------------#


#-Main page----------------------------------------------------------#

def main_page():
    cls()
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+gC+"       _____                   ____  _____ _____         _ _   _ _"  +r)
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+gC+"      |     |_____ ___ ___ ___|    \|   __|_   _|___ ___| | |_|_| |_"  +r)
    print(bC+"        MMMMMMMMMMMMMMMMMNmmmmNNMMMMMMMMMMMMMMMM "+r+gC+"      |  |  |     | -_| . | .'|  |  |__   | | | | . | . | | '_| |  _|"  +r)
    print(bC+"        MMMMMMMMMMMdy+:.```..```.-/shNMMMMMMMMMM "+r+gC+"      |_____|_|_|_|___|_  |__,|____/|_____| |_| |___|___|_|_,_|_|_|"  +r) # Police = rectangle 
    print(bC+"        MMMMMMMNy/``  -ohmNNNNNdy/`  `:smMMMMMMM "+r+gC+"                      |___|"  +r)
    print(bC+"        MMMMMNo.    :dNMMMMMMMMMMMNo`   `/dMMMMM "+r+bC+" ╓──────────────────────────────────────────────────────────────────────────"+gC+"►"  +r)
    print(bC+"        MMMMh.     sMMMMMMMMMMMMMMMMd.    `+NMMM "+r+bC+" ║"  +r)
    print(bC+"        MMMy`     sMMMMMMMMMMMMMMMMMMm`     /MMM "+r+bC+" ║"+r+"     OmegaDSToolkit factory for penetration testing"  +r)
    print(bC+"        MMm`     :MMMMMMMMMMMMMMMMMMMMy      oMM "+r+bC+" ║"  +r)
    print(bC+"        MM-      MMMMMMMMMMMMMMMMMMMMMM+      mM "+r+bC+" ╚════╗"  +r)
    print(bC+"        MM-     `MMMMMMMMMMMMMMMMMMMMMMo      mM "+r+bC+"      ║"  +r)
    print(bC+"        MMo      NMMMMMMMMMMMMMMMMMMMMM/     `MM "+r+bC+"      ╟──────"+gC+"►"+bC2+" Created by :"+rC+" Thomas Pellissier"+bC2+" (© Delta_Society™)"  +r)
    print(bC+"        MMN`     yMMMMMMMMMMMMMMMMMMMMN`     sMM "+r+bC+"      ╟──────"+gC+"►"+bC2+" Version    :"+rC+f" {version}"  +r)
    print(bC+"        MMMh`    .NMMMMMMMMMMMMMMMMMMM+     /MMM "+r+bC+"      ╟────╥─"+gC+"►"+bC2+" Codename   : @"+r+rC+"MyMeepSQL or "+bC2+"@"+bC2+"th300905"  +r)
    print(bC+"        MMMMh.    :NMMMMMMMMMMMMMMMMMs    `oMMMM "+r+bC+"      ║"+bC+"    ╙───────────"+gC+"►"+bC2+rC+" The"+bC2+" seconde"+rC+" codname is alse mine"  +r)
    print(bC+"        MMMMMNo.   -hNMMMMMMMMMMMMMm+   `/dMMMMM "+r+bC+"      ╚════════╗"  +r)
    print(bC+"        NdMMMMMNy/.` -smMMMMMMMMNy/` `:smMMMMMNm "+r+bC+"               ║"+r+"                Developed for linux and windows"  +r)
    print(bC+"        m`hNMMMMMMNdy: `MMMMMMMM+ .shmMMMMMMNm:+ "+r+bC+"               ║"  +r)
    print(bC+'        m  -/+ooooooo+  mMMMMMMM: .ooooooo+/:` o '+r+bC+"               ║"+gC+"               Welcome to the OmegaDSToolkit (ODST)."  +r)
    print(bC+"        N               hMMMMMMM`              o "+r+bC+'               ║'+gC+' The toolkit which includes a set of "penetration testing" tools.'  +r)
    print(bC+"        M               yMMMMMMM               s "+r+bC+"               ║"  +r)
    print(bC+"        MNmmmmmmmmmmmmmmMMMMMMMMmmmmmmmmmmmmmmmM "+r+bC+"               ║"+rC+"       The Omega-DS-Toolkit is a product of Delta_Society™"  +r)
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+bC+"               ║"  +r)
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+bC+"               ║"+r+"                        SELECT AN OPTION"  +r)
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+bC+"               ║"  +r)
    print()
    print("                ["+bC+"01"+r+"]"+gC+"    Information Gathering"  +r)
    print("                ["+bC+"02"+r+"]"+gC+"    Wireless attacks"  +r)
    print("                ["+bC+"03"+r+"]"+gC+"    Useful Windows tools"  +r)
    print("                ["+bC+"99"+r+"]"+gC+"    Exit\n"  +r)
    print("All tools was not finish\n")

    while True:
        try:
            print(bC+"┌─("+rC+"OmegaDSToolkit"+bC+")─["+yC+"~"+bC+"]─["+gC+"Menu"+bC+"]")
            choice = int(input(bC+"└───"+yC+"$ "+r))
            break
        except:
            error()
            input()
            cls()
            main_page()

    if choice == 1:
       informationgathering_mainpage()
    elif choice == 2:
        wireless_mainpage()
    elif choice == 3:
        windowstools_mainpage()
    elif choice == 99:
        exit()
    else:
        invalid_option()
        input()
        cls()
        main_page()

cls()
startbar()

cls()
main_page()    # for show the main page on starts
input()

#--------------------------------------------------------------------#
