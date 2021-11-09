
#-[Metadata]----------------------------------------------------#
#  Filename: DS-ToolBox[v0.1.4#dev]        [Update: 12-10-2021] #
#-[Info]--------------------------------------------------------#
#  DS-ToolBox - A basic toolbox for windows totaly              #
#  Language   - Python3                                         #
#-[Author{s}]---------------------------------------------------#
#  Thomas Pellissier ~ @Meep                                    #
#-[Operating System]--------------------------------------------#
#  Designed for & tested on: Linux                              #
#                          : Windows                            #
#                                                               #
#  Reported working: All Windows version [MS-DOS]               #
#-[Licence]-----------------------------------------------------#
#  GNU General Public License v3.0                              #
#---------------------------------------------------------------#
 

#-Import section-----------------------------------------------------#
import colored
from colored import fg, attr # fg = la couleur de départ // attr = la fin de la couleur, pour pas que tout le texte qui suit sera en couleur
from pythonping import ping     #   https://www.ictshore.com/python/python-ping-tutorial/
import os
clear = lambda: os.system("cls")
from os import chdir as cd


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

def error():
    print()
    print(bC+"["+r+rC+"ERROR"+r+bC+"]"+r+bC+"──["+r+gC+"Choose a option !"+bC+"]"+r)


def fyodort():
    clear()
    print(gC+"      _____           _              "+r)
    print(gC+"     |   __|_ _ ___ _| |___ ___      "+r)
    print(gC+"     |   __| | | . | . | . |  _|     "+r)
    print(gC+"     |__|  |_  |___|___|___|_|       "+r)
    print(gC+"           |___|                     "+r)
    print(bC+"     ╓────────────────────────────"+r+gC+"►"+r)
    print(bC+"     ╟────"+r+" All Fyodor tools ") 
    print(bC+"     ║") 
    print(bC+"     ╟──── ["+r+gC+" Codename "+r+bC+"] ───"+r+gC+"► "+r+bC2+"@"+r+rC+"Meep"+r)
    print(bC+"     ╟──── ["+r+gC+" Version  "+r+bC+"] ───"+r+gC+"► "+r+bC2+"v"+r+rC+"0.0.1"+r) 
    print(bC+"     ╙─────╖"+r)
    print(bC+"           ╟────"+r+r+gC+"► "+r+"["+bC+"01"+r+"]"+gC+"    Nmap"+r)
    print(bC+"           ╟────"+r+r+gC+"► "+r+"["+bC+"98"+r+"]"+gC+"    Return to the Vulnerability Analysis main page"+r)
    print(bC+"           ╟────"+r+r+gC+"► "+r+"["+bC+"99"+r+"]"+gC+"    Return to the main page\n"+r)    
    boucle = False
    while (not boucle):
        try:
            print(bC+"┌─("+r+rC+"Omega-DS"+r+bC+")─["+r+yC+"~"+r+bC+"]─["+r+gC+"Vulnerability Analysis"+r+bC+"]")
            fyodor_mainpage = int(input(bC+"└───"+r+yC+"$ "+r))
            break
        except:
            error()
            input()
            clear()
            fyodort()
            
    if fyodor_mainpage == 98:
        clear()
        informationgathering()
        
    elif fyodor_mainpage == 99:
        clear()
        main_page()

def informationgathering():
    clear() 
    print(rC2+"     ____   ____      .__                                    ___.    .__ .__   .__   __               "+r)
    print(rC2+"     \   \ /   /__ __ |  |    ____     ____  _______  _____  \_ |__  |__||  |  |__|_/  |_  ___.__.    "+r)
    print(rC2+"      \   Y   /|  |  \|  |   /    \  _/ __ \ \_  __ \ \__  \  | __ \ |  ||  |  |  |\   __\<   |  |    "+r)
    print(rC2+"       \     / |  |  /|  |__|   |  \ \  ___/  |  | \/  / __ \_| \_\ \|  ||  |__|  | |  |   \___  |    "+r)
    print(rC2+"        \___/  |____/ |____/|___|  /  \___  > |__|    (____  /|___  /|__||____/|__| |__|   / ____|    "+r)
    print(rC2+"                                 \/       \/               \/     \/                       \/         "+r)
    print(bC+"     <===========================================================================================>"+r)
    print(rC2+"                    _____                   .__                  .__                               "+r)
    print(rC2+"                   /  _  \    ____  _____   |  |  ___.__.  ______|__|  ______                      "+r)
    print(rC2+"                  /  /_\  \  /    \ \__  \  |  | <   |  | /  ___/|  | /  ___/                      "+r)
    print(rC2+"                 /    |    \|   |  \ / __ \_|  |__\___  | \___ \ |  | \___ \                       "+r)
    print(rC2+"                 \____|__  /|___|  /(____  /|____// ____|/____  >|__|/____  >                      "+r)
    print(rC2+"                         \/      \/      \/       \/          \/          \/                       "+r)
    print(bC+"                 <==========================================================>\n"+r)
    print("                ["+bC+"01"+r+"]"+gC+"    Fyodor tools"+r)
    print("                ["+bC+"02"+r+"]"+gC+"    Payload + Listener"+r)
    print("                ["+bC+"99"+r+"]"+gC+"    Return to the main page\n"+r)
    print("Not finish\n")
    
    boucle = False
    while (not boucle):
        try:
            print(bC+"┌─("+r+rC+"Omega-DS"+r+bC+")─["+r+yC+"~"+r+bC+"]─["+r+gC+"Vulnerability Analysis"+r+bC+"]")
            informationgathering_mainpage = int(input(bC+"└───"+r+yC+"$ "+r))
            break
        except:
            error()
            input()
            clear()
            informationgathering()

    if informationgathering_mainpage == 1:
        fyodort()
    elif informationgathering_mainpage == 99:
        clear()
        main_page()

