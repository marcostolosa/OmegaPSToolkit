
 #-Metadata----------------------------------------------------#
 #  Filename: DS-ToolBox[v0.1.4#dev]      [Update: 12-10-2021] #
 #-Info--------------------------------------------------------#
 #  DS-ToolBox - A basic toolbox for windows totaly            #
 #  Language   - Python3                                       #
 #-Author[s}---------------------------------------------------#
 #  Thomas Pellissier ~ @$_M33p                                #
 #-Operating System--------------------------------------------#
 #  Designed for & tested on: Windows                          #
 #                                                             #
 #  Reported working : All Windows version [MS-DOS]            #
 #-Licence-----------------------------------------------------#
 #  GNU General Public License v3.0                            #
 #-------------------------------------------------------------#
 

#-Import section-----------------------------------------------------#
import colored
from colored import fg, bg, attr



import os
clear = lambda: os.system("cls")
import msvcrt as m
def wait():
    m.getch()

#--------------------------------------------------------------------#


#-Colors section-----------------------------------------------------#
bC = fg('#1d89f3')
bC2 = fg('#0B4D8F')
rC = fg('#F44336')
gC = fg('#39CC3F')


r = attr('reset')
#--------------------------------------------------------------------#

#-Fonctions----------------------------------------------------------#
def error():
    print(bC+"["+r+rC+"ERROR"+r+bC+"]"+r+bC+"──["+r+gC+"Choose a option !"+bC+"]"+r)

def fyodor_nmap():
    clear()
    print("        _  __                     ") # police = smslant
    print("       / |/ /  __ _  ___ _   ___  ")
    print("      /    /  /  ' \/ _ `/  / _ \ ")
    print("     /_/|_/  /_/_/_/\_,_/  / .__/ ")
    print("                          /_/     ")


def vulnerabilityanalysis():
    clear() 

    print("                [01]    Fyodor tools")
    print("                [02]    Network commands")
    print("                [99]    Return to the main page\n")
    print("Not finish\n")
    
    boucle = False
    while (not boucle):
        try:
            print(bC+"┌─["+r+rC+"Omega-DS"+r+bC+"]──["+r+gC+"Menu"+r+bC+"]")
            fyodor_mainpage = int(input(bC+"└─────► "+r))
            break
        except:
            error()
            input()
            clear()
            vulnerabilityanalysis()

    if fyodor_mainpage == 1:
        fyodor_nmap()
    elif fyodor_mainpage == 99:
        clear()
        main_page()

def windows_tools_backup():
    print("     ________      _____   ___________   ________    _____            __________                  __                    ")
    print("     \_____  \    /     \  \_   _____/  /  _____/   /  _  \           \______   \_____     ____  |  | __ __ __ ______   ")
    print("      /   |   \  /  \ /  \  |    __)_  /   \  ___  /  /_\  \   ______  |    |  _/\__  \  _/ ___\ |  |/ /|  |  \\____ \  ")
    print("     /    |    \/    Y    \ |        \ \    \_\  \/    |    \ /_____/  |    |   \ / __ \_\  \___ |    < |  |  /|  |_> > ")
    print("     \_______  /\____|__  //_______  /  \______  /\____|__  /          |______  /(____  / \___  >|__|_ \|____/ |   __/  ")
    print("             \/         \/         \/          \/         \/                  \/      \/      \/      \/       |__|     ")


