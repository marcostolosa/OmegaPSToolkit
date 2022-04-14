#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstconsole.py                [Update: 2022-04-11 | 12:57 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  OmegaPSTookit ~ A massive penetration testing toolkit for penteser       #
#  Language  ~  Python3                                                     #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright (C) 2022 MyMeepSQL - © PSociety™                               #
#---[Operating System]------------------------------------------------------#
#  Developed for linux                                                      #
#---[Licence]---------------------------------------------------------------#
#  GNU General Public License v3.0                                          #
#  -------------------------------                                          #
#                                                                           #
#  This program is free software; you can redistribute it and/or modify     #
#  it under the terms of the GNU General Public License as published by     #
#  the Free Software Foundation; either version 2 of the License, or        #
#  (at your option) any later version.                                      #
#                                                                           #
#  This program is distributed in the hope that it will be useful,          #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#  GNU General Public License for more details.                             #
#                                                                           #
#  You should have received a copy of the GNU General Public License along  #
#  with this program; if not, write to the Free Software Foundation, Inc.,  #
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.              #
#---------------------------------------------------------------------------#

# Import section
import os, sys
from time import sleep
####


            

# Custom imports
try:
    from opstversions import *
    from opstfunctions import *
    from opstcolors import *
except ModuleNotFoundError:
    print()
    criticalmsg = f"{B}[{R}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run 'sudo opstsetup install' command for install it.\n"
    exit(criticalmsg)
except ImportError:
    print()
    criticalmsg = f"{B}[{R}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run 'sudo opstsetup install' command for install it.\n"
    exit(criticalmsg)
except NameError:
    print()
    criticalmsg = f"{B}[{R}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run 'sudo opstsetup install' command for install it.\n"
    exit(criticalmsg)
####


#-Check module is installed---------------------------------------------------------------------#
try:
    # Check if the user run OPST with root privilege
    if os.getuid() != 0:    
        permerror =f"""
{R}[!]{W}    OPSTConsole could be run as the 'root' user or with 'sudo'
       Re-run the 'opstconsol   e' with 'sudo' or with the 'root' user
       Run \"sudo opstconsole\"
"""
        sys.exit(permerror)
except AttributeError:
    non_linux()
else:
    cls()
    # Checking if modules are installed
    sys.stdout.write("\x1b]2;Checking if all modules are [OK]\x07")
    try:
        print(f"{white}{underscore}Checking if the current modules of OPST are installed...{W}")
        print()
        sleep(1.5)
        import itertools
        import progress
        import colored
        import shutil
        import time
        import platform
        import shlex
        import textwrap
        from collections import namedtuple
        from builtins import format
        print(f"{B}[{G}OK{B}]{GR}         All modules are install !{W}")
        try:
            print(f"{B}[{G}-{B}]{GR}          Checking for Internet connexion... (Press CTRL + C to skip){W}")
            sleep(1)
            if connexion() == True:
                internetstatus = f"{G}Connected{W}"
                print(f"{B}[{G}!{B}]{GR}          Internet status : {G}Connected{W}.")
            else:
                internetstatus = f"{R}Not connected{W}"
                print(f"{B}[{G}!{B}]{GR}          Internet status : {R}Not connected{W}.")
            print()
        except KeyboardInterrupt:
            print(f"{B}\n[{R}*{B}]{GR}         CTRL + C detected, skipping the Internet checker...{W}")
            internetstatus = (f"{yC}?{r}")
            pass
        print(f"{B}[{R}>>{B}]{GR}         Launching of OPST...{W}")
        sys.stdout.write("\x1b]2;OmegaPSToolkit | A massive penetration testing toolkit.\x07")  # Title page
        sleep(1)
    except KeyboardInterrupt:
        print()
        abortmsg = f"{B}[{R}ERROR{B}]{GR}      User aborted\n"
        exit(abortmsg)
    except EOFError:
        print()
        abortmsg = f"{B}[{R}ERROR{B}]{GR}      User aborted\n"
        exit(abortmsg)
    except ModuleNotFoundError:
        print()
        criticalmsg = f"{B}[{R}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run 'sudo opstsetup install' command for install it.\n"
        exit(criticalmsg)
    except ImportError:
        print()
        criticalmsg = f"{B}[{R}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run 'sudo opstsetup install' command for install it.\n"
        exit(criticalmsg)
    except NameError:
        print()
        criticalmsg = f"{B}[{R}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run 'sudo opstsetup install' command for install it.\n"
        exit(criticalmsg)
#-END-OF-MODULES-CHECKER----------------------------------------------------------------------------------------------------------------------------#

#-Main-tool----------------------------------------------------------#
try:
    def invalid_option():
        print(f"{bC}[{rC2}!{bC}]─[{gC}'{command}' is not a valid command{bC}]{r}")  # if the user enter a bad option (if the option type by the user are not recognized)
        input(f"{bC}[{rC2}!{bC}]─[{gC}Press [ENTER] key to continue{bC}]{r}")       #

    def cli_invalid_command():
        print(f"{bC}[{rC2}!{bC}]─[{gC}{command}' is not a valid command{bC}]{r}")   # if the user enter a bad option (if the option type by the user are not recognized)


### Wireless Atack | main page
    def wireless_mainpage():
        cls()
        print(f"{gC}         ________ __              __                         __                __        {r}")
        print(f"{gC}        |  |  |  |__|.----.-----.|  |.-----.-----.-----.    |  |_.-----.-----.|  |.-----.{r}")
        print(f"{gC}        |  |  |  |  ||   _|  -__||  ||  -__|__ --|__ --|    |   _|  _  |  _  ||  ||__ --|{r}")
        print(f"{gC}        |________|__||__| |_____||__||_____|_____|_____|    |____|_____|_____||__||_____|{r}")
        print(f"{bC}     ╓────────────────────────────────────────────────────────────────────────────────{gC}►{r}")

        ##          coming soon


#---Information Gathering--------------------------------------------#