def windows_tools_backup():
    print(rC2+"      _______                              ______              __                  "+r)
    print(rC2+"     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  "+r)
    print(rC2+"     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  "+r)
    print(rC2+"     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  "+r)
    print(rC2+"                             |_____|                                      |__|     "+r)


def windows_tools_mainpage():
    clear()
    print(rC2+"      _____ _ _ _ _____         _      "+r)
    print(rC2+"     |  |  | | | |_   _|___ ___| |___  "+r)
    print(rC2+"     |  |  | | | | | | | . | . | |_ -| "+r)
    print(rC2+"     |_____|_____| |_| |___|___|_|___| "+r)
    print(bC+"     ┌──────────────────────────────────"+r+gC+"►"+r)
    print(bC+"     ├─────►"+r+" UsefulWindowsTools")
    print(bC+"     │    ")
    print(bC+"     ├──── ["+r+gC+"  Codename  "+r+bC+"] ───"+r+gC+"► "+r+bC2+"@"+r+rC+"Meep")
    print(bC+"     ├──── ["+r+gC+"  Version   "+r+bC+"] ───"+r+gC+"► "+r+bC2+"v"+r+rC+"0.0.1"+r)
    print(bC+"     └────┐   ")
    print(bC+"          ├────"+r+r+gC+"► "+r+"["+bC+"01"+r+"]"+gC+"     Backup commands"+r)
    print(bC+"          ├────"+r+r+gC+"► "+r+"["+bC+"02"+r+"]"+gC+"     Network commands"+r)
    print(bC+"          ├────"+r+r+gC+"► "+r+"["+bC+"99"+r+"]"+gC+"     Return to the main page\n"+r)
    print("Not finish\n")

    boucle = False
    while (not boucle):
        try:
            print(bC+"┌─("+r+rC+"Omega-DS"+r+bC+")─["+r+yC+"~"+r+bC+"]─["+r+gC+"UWTools"+r+bC+"]")
            windowsT_mainpage = int(input(bC+"└───"+r+yC+"$ "+r))
            break
        except:
            error()
            input()
            clear()
            windows_tools_mainpage()

    if windowsT_mainpage == 1:
        clear()
        windows_tools_backup()
    
    elif windowsT_mainpage == 99:
        clear()
        main_page()



#--------------------------------------------------------------------#

#-Main page----------------------------------------------------------#

