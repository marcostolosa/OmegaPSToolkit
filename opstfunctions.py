#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstfunctions.py              [Update: 2022-04-11 | 12:57 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}         #
#                                                                           #
#  The file wich include all functions                                      #
#  Language  ~  Python3                                                     #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright (C) 2022 MyMeepSQL - © Delta_Society™                          #
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
try:
    import os,sys
    from opstcolors import *
    from opstversions import *
except ModuleNotFoundError:
    print()
    criticalmsg = f"{B}[{r}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run the 'setup.py' for install it. (sudo python3 setup.py install)\n"
    sys.exit(criticalmsg)
except NameError:
    print()
    criticalmsg = f"{B}[{r}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run the 'setup.py' for install it. (sudo python3 setup.py install)\n"
    sys.exit(criticalmsg)
####

# Functions
## Main functions
def non_linux():
    print()
    criticalmsg = f"{B}[{R}FATAL ERROR{B}]{R} You tried to run OPST on a non-linux machine. OPST can be run only on a Linux kernel.\n{W}"
    sys.exit(criticalmsg)

def connexion(host='https://google.com'):
    import urllib.request
    try:
        urllib.request.urlopen(host, timeout=10)    # Check if the user have an Internet connection
        return True
    except:
        return False

def cls():
    os.system('clear')

def exitodst():
    exitodst = f"\n{bC}[{gC}Goodby{bC}]{r}\n"
    exit(exitodst)

def error():
    print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Choose a option{bC}]{r}")                  # if the user doesn't choose option
    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to continue{bC}]{r}")    #

def y_or_n_error():
    print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Chose y or n{bC}]{r}")                     # If the user does not choose "y" or "n"
    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")       #

def mainpage_helpmsg():
    print(f"""
{GR}{D} _______ ______ _______ _______ {W}
{GR}{D}|       |   __ \     __|_     _|{W}{G}  OmegaPSToolkit {D}v{opstconsole_version}
{GR}{D}|   -   |    __/__     | |   |  {W}{D}  A massive penetration testing toolkit
{GR}{D}|_______|___|  |_______| |___|  {C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}

All commands of the OmegaDSToolkit you can use is the main page

{B}COMMAND:{W}
    1           ::   Go to the Information Gathering page
    2           ::   Go to the Wireless Tools page
    3           ::   Go to the Usefull tools page
    cli         ::   Use the opstconsole like a CLI
    help        ::   Show this help message
    exit        ::   Exit opstconsole
    """)
    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to continue{bC}]{r}")



###

## CLI functions
def cli_helpmsg():
    print(f"""
{GR}{D} _______ ______ _______ _______ {W}
{GR}{D}|       |   __ \     __|_     _|{W}{G}  OmegaPSToolkit CLI {D}v{opstconsole_cli_version}
{GR}{D}|   -   |    __/__     | |   |  {W}{D}  A massive penetration testing toolkit
{GR}{D}|_______|___|  |_______| |___|  {C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}

All commands of the OmegaDSToolkit CLI you can use is the main page

{B}COMMAND:{W}
    ping        ::      The ping tool
    nslookup    ::      The nslookup tool
    netstat     ::      The netstat tool
    which       ::      The which tool

{B}OTHER COMMAND:{W}
    help        ::      Show this help message
    info        ::      Show informations about OSPT and other informations
    leave       ::      Exit opstconsole's CLI version
    exit        ::      Exit opstconsole
""")

def cli_infomsg():
    print(f"""
{GR}{D} _______ ______ _______ _______ {W}
{GR}{D}|       |   __ \     __|_     _|{W}{G}  OmegaPSToolkit CLI {D}v{opstconsole_cli_version}
{GR}{D}|   -   |    __/__     | |   |  {W}{D}  A massive penetration testing toolkit
{GR}{D}|_______|___|  |_______| |___|  {C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}

Some informations about the OmegaPSToolkit

{C}Informations about OmegaPSToolkit{GR}:{W}

    {G}OPST versions{GR}:{W}
        opstconsole         v{opstconsole_version}
        odstconsole CLI     v{opstconsole_cli_version}
        opstupdate          {opstupdate_version}
        opsthelp            {opstupdate_help}
        odstsetup           {opstsetup_version}
        odstinstall-all     {opstinstallall_version}

    {G}Other versions{GR}:{W}
        python              v{python_version}

{C}Informations about author{GR}:{W}
    Author                  Thomas Pellissier
    Codename                MyMeepSQL
    Owner                   © PSociety™. 2022, All rights reserved.

{C}Ohter informations{GR}:{W}
    Operating System (OS)   {OS}
""")
###




# End of functions section