def windows_tools_mainpage():
    clear()
    print("      _____ _ _ _ _____         _      ")
    print("     |  |  | | | |_   _|___ ___| |___  ")
    print("     |  |  | | | | | | | . | . | |_ -| ")
    print("     |_____|_____| |_| |___|___|_|___| ")
    print("    <--------------------------------->")
    print("                 UWTools ")
    print("                 ")
    print()
    print("                [01]    Backup commands")
    print("                [02]    Network commands")
    print("                [99]    Return to the main page\n")
    print("Not finish\n")

    boucle = False
    while (not boucle):
        try:
            print(bC+"┌─["+r+rC+"Omega-DS"+r+bC+"]──["+r+gC+"Menu"+r+bC+"]")
            windowsT_mainpage = int(input(bC+"└─────► "+r))
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

    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r)
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r)
    print(bC+"        MMMMMMMMMMMMMMMMMNmmmmNNMMMMMMMMMMMMMMMM "+r)
    print(bC+"        MMMMMMMMMMMdy+:.```..```.-/shNMMMMMMMMMM "+r)
    print(bC+"        MMMMMMMNy/``  -ohmNNNNNdy/`  `:smMMMMMMM "+r)
    print(bC+"        MMMMMNo.    :dNMMMMMMMMMMMNo`   `/dMMMMM "+r+"                    _____                   ____  _____  ")
    print(bC+"        MMMMh.     sMMMMMMMMMMMMMMMMd.    `+NMMM "+r+"                   |     |_____ ___ ___ ___|    \|   __| ")
    print(bC+"        MMMy`     sMMMMMMMMMMMMMMMMMMm`     /MMM "+r+"                   |  |  |     | -_| . | .'|  |  |__   | ")
    print(bC+"        MMm`     :MMMMMMMMMMMMMMMMMMMMy      oMM "+r+"                   |_____|_|_|_|___|_  |__,|____/|_____| ")
    print(bC+"        MM-      MMMMMMMMMMMMMMMMMMMMMM+      mM "+r+"                                   |___|                 ")
    print(bC+"        MM-     `MMMMMMMMMMMMMMMMMMMMMMo      mM "+r+" __________________________________________________________________________ ")
    print(bC+"        MMo      NMMMMMMMMMMMMMMMMMMMMM/     `MM "+r+" ["+bC+"##"+r+"]         OmegaDS Toolkit factory for penetration testing          ["+bC+"##"+r+"] ")
    print(bC+"        MMN`     yMMMMMMMMMMMMMMMMMMMMN`     sMM "+r+" ["+bC+"##"+r+"]"+bC2+"        Created by:"+r+rC+" Thomas Pellissier (© Delta_Society™)"+r+"          ["+bC+"##"+r+"] ")
    print(bC+"        MMMh`    .NMMMMMMMMMMMMMMMMMMM+     /MMM "+r+" ["+bC+"##"+r+"]"+bC2+"                          Version:"+r+rC+" 0.0.1"+r+"                          ["+bC+"##"+r+"] ")
    print(bC+"        MMMMh.    :NMMMMMMMMMMMMMMMMMs    `oMMMM "+r+" ["+bC+"##"+r+"]"+bC2+"                  Codename:"+r+rC+" 'Meep' or 'th300905'"+r+"                  ["+bC+"##"+r+"] ")
    print(bC+"        MMMMMNo.   -hNMMMMMMMMMMMMMm+   `/dMMMMM "+r+" ["+bC+"##"+r+"]                 Designed for & tested on Windows                 ["+bC+"##"+r+"] ")
    print(bC+"        NdMMMMMNy/.` -smMMMMMMMMNy/` `:smMMMMMNm "+r+" ["+bC+"##"+r+"]                                                                  ["+bC+"##"+r+"] ")
    print(bC+"        m`hNMMMMMMNdy: `MMMMMMMM+ .shmMMMMMMNm:+ "+r+" ["+bC+"##"+r+"]"+gC+"             Welcome to the Omega-DS-Toolkit (ODST)."+r+"              ["+bC+"##"+r+"] ")
    print(bC+'        m  -/+ooooooo+  mMMMMMMM: .ooooooo+/:` o '+r+' ['+bC+'##'+r+']'+gC+' The toolkit which includes a set of "penetration testing" tools.'+r+' ['+bC+'##'+r+'] ')
    print(bC+"        N               hMMMMMMM`              o "+r+" ["+bC+"##"+r+"]                                                                  ["+bC+"##"+r+"] ")
    print(bC+"        M               yMMMMMMM               s "+r+" ["+bC+"##"+r+"]"+gC+"        The Omega-DS-Toolkit is a product of Delta_Society™"+r+"       ["+bC+"##"+r+"] ")
    print(bC+"        MNmmmmmmmmmmmmmmMMMMMMMMmmmmmmmmmmmmmmmM "+r+" ["+bC+"##"+r+"]                                                                  ["+bC+"##"+r+"] ")
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+" ["+bC+"##"+r+"]                         SELECT AN OPTION:                        ["+bC+"##"+r+"] ")
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+" ["+bC+"##"+r+"] .________________________________________________________________["+bC+"##"+r+"] ")
    print(bC+"        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "+r+" \_.----------------------------------------------------------------------/ ")
    print()
    print("                ["+bC+"01"+r+"]"+gC+"    Vulnerability Analysis"+r)
    print("                ["+bC+"02"+r+"]"+gC+"    Wireless attacks"+r)
    print("                ["+bC+"03"+r+"]"+gC+"    Windows tools"+r)
    print("                ["+bC+"99"+r+"]"+gC+"    Exit\n "+r)
    print("Not finish\n")

    boucle = False
    while ( not boucle ):
        try:
            print(bC+"┌─["+r+rC+"Omega-DS"+r+bC+"]──["+r+gC+"Menu"+r+bC+"]")
            choice = int(input(bC+"└─────► "+r))
            break
        except:
            error()
            input()
            clear()
            main_page()

    if choice == 1:
       vulnerabilityanalysis()

    elif choice == 3:
        windows_tools_mainpage()

clear()
main_page()    # for the staring page





input()
#--------------------------------------------------------------------#


    