def main_page():
    clear()
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r)
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r)
    print(bC+"        MMMMMMMMMMMMMMMMMNmmmmNNMMMMMMMMMMMMMMMM "+r)
    print(bC+"        MMMMMMMMMMMdy+:.```..```.-/shNMMMMMMMMMM "+r)
    print(bC+"        MMMMMMMNy/``  -ohmNNNNNdy/`  `:smMMMMMMM "+r)
    print(bC+"        MMMMMNo.    :dNMMMMMMMMMMMNo`   `/dMMMMM "+r+"       _____                   ____  _____ _____         _ _   _ _   ")
    print(bC+"        MMMMh.     sMMMMMMMMMMMMMMMMd.    `+NMMM "+r+"      |     |_____ ___ ___ ___|    \|   __|_   _|___ ___| | |_|_| |_  ")
    print(bC+"        MMMy`     sMMMMMMMMMMMMMMMMMMm`     /MMM "+r+"      |  |  |     | -_| . | .'|  |  |__   | | | | . | . | | '_| |  _| ")    
    print(bC+"        MMm`     :MMMMMMMMMMMMMMMMMMMMy      oMM "+r+"      |_____|_|_|_|___|_  |__,|____/|_____| |_| |___|___|_|_,_|_|_|  ") # Police = rectangle
    print(bC+"        MM-      MMMMMMMMMMMMMMMMMMMMMM+      mM "+r+"                      |___|                    ")
    print(bC+"        MM-     `MMMMMMMMMMMMMMMMMMMMMMo      mM "+r+" __________________________________________________________________________ ")
    print(bC+"        MMo      NMMMMMMMMMMMMMMMMMMMMM/     `MM "+r+" ["+bC+"##"+r+"]          OmegaDSToolkit factory for penetration testing          ["+bC+"##"+r+"] ")
    print(bC+"        MMN`     yMMMMMMMMMMMMMMMMMMMMN`     sMM "+r+" ["+bC+"##"+r+"]"+bC2+"          Created by:"+r+rC+" Thomas Pellissier (© Delta_Society™)"+r+"        ["+bC+"##"+r+"] ")
    print(bC+"        MMMh`    .NMMMMMMMMMMMMMMMMMMM+     /MMM "+r+" ["+bC+"##"+r+"]"+bC2+"          Version:"+r+rC+"    0.0.1"+r+"                                       ["+bC+"##"+r+"] ")
    print(bC+"        MMMMh.    :NMMMMMMMMMMMMMMMMMs    `oMMMM "+r+" ["+bC+"##"+r+"]"+bC2+"          Codename:   @"+r+rC+"MyMeepSQL or "+r+bC2+"@"+r+rC+"th300905"+r+"                     SS["+bC+"##"+r+"] ")
    print(bC+"        MMMMMNo.   -hNMMMMMMMMMMMMMm+   `/dMMMMM "+r+" ["+bC+"##"+r+"]          Designed for & tested on Linux / Windows                ["+bC+"##"+r+"] ")
    print(bC+"        NdMMMMMNy/.` -smMMMMMMMMNy/` `:smMMMMMNm "+r+" ["+bC+"##"+r+"]                                                                  ["+bC+"##"+r+"] ")
    print(bC+"        m`hNMMMMMMNdy: `MMMMMMMM+ .shmMMMMMMNm:+ "+r+" ["+bC+"##"+r+"]"+gC+"              Welcome to the OmegaDSToolkit (ODST)."+r+"               ["+bC+"##"+r+"] ")
    print(bC+'        m  -/+ooooooo+  mMMMMMMM: .ooooooo+/:` o '+r+' ['+bC+'##'+r+']'+gC+' The toolkit which includes a set of "penetration testing" tools.'+r+' ['+bC+'##'+r+'] ')
    print(bC+"        N               hMMMMMMM`              o "+r+" ["+bC+"##"+r+"]                                                                  ["+bC+"##"+r+"] ")
    print(bC+"        M               yMMMMMMM               s "+r+" ["+bC+"##"+r+"]"+gC+"        The Omega-DS-Toolkit is a product of Delta_Society™"+r+"       ["+bC+"##"+r+"] ")
    print(bC+"        MNmmmmmmmmmmmmmmMMMMMMMMmmmmmmmmmmmmmmmM "+r+" ["+bC+"##"+r+"]                                                                  ["+bC+"##"+r+"] ")
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+" ["+bC+"##"+r+"]                         SELECT AN OPTION:                        ["+bC+"##"+r+"] ")
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+" ["+bC+"##"+r+"] .________________________________________________________________["+bC+"##"+r+"] ")
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+" \_.----------------------------------------------------------------------/ ")
    print()
    print("                ["+bC+"01"+r+"]"+gC+"    Information Gathering"+r)
    print("                ["+bC+"02"+r+"]"+gC+"    Wireless attacks"+r)
    print("                ["+bC+"03"+r+"]"+gC+"    Windows tools"+r)
    print("                ["+bC+"99"+r+"]"+gC+"    Exit\n "+r)
    print("Not finish\n")

    boucle = False
    while ( not boucle ):
        try:
            print(bC+"┌─("+r+rC+"Omega-DS"+r+bC+")─["+r+yC+"~"+r+bC+"]─["+r+gC+"Menu"+r+bC+"]")
            choice = int(input(bC+"└───"+r+yC+"$ "+r))
            break
        except:
            error()
            input()
            clear()
            main_page()

    if choice == 1:
       informationgathering()

    elif choice == 3:
        windows_tools_mainpage()

clear()
main_page()    # for the staring page





input()
#--------------------------------------------------------------------#


    