### Information Gathering | main page ###
    def informationgathering_mainpage():
        cls() 
        print(f"""
{rC2}      _______         ___                             __   __                    {r}
{rC2}     |_     _|.-----.'  _|.-----.----.--------.---.-.|  |_|__|.-----.-----.      {r}
{rC2}      _|   |_ |     |   _||  _  |   _|        |  _  ||   _|  ||  _  |     |      {r}
{rC2}     |_______||__|__|__|  |_____|__| |__|__|__|___._||____|__||_____|__|__|      {r}
{bC}   ◄═════════════════════════════════════════════════════════════════════════►    {r}
{rC2}          _______         __   __                __ {r}
{rC2}         |     __|.---.-.|  |_|  |--.-----.----.|__|.-----.-----.                {r}
{rC2}         |    |  ||  _  ||   _|     |  -__|   _||  ||     |  _  |                {r}
{rC2}         |_______||___._||____|__|__|_____|__|  |__||__|__|___  |                {r}
{bC}   ╔══════════════════════════════════════════════════════{rC2}|_____|{bC}══►{r}
{bC}   ╚═════╗{r}
{bC}         ║{r}   In this category you will find tools to collect information,
{bC}         ║{r}              such as port scan, SQL injections etc
{bC}         ║{r}
{bC}         ╟──── [{gC}  Made by   {bC}] ───{gC}► {rC}Thomas Pellissier{bC2} (from © PSociety™){r}
{bC}         ╟──── [{gC}  Codename  {bC}] ───{gC}► {bC2}@{r}{rC}MyMeepSQL")
{bC}         ╟──── [{gC}  Version   {bC}] ───{gC}► {bC2}v{rC}0.0.1{r})
{bC}         ║{r}
{bC}         ╟────{gC}► {r}[{bC}1{r}]{gC}    Scan{r}
{bC}         ╟────{gC}► {r}[{bC}o{r}]{gC}    Return to the{rC} OmegaPSToolkit{gC} main page{r}
{bC}         ╙────{gC}► {r}[{bC}exit{r}]{gC} Exit the opstconsole\n{r}
{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/Information_Gathering{bC}]{r}""")
        global commands
        command = str(input(f"{bC}└╼{rC}$ {r}"))

        if command == "1":
            informationgathering_scan_mainpage()
        elif command == "x":
            cls()
            main_page()
        elif not command:
            error()
            cls()
            informationgathering_mainpage()
        else:
            invalid_option()
            cls()
            informationgathering_mainpage()

### Information Gathering | Scan tools ### 
    def informationgathering_scan_mainpage():
        cls()
        print(f"{gC}       _____             _____         _               {r}")
        print(f"{gC}      |   __|___ ___ ___|_   _|___ ___| |___           {r}")
        print(f"{gC}      |__   |  _| .'|   | | | | . | . | |_ -|          {r}")
        print(f"{gC}      |_____|___|__,|_|_| |_| |___|___|_|___|          {r}")
        print(f"{gC}     ╓────────────────────────────────────────{gC}►{r}")
        print(f"{gC}     ╙────╖")
        print(f"{gC}          ║{r}   Some tools for scanning target")
        print(f"{gC}          ║{r}")
        print(f"{gC}          ╟──────{gC}►{r}{bC2} Created by :: {r}{rC}Thomas Pellissier{bC2} (from © PSociety™){r}")
        print(f"{gC}          ╟──────{gC}►{r}{bC2} Codename   :: @{r}{rC}MyMeepSQL{r}")
        print(f"{gC}          ╟──────{gC}►{r}{bC2} Version    :: v{r}{rC}0.0.1{r}")
        print(f"{gC}          ║{r}")
        print(f"{gC}          ╙─────╖{r}")
        print(f"{gC}                ╟────{gC}► {r}[{bC}1{r}]{gC}    Nmap{r}")
        print(f"{gC}                ╟────{gC}► {r}[{bC}2{r}]{gC}    SQLMap{r}")
        print(f"{gC}                ╟────{gC}► {r}[{bC}x{r}]{gC}    Return to the{rC} Information Gathering{gC} main page{r}")
        print(f"{gC}                ╟────{gC}► {r}[{bC}o{r}]{gC}    Return to the{rC} OmegaPSToolkit{gC} main page{r}")
        print(f"{gC}                ╙────{gC}► {r}[{bC}exit{r}]{gC} Exit the opstconsole\n{r}")
        print(f"{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/Information_Gathering/ScanTools{bC}]{r}")
        global command
        command = str(input(f"{bC}└╼{rC}$ {r}"))

        if command == "2":
            informationgathering_scan_sqlmap()

        # if scan_mainpage_ == 2:
            # informationgathering_sqlmap()

        elif command == "x":
            cls()
            informationgathering_scan_mainpage()
        elif command == "o":
            cls()
            main_page()
        elif command == "exit":
            exitodst()
        elif not command:
            error()
            cls()
            informationgathering_scan_mainpage()
        else:
            invalid_option()
            cls()
            informationgathering_scan_mainpage()

    def informationgathering_scan_sqlmap():
        sqlmapdir="Tools/sqlmapmaster"
        while True:
            os.chdir(sqlmapdir)
            prompt_for_command = f"{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/Information_Gathering/ScanTools/sqlmap{bC}]{r}"
            user_input = input(prompt_for_command + f"\n{bC}└╼{rC}$ {r}")
            command = user_input
            if not command:
                print()
                user_input
            # elif "connexionstatus" == command:
            #     print(f"{B}[-]{GR}    Checking for Internet connexion...{W}")
            #     sleep(1)
            #     if connexion() == True:
            #         internetstatus = f"{G}Connected{W}"
            #         print(f"{G}[+]{GR}    Internet status : {G}Connected{W}.")
            #     else:
            #         internetstatus = f"{R}Not connected{W}"
            #         print(f"{R}[!]{GR}    Internet status : {R}Not connected{W}.")
            #     print()
            
            elif command:
                os.system(command)
            elif "clear" == command:
                cls()
                informationgathering_scan_sqlmap()
            elif "info" == command:
                cli_infomsg()
            elif "leave" == command:
                print(f"{G}[-]{W}   Exiting CLI mode...")
                sleep(0.5)
                informationgathering_scan_mainpage()
            elif "exit" == command:
                exitodst()
            else:
                unknown_command = f"{R}\n[!]{W}   '{command}' is not recognized as an internal or external command.\n"
                print(unknown_command)
#---End of Information Gathering-------------------------------------#

#---Usefull tool-----------------------------------------------------#
### Usefull Windows tool | main page ###
    def usefulltools_mainpage():
        cls()
        print(f"""
{rC2}       _____ _____         _     {r}
{rC2}      |  |  |_   _|___ ___| |___ {r}
{rC2}      |  |  | | | | . | . | |_ -|{r}
{rC2}      |_____| |_| |___|___|_|___|{r}
   {bC}╔═════════════════════════════{gC}►{r}
   {bC}╚════╗
        {bC}║{r}   UsefulTools include several useful
        {bC}║{r}        tools like Windows tools
        {bC}║
        {bC}╟──── [{gC}  Made by   {bC}] ───{gC}►{rC} Thomas Pellissier{bC2} (from © PSociety™){r}
        {bC}╟──── [{gC}  Codename  {bC}] ───{gC}►{bC2} @{rC}MyMeepSQL{r}
        {bC}╟──── [{gC}  Version   {bC}] ───{gC}►{bC2} v{rC}0.1.0{r}
        {bC}║
        {bC}╟────{gC}► {r}[{bC}1{r}]{gC}     Backup tool{r}
        {bC}╟────{gC}► {r}[{bC}2{r}]{gC}     Network commands{r}
        {bC}╟────{gC}► {r}[{bC}o{r}]{gC}     Return to the{rC} OmegaPSToolkit{gC} main page{r}
        {bC}╙────{gC}► {r}[{bC}exit{r}]{gC}  Exit the opstconsole\n{r}
{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools{bC}]{r}""")
        global command
        command = str(input(f"{bC}└╼{rC}$ {r}"))

        if command == "1":
            usefulltools_backup_main()
        if command == "2":
            usefulltools_networkC_main_page()
        elif command == "o":
            main_page()
        elif not command:
            error()
            cls()
            usefulltools_mainpage()
        elif command == "exit":
            exitodst()
        else:
            invalid_option()
            cls()
            usefulltools_mainpage()
            
### Usefull Windows tool  | Network commands ###
    def usefulltools_networkC_main_page():
        while connexion == False:
            connexion()
        cls()
        print(f"""
{rC2}        _______         __                        __     ______                                         __        {r}
{rC2}       |    |  |.-----.|  |_.--.--.--.-----.----.|  |--.|      |.-----.--------.--------.---.-.-----.--|  |.-----.{r}
{rC2}       |       ||  -__||   _|  |  |  |  _  |   _||    < |   ---||  _  |        |        |  _  |     |  _  ||__ --|{r}
{rC2}       |__|____||_____||____|________|_____|__|  |__|__||______||_____|__|__|__|__|__|__|___._|__|__|_____||_____|{r}
{bC}   ╓───────────────────────────────────────────────────────────────────────────────────────────────────────────────{gC}►{r}
{bC}   ╚════╗{r}
{bC}        ║{r}    Some network commands{r}
{bC}        ║{r}
{bC}        ╟──────{gC}►{bC2} Created by       :: {rC}Thomas Pellissier{bC2} (from © PSociety™){r}
{bC}        ╟──────{gC}►{bC2} Codename         :: @{rC}MyMeepSQL{r}
{bC}        ╟──────{gC}►{bC2} Version          :: v{rC}0.1.9{r}
{bC}        ╟──────{gC}►{bC2} Internet Status  :: {rC}{internetstatus}{r}
{bC}        ║{r}
{bC}        ╚══════╗{r}
{bC}               ╟────{gC}► {r}[{bC}1{r}]{gC}     Ping
{bC}               ╟────{gC}► {r}[{bC}2{r}]{gC}     NSLookup
{bC}               ╟────{gC}► {r}[{bC}3{r}]{gC}     Traceroute
{bC}               ╟────{gC}► {r}[{bC}4{r}]{gC}     Netstat
{bC}               ╟────{gC}► {r}[{bC}5{r}]{gC}     Whois
{bC}               ╟────{gC}► {r}[{bC}x{r}]{gC}     Return to the{rC} UTools{gC} main page{r}
{bC}               ╟────{gC}► {r}[{bC}o{r}]{gC}     Return to the{rC} OmegaPSToolkit{gC} main page{r}
{bC}               ╙────{gC}► {r}[{bC}exit{r}]{gC}  Exit the opstconsole\n{r}
{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/NetworkCommands{bC}]{r}""")
        global command
        command = str(input(f"{bC}└╼{rC}$ {r}"))

        if command == "1":
            usefulltools_networkC_ping()
        elif command == "2":
            usefulltools_networkC_nslookup()
        elif command == "3":
            usefulltools_networkC_traceroute()
        elif command == "4":
            usefulltools_networkC_netstat()
        elif command == "5":
            usefulltools_networkC_whois()
        elif command == "x":
            usefulltools_mainpage()
        elif command == "o":
            main_page()
        elif command == "exit":
            exitodst()
        elif not command:
            error()
            cls()
            usefulltools_networkC_main_page()
        else:
            invalid_option()
            cls()
            usefulltools_networkC_main_page()

    def usefulltools_networkC_netstat():
        cls()
        print(f"""
{rC2}       _______         __          __          __   {r}
{rC2}      |    |  |.-----.|  |_.-----.|  |_.---.-.|  |_ {r}
{rC2}      |       ||  -__||   _|__ --||   _|  _  ||   _|{r}
{rC2}      |__|____||_____||____|_____||____|___._||____|{r}
{bC}   ╓─────────────────────────────────────────────────{gC}►{r}
{bC}   ╚════╗
{bC}        ║{r}   To show all output one your PC.
{bC}        ║
{bC}        ╟──────{gC}►{bC2} Created by       ::  {rC}Thomas Pellissier{bC2} (from © PSociety™){r}
{bC}        ╟──────{gC}►{bC2} Codename         ::  {bC2}@{rC}MyMeepSQL{r}
{bC}        ╟──────{gC}►{bC2} Version          ::  {bC2}v{rC}0.0.1{r}
{bC}        ╟──────{gC}►{bC2} Internet Status  ::  {rC}{internetstatus}{r}
{bC}      ╔═╝{r}
{bC}      ╚════════════════════════════════════════════╗{r}
        Type 'netstat --help for the help message  {bC}║{r}
         (type 'exit' for exit the Netstat tool)   {bC}║{r}
{bC}      ═════════════════════════════════════════════╝\n{r}
{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/NetworkCommands/Netstat{bC}]{r}""")
        netstatcommand = str(input(f"{bC}└╼{rC}$ {r}"))
        if netstatcommand == "exit":
            usefulltools_networkC_main_page()
        elif netstatcommand:
            try:
                netstat = os.system(f"{netstatcommand}")
                print(netstat)
                input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to remake a netstat{bC}]{r}")
                usefulltools_networkC_netstat()
            except KeyboardInterrupt:
                print()
                print(f"{bC}[{rC2}*{bC}]{bC}─[{gC}CTRL + C detected stop the netstat...{bC}]{r}")
                input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to remake a netstat{bC}]{r}")
                usefulltools_networkC_netstat()
        else:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}No netstat command found{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_networkC_netstat()

    def usefulltools_networkC_whois():
        cls()
        print(f"""
{rC2}       ________ __           __        {r}
{rC2}      |  |  |  |  |--.-----.|__|.-----.{r}
{rC2}      |  |  |  |     |  _  ||  ||__ --|{r}
{rC2}      |________|__|__|_____||__||_____|{r}
{bC}   ╓────────────────────────────────────{gC}►{r}
{bC}   ╚════╗
{bC}        ║{r}   Find out how many routers a packet passes
{bC}        ║{r}        through before its destination.
{bC}        ║
{bC}        ╟──────{gC}►{bC2} Created by       ::  {rC}Thomas Pellissier{bC2} (from © PSociety™){r}
{bC}        ╟──────{gC}►{bC2} Codename         ::  {bC2}@{rC}MyMeepSQL{r}
{bC}        ╟──────{gC}►{bC2} Version          ::  {bC2}v{rC}0.0.1{r}
{bC}        ╟──────{gC}►{bC2} Internet Status  ::  {rC}{internetstatus}{r}
{bC}      ╔═╝{r}
{bC}      ╚═════════════════════════════════════════════════════════════════════════════════════════╗{r}
        Write an domain for see informations about it, type 'whois --help for the help message  {bC}║{r}
                              (type 'exit' for exit the Traceroute tool)                        {bC}║{r}
{bC}      ══════════════════════════════════════════════════════════════════════════════════════════╝\n{r}
{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/NetworkCommands/Traceroute{bC}]{r}""")
        whoiscommand = str(input(f"{bC}└╼{rC}$ {r}"))

        if whoiscommand == "exit":
            usefulltools_networkC_main_page()
        elif whoiscommand:
            if connexion() == True:
                try:
                    whois = os.system(f"{whoiscommand}")
                    print(whois)
                    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to write an another IP/domain for get informations about it{bC}]{r}")
                    usefulltools_networkC_whois()
                except KeyboardInterrupt:
                    print()
                    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to write an another IP/domain for whois{bC}]{r}")
                    usefulltools_networkC_whois()
                else:
                    print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Can’t get informations, check your Inthernet connexion and try again{bC}]{r}")
                    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
                    usefulltools_networkC_whois()
        else:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}No IP/domain found, write an IP/domain to whois it{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_networkC_whois()

    def usefulltools_networkC_traceroute():
        cls()
        print(f"""
{rC2}       _______                                          __         {r}
{rC2}      |_     _|.----.---.-.----.-----.----.-----.--.--.|  |_.-----.{r}
{rC2}        |   |  |   _|  _  |  __|  -__|   _|  _  |  |  ||   _|  -__|{r}
{rC2}        |___|  |__| |___._|____|_____|__| |_____|_____||____|_____|{r}
{bC}   ╓────────────────────────────────────────────────────────────────{gC}►{r}
{bC}   ╚════╗
{bC}        ║{r}   Find out how many routers a packet passes
{bC}        ║{r}        through before its destination.
{bC}        ║
{bC}        ╟──────{gC}►{bC2} Created by       ::  {rC}Thomas Pellissier{bC2} (from © PSociety™){r}
{bC}        ╟──────{gC}►{bC2} Codename         ::  {bC2}@{rC}MyMeepSQL{r}
{bC}        ╟──────{gC}►{bC2} Version          ::  {bC2}v{rC}0.0.7{r}
{bC}        ╟──────{gC}►{bC2} Internet Status  ::  {rC}{internetstatus}{r}
{bC}      ╔═╝{r}
{bC}      ╚═════════════════════════════════════════════════════════════════════════════════════╗{r}
        Write an IP to ping it and track it, type 'traceroute --help' for the help message  {bC}║{r}
                            (type 'exit' for exit the Traceroute tool)                      {bC}║{r}
{bC}      ══════════════════════════════════════════════════════════════════════════════════════╝\n{r}
{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/NetworkCommands/Traceroute{bC}]{r}""")
        traceroutecommand = str(input(f"{bC}└╼{rC}$ {r}"))

        if traceroutecommand == "exit":
            usefulltools_networkC_main_page()
        elif traceroutecommand:
            if connexion() == True:
                try:
                    traceroute = os.system(f"{traceroutecommand}")
                    print(traceroute)
                    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to write an another IP for traceroute it{bC}]{r}")
                    usefulltools_networkC_traceroute()
                except KeyboardInterrupt:
                    print()
                    print(f"{bC}[{rC2}*{bC}]{bC}─[{gC}CTRL + C detected stop the traceroute...{bC}]{r}")
                    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to write an another IP for traceroute{bC}]{r}")
                    usefulltools_networkC_traceroute()
                except RuntimeError:
                    print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}'{traceroutecommand}' not found, prlease ckeck the IP before trace it{bC}]{r}")
                    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
                    usefulltools_networkC_traceroute()
                else:
                    print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Can’t reach the destination, check your Internet Inthernet and try again{bC}]{r}")
                    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
                    usefulltools_networkC_traceroute()
        else:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}No IP/domain found, write an IP/domain to traceroute it{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_networkC_traceroute()

    def usefulltools_networkC_nslookup():
        cls()
        print(f"""
{rC2}       _______ _______ _____                __{r}
{rC2}      |    |  |     __|     |_.-----.-----.|  |--.--.--.-----.{r}
{rC2}      |       |__     |       |  _  |  _  ||    <|  |  |  _  |{r}
{rC2}      |__|____|_______|_______|_____|_____||__|__|_____|   __|{r}
{bC}   ╓───────────────────────────────────────────────────{rC2}|__|{bC}────{gC}►{r}
{bC}   ╚════╗{r}
{bC}        ║{r}    Some windows network commands
{bC}        ║{r}
{bC}        ╟──────{gC}►{bC2} Created by       :: {rC}Thomas Pellissier{bC2} (from © PSociety™){r}
{bC}        ╟──────{gC}►{bC2} Codename         :: @{rC}MyMeepSQL{r}
{bC}        ╟──────{gC}►{bC2} Version          :: v{rC}0.0.8{r}
{bC}        ╟──────{gC}►{bC2} Internet Status  :: {rC}{internetstatus}{r}
{bC}      ╔═╝{r}
{bC}      ╚═══════════════════════════════════════════╗{r}
         Write a domain for look the IP he used   {bC}║{r}
        (type 'exit' for exit the NSLookup tool)  {bC}║{r}
{bC}      ════════════════════════════════════════════╝\n{r}
{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/NetworkCommands/NSLookup{bC}]{r}""")
        ip_domain = str(input(f"{bC}└╼{rC}$ {r}"))
        if ip_domain == "exit":
            usefulltools_networkC_main_page()
        elif ip_domain:
            if connexion() == True:
                print(f"""
{bC}╔══════════════════════╗
{bC}║{r}   NSLookup respond{bC}   ║
{bC}╚══════════════════════╝{r}
""")
                nslookup = os.system(f"nslookup {ip_domain}")
                print(nslookup)
                print()
                input(f"{bC}[{rC2}-{bC}]─[{gC}Press [ENTER] key to write an another domain for nslookup{bC}]{r}")
                usefulltools_networkC_nslookup()
            else:
                print(f"{bC}[{rC2}!{bC}]─[{gC}Can’t reach the destination, check your Internet Inthernet and try again{bC}]{r}")
                input(f"{bC}[{rC2}-{bC}]─[{gC}Press [ENTER] key to retry{bC}]{r}")
                usefulltools_networkC_nslookup()
        else:
            print(f"{bC}[{rC2}!{bC}]─[{gC}No domain found, write an domain for lookup it{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_networkC_nslookup()

    def usefulltools_networkC_ping():
        cls()
        print(f"""
{rC2}      ______ __               {r}
{rC2}     |   __ \__|.-----.-----. {r}
{rC2}     |    __/  ||     |  _  | {r}
{rC2}     |___|  |__||__|__|___  | {r}
{bC}   ╓──────────────────{rC2}|_____|{bC}──{gC}►{r}
{bC}   ╚════╗{r}
{bC}        ║{r}    Ping IP/domain to test if it responds (if it is connected)
{bC}        ║{r}
{bC}        ╟──────{gC}►{bC2} Created by       :: {rC}Thomas Pellissier {bC2}(from © PSociety™){r}
{bC}        ╟──────{gC}►{bC2} Codename         :: @{rC}MyMeepSQL{r}
{bC}        ╟──────{gC}►{bC2} Version          :: v{rC}0.0.9{r}
{bC}        ╟──────{gC}►{bC2} Internet Status  :: {rC}{internetstatus}{r}
{bC}      ╔═╝{r}
{bC}      ╚═════════════════════════════════════════════════════════════╗{r}
        Write an IP to ping it, type 'ping -help' for help message  {bC}║{r}
                   (type 'exit' for exit the Ping tool)             {bC}║{r}
{bC}      ══════════════════════════════════════════════════════════════╝\n{r}
{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/NetworkCommands/Ping{bC}]{r}""")
        pingcommand = str(input(f"{bC}└╼{rC}$ {r}"))

        if pingcommand == "exit":
            usefulltools_networkC_main_page()
        elif pingcommand:
            if connexion() == True:
                try:
                    ping = os.system(f"{pingcommand}")
                    print(ping)
                    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to write an another IP for pinging{bC}]{r}")
                    usefulltools_networkC_ping()
                except KeyboardInterrupt:
                    print()
                    print(f"{bC}[{rC2}*{bC}]{bC}─[{gC}CTRL + C detected stop the ping...{bC}]{r}")
                    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to write an another IP for pinging{bC}]{r}")
                    usefulltools_networkC_ping()
            else:
                print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Can’t reach the destination, check your Internet Inthernet and try again{bC}]{r}")
                input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
                usefulltools_networkC_ping()
        else:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}No IP found, write an IP to ping it{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_networkC_ping()

### Usefull Windows tool  | Backup tool ###
    def usefulltools_backup_main():
        cls()
        print(f"""
{rC2}      _______                              ______              __                 {r}
{rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----. {r}
{rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  | {r}
{rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __| {r}
{bC}   ╓─────────────────────────{rC2}|_____|{bC}──────────────────────────────────────{rC2}|__|{bC}────{gC}►{r}
{bC}   ╚════════╗{r}
{bC}            ║{r}    A tool for make backup quickly{r}
{bC}            ║{r}
{bC}            ╟──────{gC}►{bC2} Created by :: {rC}Thomas Pellissier{bC2} (from © PSociety™){r}
{bC}            ╟──────{gC}►{bC2} Codename   :: @{rC}MyMeepSQL{r}
{bC}            ╟──────{gC}►{bC2} Version    :: v{rC}0.1.4{r}
{bC}    ╔═══════╝{r}
{bC}    ╚════════════════════════════════╗{r}
      Do you want make backup [Y/n]  {bC}║{r}
{bC}    ═════════════════════════════════╝\n{r}
{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/BackupTool/menu{bC}]{r}""")
        choice = str(input(f"{bC}└╼{rC}$ {r}"))

        if choice == "y" or choice == "Y":
            usefulltools_backup_source()
        elif choice == "n":
            usefulltools_mainpage()
        elif not choice:
            y_or_n_error()
            usefulltools_backup_main()
        else:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Invalid option, chose [Y/n]{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_backup_main()

    def usefulltools_backup_source():
        cls()
        print(f"""
{rC2}      _______                              ______              __                  {r}
{rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  {r}
{rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  {r}
{rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  {r}
{bC}   ╓─────────────────────────{rC2}|_____|{bC}──────────────────────────────────────{rC2}|__|{bC}────{gC}►{r}
{bC}   ╚════════════════════════════════════════════╗{r}
     Whish folder or file you want backup it ?  {bC}║{r}
           {rC}/!\{r} Type the source path {rC}/!\         {bC}║{r}
{bC}   ═════════════════════════════════════════════╝{r}

{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/BackupTool/source{bC}]{r}""")
        global omegabackup_source
        omegabackup_source = str(input(f"{bC}└╼{rC}$ {r}"))

        if not omegabackup_source:
            print(f"{bC}[{r}{rC2}!{r}{bC}]{r}{bC}─[{r}{gC}Type your source path{bC}]{r}")
            input(f"{bC}[{r}{rC2}-{r}{bC}]{r}{bC}─[{r}{gC}Press [ENTER] key to continue{bC}]{r}")
            usefulltools_backup_source()
        else:
            usefulltools_backup_destination()

    def usefulltools_backup_destination():
        cls()
        print(f"""
{rC2}      _______                              ______              __                  {r}
{rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  {r}
{rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  {r}
{rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  {r}
{bC}   ╓─────────────────────────{rC2}|_____|{bC}──────────────────────────────────────{rC2}|__|{bC}────{gC}►{r}
{bC}   ╚════════════════════════════════════╗{r}
       Where you want to backup it ?    {bC}║{r}
     {rC}/!\{r} Type the destination path {rC}/!\  {bC}║{r}
{bC}   ═════════════════════════════════════╝{r}

{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/BackupTool/destination{bC}]""")
        global oemgabackup_destination
        oemgabackup_destination = str(input(f"{bC}└╼{rC}$ {r}"))
            
        if not oemgabackup_destination:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Type your destination path{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_backup_destination()
        else:
            usefulltools_backup_verification()

    def usefulltools_backup_verification():
        cls()
        print(f"""
{rC2}      _______                              ______              __                  {r}
{rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  {r}
{rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  {r}
{rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  {r}
{bC}   ╓─────────────────────────{rC2}|_____|{bC}──────────────────────────────────────{rC2}|__|{bC}────{gC}►{r}
{bC}   ╚═════════════════════════════════════╗{r}
     Are you sure you want backup [Y/n]  {bC}║{r}
{bC}   ╔═════════════════════════════════════╝{r}
{bC}   ╚════╗{r}
{bC}        ╟──────{gC}►{rC} Source{bC} ───────{gC}► {rC}"{r}{omegabackup_source}{rC}"{r}
{bC}        ╚──────{gC}►{rC} Destination{bC} ──{gC}► {rC}"{r}{oemgabackup_destination}{rC}"{r}

{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/BackupTool/verification{bC}]{r}""")
        sure = str(input(f"{bC}└╼{rC}$ {r}"))

        if not sure:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Chose [Y/n]{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_backup_verification()

        elif sure == "y" or sure == "Y":
            cls()
            print(f"""
{rC2}      _______                              ______              __                {r}
{rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.{r}
{rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |{r}
{rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|{r}
{bC}   ╓─────────────────────────{rC2}|_____|{bC}──────────────────────────────────────{rC2}|__|{bC}────{gC}►{r}
{bC}   ╚═══════════╗{r}
     Backuping...  {bC}║
{bC}   ════════════╝{r}""")
            try:
                from datetime import datetime
                from pathlib import Path
                import zipfile
                OBJECT_TO_BACKUP = f'{omegabackup_source}'          # The file or directory to backup
                BACKUP_DIRECTORY = f'{oemgabackup_destination}'     # The location to store the backups in
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
                backup_file_name = f'BACKUP-{datetime.now().strftime("%Y-%m-%W %Hh%M %Ss")} - {object_to_backup_path.name}.zip'
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

                cls()
                print(f"""
{rC2}      _______                              ______              __                {r}
{rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.{r}
{rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |{r}
{rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|{r}
{bC}   ╓─────────────────────────{rC2}|_____|{bC}──────────────────────────────────────{rC2}|__|{bC}────{gC}►{r}
{bC}   ╚════════════════════════════╗{r}
     Backup end successfully !{bC}  ║{r}
{bC}   ═════════════════════════════╝{r}""")
                sleep(2)
                usefulltools_backup_remakebackup()
            except KeyboardInterrupt:
                print(f"{bC}     ║ [{rC2}*{bC}]─[{gC}CTRL + C detected stop the ping.{bC}]{r}")
                print(f"{bC}     ║ [{rC2}!{bC}]─[{gC}Backup interrupted.{bC}]{r}")
                print(f"{bC}     ║ [{rC2}-{bC}]─[{gC}Deleting current backup...{bC}]{r}")
                os.system(f"rm -fr ")
            except PermissionError:
                print(f"{bC}     ║ [{rC2}!{bC}]─[{gC}Permission denied.{bC}]{r}")
                print(f"{bC}     ║ [{rC2}!{bC}]─[{gC}Please check your permissions with your folder/users.{bC}]{r}")
                print(f"{bC}     ║ [{rC2}-{bC}]─[{gC}Do you want to remake the backup config ? [Y/n]{bC}]{r}")
                print(f"{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/BackupTool/permission_denied{bC}]{r}")
                permerror = str(input(f"{bC}└╼{rC}$ {r}"))
                
                while not permerror:
                    print(f"{bC}[{rC2}!{bC}]─[{gC}Chose [Y/n]{bC}]{r}")
                    print(f"{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/BackupTool/permission_denied{bC}]{r}")
                    permerror = str(input(f"{bC}└╼{rC}$ {r}"))
                if permerror == "y" or permerror == "Y":
                    usefulltools_backup_source()
                if permerror == "n" or permerror == "N":
                    usefulltools_mainpage()
            except:
                print(f"{bC}     ║ [{rC2}*{bC}]─[{gC}Error occurred while copying file{bC}]{r}")
                print(f"""{bC}     ║ [{rC2}!{bC}]─[{gC}Check the source/destination path whether they are correct or no,
     {bC}║{gC}   check that the files are not corrupted or some other problem and redo the backup configuration{bC}]{r}""")
                input(f"{bC}     ║ [{rC2}-{bC}]─[{gC}Press [ENTER] key to remake the backup configuration{bC}]{r}")
                usefulltools_backup_source()
        elif sure == "n" or sure =="N":
            usefulltools_backup_reconfig()
        else:
            print(f"{bC}[{rC2}!{bC}]─[{gC}Invalid option, chose [Y/n]{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_backup_verification()

    def usefulltools_backup_reconfig():
        cls()
        print(F"""
{rC2}      _______                              ______              __                {r}
{rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.{r}
{rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |{r}
{rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|{r}
{bC}   ╓─────────────────────────{rC2}|_____|{bC}──────────────────────────────────────{rC2}|__|{bC}────{gC}►{r}
{bC}   ╚═════════════════════════════════════════════════╗{r}
     Do you want reconfig the backup config ? [Y/n]  {bC}║{r}
{bC}   ══════════════════════════════════════════════════╝{r}

{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/BackupTool/Remake_the_backup_config{bC}]{r}""")
        choice = str(input(f"{bC}└╼{rC}$ {r}"))
        if choice == "y" or choice == "Y":
            usefulltools_backup_source()
        elif choice == "n" or choice == "N":
            usefulltools_mainpage()
        elif not choice:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Choose [Y/n]{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_backup_reconfig()
        else:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Invalid option, choose [Y/n]{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_backup_reconfig()

    def usefulltools_backup_remakebackup():
        cls()
        print(f"""
{rC2}      _______                              ______              __                {r}
{rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.{r}
{rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |{r}
{rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|{r}
{bC}   ╓─────────────────────────{rC2}|_____|{bC}──────────────────────────────────────{rC2}|__|{bC}────{gC}►{r}
{bC}   ╚═════════════════════════════════════════╗{r}
     Do you want to remake a backup ? [Y/n]  {bC}║{r}
{bC}   ══════════════════════════════════════════╝{r}

{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/UTools/BackupTool/remake_backup_config{bC}]{r}""")
        choice = str(input(f"{bC}└╼{rC}$ {r}"))
        if choice == "y" or choice == "Y":
            usefulltools_backup_source()
        elif choice == "n" or choice == "N":
            usefulltools_mainpage()
        elif not choice:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Choose [Y/n]{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_backup_reconfig()
        else:
            print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Invalid option, choose [Y/n]{bC}]{r}")
            input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")
            usefulltools_backup_reconfig()
#-End-Usefull Windows tool-------------------------------------------#

#-OmegaPSToolkit-CLI-main-page---------------------------------------#
    def cli_main_page():
        print(f"""
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {gC}      _____                   _____ _____ _____         _ _   _ _{r}
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {gC}     |     |_____ ___ ___ ___|  _  |   __|_   _|___ ___| | |_|_| |_{r}
{bC}        MMMMMMMMMMMMMMMMMNmmmmNNMMMMMMMMMMMMMMMM {gC}     |  |  |     | -_| . | .'|   __|__   | | | | . | . | | '_| |  _|{r}
{bC}        MMMMMMMMMMMdy+:.```..```.-/shNMMMMMMMMMM {gC}     |_____|_|_|_|___|_  |__,|__|  |_____| |_| |___|___|_|_,_|_|_|   {gC}v{rC}{opstconsole_cli_version}{r}
{bC}        MMMMMMMNy/``  -ohmNNNNNdy/`  `:smMMMMMMM {bC} ╓───────────────────{gC}|___|{bC}─────────────────────────────────────────────────────{gC}►{r}
{bC}        MMMMMNo.    :dNMMMMMMMMMMMNo`   `/dMMMMM {bC} ║{r}
{bC}        MMMMh.     sMMMMMMMMMMMMMMMMd.    `+NMMM {bC} ║     {r}OmegaPSToolkit factory for penetration testing
{bC}        MMMy`     sMMMMMMMMMMMMMMMMMMm`     /MMM {bC} ║{r}
{bC}        MMm`     :MMMMMMMMMMMMMMMMMMMMy      oMM {bC} ╚════╗{r}
{bC}        MM-      MMMMMMMMMMMMMMMMMMMMMM+      mM {bC}      ╟──────{gC}► {bC2}{underscore}Created by{W}{bC2}       :: {rC}Thomas Pellissier{bC2} (from © PSociety™){r}
{bC}        MMo      NMMMMMMMMMMMMMMMMMMMMM/     `MM {bC}      ╟──────{gC}► {bC2}{underscore}OPSTC CLI Version{W}{bC2}:: v{rC}{opstconsole_cli_version}{r}
{bC}        MMN`     yMMMMMMMMMMMMMMMMMMMMN`     sMM {bC}      ╟──────{gC}► {bC2}{underscore}Internet Status{W}{bC2}  ::    {rC}{internetstatus}{r}
{bC}        MMMh`    .NMMMMMMMMMMMMMMMMMMM+     /MMM {bC}      ╟────╥─{gC}► {bC2}{underscore}Codename{W}{bC2}         :: @{rC}MyMeepSQL or {bC2}@{bC2}th300905{r}
{bC}        MMMMh.    :NMMMMMMMMMMMMMMMMMs    `oMMMM {bC}      ║{bC}    ╙───────────────────{gC}►{bC2}{rC}  The {bC2}{underscore}seconde{W}{rC} codename is also mine{r}
{bC}        MMMMMNo.   -hNMMMMMMMMMMMMMm+   `/dMMMMM {bC}      ╚════════╗{r}
{bC}        NdMMMMMNy/.` -smMMMMMMMMNy/` `:smMMMMMNm {bC}               ║                      {r}Developed for linux
{bC}        m`hNMMMMMMNdy: `MMMMMMMM+ .shmMMMMMMNm:+ {bC}               ║{r}
{bC}        m  -/+ooooooo+  mMMMMMMM: .ooooooo+/:` o {bC}               ║{gC}             Welcome to the OmegaPSToolkit (OPST).{r}
{bC}        N               hMMMMMMM`              o {bC}               ║{gC} The toolkit which includes a set of penetration testing tools.{r}
{bC}        M               yMMMMMMM               s {bC}               ║{r}
{bC}        MNmmmmmmmmmmmmmmMMMMMMMMmmmmmmmmmmmmmmmM {bC}               ╚         {rC}{r}{italic}The OmegaPSToolkit is a product of © PSociety™{W}{r}
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {r}
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {r}
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {r}


{G}[*]{GR}  This is the CLI version of opstonsole, type "{B}help{GR}" for all commands
{R}[!]{GR}  This CLI version of osptconsoel is {underscore}{R}TOTALLY{W}{GR} in {R}BETA
""")

        while True:
            prompt_for_command = f"{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/CLI_BETA{bC}]{r}"
            user_input = input(prompt_for_command + f"\n{bC}└╼{rC}$ {r}")
            command = user_input
            if not command:
                print()
                user_input
            # elif "connexionstatus" == command:
            #     print(f"{B}[-]{GR}    Checking for Internet connexion...{W}")
            #     sleep(1)
            #     if connexion() == True:
            #         internetstatus = f"{G}Connected{W}"
            #         print(f"{G}[+]{GR}    Internet status : {G}Connected{W}.")
            #     else:
            #         internetstatus = f"{R}Not connected{W}"
            #         print(f"{R}[!]{GR}    Internet status : {R}Not connected{W}.")
            #     print()
            elif "ping" == command:
                print(f"""
{C}[-]{W}    Type an IP/domain to ping it (type '-help' for the help message, type 'leave' for exit ping tool)
{G}[+]{W}    Exemple: -c 4 1.1.1.1
       Exemple: -c 4 google.com
       Exemple: -c 4 https://duckduckgo.com
    """)
                while True:
                    prompt_for_command = f"{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/CLI_BETA/ping{bC}]{r}"
                    user_input = input(prompt_for_command + f"\n{bC}└╼{rC}$ {r}")
                    command = user_input

                    if not command:
                        print()
                        user_input
                    elif "leave" == command:
                        print()
                        print(f"{G}[-]{W}    Exiting ping tool...")
                        print()
                        break
                    else:
                        os.system(f"ping {command}")
                        print()
            elif "nslookup" == command:
                print(f"""
{C}[-]{W}    Type an IP/domain to nslookup it (type 'leave' for exit nslookup tool)
{G}[+]{W}    Exemple: 8.8.8.8
       Exemple: google.com
    """)
                print()
                while True:
                    prompt_for_command = f"{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~/CLI_BETA/nslookup{bC}]{r}"
                    user_input = input(prompt_for_command + f"\n{bC}└╼{rC}$ {r}")
                    command = user_input

                    if not command:
                        print()
                        user_input
                    elif "leave" == command:
                        print()
                        print(f"{G}[-]{W}    Exiting nslookup tool...")
                        print()
                        break
                    else:
                        os.system(f"nslookup {command}")
                        print()

            elif "clear" == command:
                cls()
                cli_main_page()
            elif "help" == command:
                cli_helpmsg()
            elif "info" == command:
                cli_infomsg()
            elif "leave" == command:
                print(f"{G}[-]{W}   Exiting CLI mode...")
                sleep(0.5)
                main_page()
            elif "exit" == command:
                exitodst()
            else:
                unknown_command = f"{R}\n[!]{W}   '{command}' is not recognized as an internal or external command.\n"
                print(unknown_command)

#-OmegaPSToolkit-main-page-------------------------------------------#
    def main_page():
        cls()
        print(f"""
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {gC}      _____                   _____ _____ _____         _ _   _ _{r}
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {gC}     |     |_____ ___ ___ ___|  _  |   __|_   _|___ ___| | |_|_| |_{r}
{bC}        MMMMMMMMMMMMMMMMMNmmmmNNMMMMMMMMMMMMMMMM {gC}     |  |  |     | -_| . | .'|   __|__   | | | | . | . | | '_| |  _|{r}
{bC}        MMMMMMMMMMMdy+:.```..```.-/shNMMMMMMMMMM {gC}     |_____|_|_|_|___|_  |__,|__|  |_____| |_| |___|___|_|_,_|_|_|   {gC}v{rC}{opstconsole_version}{r}
{bC}        MMMMMMMNy/``  -ohmNNNNNdy/`  `:smMMMMMMM {bC} ╓───────────────────{gC}|___|{bC}─────────────────────────────────────────────────────{gC}►{r}
{bC}        MMMMMNo.    :dNMMMMMMMMMMMNo`   `/dMMMMM {bC} ║{r}
{bC}        MMMMh.     sMMMMMMMMMMMMMMMMd.    `+NMMM {bC} ║     {r}OmegaPSToolkit factory for penetration testing{r}
{bC}        MMMy`     sMMMMMMMMMMMMMMMMMMm`     /MMM {bC} ║{r}
{bC}        MMm`     :MMMMMMMMMMMMMMMMMMMMy      oMM {bC} ╚════╗{r}
{bC}        MM-      MMMMMMMMMMMMMMMMMMMMMM+      mM {bC}      ╟──────{gC}► {bC2}{underscore}Created by{W}{bC2}       ::{rC} Thomas Pellissier{bC2} (from © PSociety™){r}
{bC}        MMo      NMMMMMMMMMMMMMMMMMMMMM/     `MM {bC}      ╟──────{gC}► {bC2}{underscore}OPSTC Version{W}{bC2}    :: v{rC}{opstconsole_version}{r}
{bC}        MMN`     yMMMMMMMMMMMMMMMMMMMMN`     sMM {bC}      ╟──────{gC}► {bC2}{underscore}Internet Status{W}{bC2}  ::{rC} {internetstatus}{r}
{bC}        MMMh`    .NMMMMMMMMMMMMMMMMMMM+     /MMM {bC}      ╟────╥─{gC}► {bC2}{underscore}Codename{W}{bC2}         :: @{rC}MyMeepSQL or {bC2}@{bC2}th300905{r}
{bC}        MMMMh.    :NMMMMMMMMMMMMMMMMMs    `oMMMM {bC}      ║{bC}    ╙───────────────────{gC}►{bC2}{rC}  The {bC2}{underscore}seconde{W}{rC} codename is also mine{r}
{bC}        MMMMMNo.   -hNMMMMMMMMMMMMMm+   `/dMMMMM {bC}      ╚════════╗{r}
{bC}        NdMMMMMNy/.` -smMMMMMMMMNy/` `:smMMMMMNm {bC}               ║                      {r}Developed for linux{r}
{bC}        m`hNMMMMMMNdy: `MMMMMMMM+ .shmMMMMMMNm:+ {bC}               ║{r}
{bC}        m  -/+ooooooo+  mMMMMMMM: .ooooooo+/:` o {bC}               ║{gC}             Welcome to the OmegaPSToolkit (OPST).{r}
{bC}        N               hMMMMMMM`              o {bC}               ║{gC} The toolkit which includes a set of penetration testing tools.{r}
{bC}        M               yMMMMMMM               s {bC}               ║{r}
{bC}        MNmmmmmmmmmmmmmmMMMMMMMMmmmmmmmmmmmmmmmM {bC}               ║          {r}{italic}The OmegaPSToolkit is a product of © PSociety™.{W}
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {bC}               ║{r}{italic}                  2021-2022, All rights reserved.
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {bC}               ║{r}
{bC}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM {bC}               ╚                        {GR}{underscore}SELECT AN OPTION{W}


                [{bC}1{r}]{gC}    Information Gathering tools{r}
                [{bC}2{r}]{gC}    Wireless tools{r}
                [{bC}3{r}]{gC}    Useful tools (UT){r}
                [{bC}cli{r}]{gC}  Use OPST like a Command Line Interpeter {bC}[{rC}BETA{bC}]{r}
                [{bC}help{r}]{gC} Show the help message{r}
                [{bC}exit{r}]{gC} Exit the opstconsole{r}

OPST was not finish and he's totally in development!

{bC}┌──({rC}OmegaPSToolkit{bC})─[{r}~{bC}]{r}""")
        global command
        command = str(input(f"{bC}└╼{rC}$ {r}"))

        if command == "1":
            cls()
            informationgathering_mainpage()
        elif command == "2":
            cls()
            wireless_mainpage()
        elif command == "3":
            cls()
            usefulltools_mainpage()
        elif command == "cli":
            print(f"{G}[-]{W}   Loading CLI mode...")
            sleep(0.5)
            cls()
            cli_main_page()
        elif command == "help":
            mainpage_helpmsg()
            cls()
            main_page()
        elif command == "exit":
            exitodst()
        elif not command:
            error()
            cls()
            main_page()
        else:
            invalid_option()
            cls()
            main_page()
            
    #-END-OF-MAIN-PAGE---------------------------------------------------#

    main_page()      # call the main function

except KeyboardInterrupt:
    print()
    exitodst()
except EOFError:
    print()
    exitodst()
#-END-OF-MAIN-TOOL---------------------------------------------------#



























#      _______________________
#     |    _____     _____    |
#     |   | __ |    | __ |    |
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
#       |_______|_________| Built by MyMeepSQL | Please don’t change/delete that. This is my signature.
#                           Codename MyMeepSQL by © PSociety™. 2022, all rights reserved.

#                    ______
#                   / ____ |
#                  /</   |<|
#                 /</    |>|
#         _      /</     |<|
#      __||__   /</      \_/
#  ___| OPST |_/</
# |  __________  |
# \__________                          