#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstsetup.py                   [Update: 2022-04-05 | 1:30 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The SetupTool for ODST                                                   #
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

# Import Section
import urllib.request
import os,sys
from opstversions import opstsetup_version
from setuptools import setup,find_packages
from time import sleep
####

# Some functions
def abort():
    abort_msg = f"\n{GR}{D}[-]{W}    Abort."
    sys.exit(abort_msg)
####

# Colors
## Basic colors
W = '\033[0m'      # white (normal)
R = '\033[31m'     # red
G = '\033[32m'     # green
O = '\033[33m'     # orange
B = '\033[34m'     # blue
P = '\033[35m'     # purple
C = '\033[36m'     # cyan
GR = '\033[37m'    # gray
D = '\033[2m'      # dims current color. {W} resets.
## Text formating
bold = '\033[1m'
dark = '\033[2m'
italic = '\033[3m'
underscore = '\033[4m'
normal = '\033[22m'
####

# The SetupTool
try:
    if os.getuid() != 0:    #   check if the user run OPST with root privilege
        permerror =f"""
{R}[!]{W}    OPSTSetup could be run as the 'root' user or with 'sudo'
       Re-run the 'opstsetup' with 'sudo' or with the 'root' user
       Run \"sudo opstsetup install\"
"""
        sys.exit(permerror)
except AttributeError:
    print()
    criticalmsg = f"{B}[{R}FATAL ERROR{B}]{R}    You tried to run OPST on a non-linux machine. OPST can be run only on a Linux kernel.\n{W}"
    sys.exit(criticalmsg)
except EOFError:
    print()
    print(f"{GR}{D}    Abort.{W}")
    sys.exit()
except KeyboardInterrupt:
    print()
    print(f"{GR}{D}    Abort.{W}")
    sys.exit()
else:
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            long_description = fh.read()
        print()
        print(f"{GR}{D} _______ ______ _______ _______ _______         __               ")
        print(f"{GR}{D}|       |   __ \     __|_     _|     __|.-----.|  |_.--.--.-----.{W}{G}  OPSTSetup {D}{opstsetup_version}")
        print(f"{GR}{D}|   -   |    __/__     | |   | |__     ||  -__||   _|  |  |  _  |{W}{D}  A massive penetration testing toolkit")         # Police = Chunky from https://www.coolgenerator.com/ascii-text-generator
        print(f"{GR}{D}|_______|___|  |_______| |___| |_______||_____||____|_____|   __|{C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}")
        print(f"{GR}{D}  + -------- !* Welcome to the OPSTSetup. *! -------- +   |__|{W}")
        print()
        print(f"{G}[-]{W}    Checking for internet connexion...")
        print()
        try:
            urllib.request.urlopen('http://google.com')
            connexion = True
        except:
            connexion =  False
        if connexion == True:
            print(f"+ -- --=[  Internet status.......... {G}Connected{W}.                                                                             ]")
            pass
        else:
            print(f"{R}[!]{W}   Internet status.......... {R}Not connected{W}.                                            ]")
            print(f"{R}[*]{W}   No Internet connexion found, please check you are connected to Internet and retry.  ]")
            sys.exit()
        print(f"+ -- --=[  {underscore}The tool will:{W}                                                                                                   ]")
        print(f"        [    ...Install {G}Colored{W} and {G}Progress{W} PIP3 modules that OmegaPSToolkit must have and make a {G}OmegaPSToolkit package{W}.  ]")
        print()
        yn = str(input(f"{C}[?]{W}    Do you want to continue? [Y/n] "))
        if yn != 'y' and yn != 'Y':
            abort()
        elif not yn:
            abort()
        else:
            pass
        try:
            print()
            print(f"{G}{D}--------------------------------------------------------------------------------------{W}")
            print()
            print(f"{G}[-]{W}    Installing {G}Colored{W}, {G}Progress{W} and make a {G}OmegaPSToolkit package{W}...")
            print()
            sleep(0.5)
            setup(classifiers=[
                    "Copyright                          :: Copyright (C) 2022, Thomas Pellissier aka MyMeepSQL from © PSociety™",
                    "Author                             :: Thomas Pellissier",
                    "Developed for                      :: Linux",
                    "Development Status                 :: 2 - In Development",
                    "Natural Language                   :: English",
                    "Environment                        :: Terminal",
                    "Intended Audience                  :: Developers, Sec.",
                    "Programming Language               :: Python :: 3.8",
                    "Programming Language compatible    :: Python :: 3.1-3.x.x",
                    "Other Programming Language         :: Bash (Linux)",
                ],
                name='OmegaPSToolkit',
                description='A massive penetration testing toolkit',
                long_description = long_description,
                url='https://github.com/MyMeepSQL/OmegaPSToolkit',
                author='Thomas Pellissier',
                author_email='thomas.pellissier@outlook.com',
                license='GNU-GPL-3.0',
                version='0.0.1.3',
                python_requires='>=3.1.0',
                packages=find_packages(),
                zip_safe=False,
                include_package_data=True,
                install_requires=[
                    'progress', 'colored'
                ],
            )
            print()
            print(f"{G}[-]{W}    Instalation complete.")
            sleep(1)
            print()
            print(f"{G}{D}--------------------------------------------------------------------------------------{W}")
            print()
            yn = str(input(f"{C}[?]{W}    Do you want to reload your terminal (just in case) ? [Y/n] "))
            if yn == 'y' or yn == 'Y':
                print()
                print(f"{G}{D}---------------------{W}")
                print(f"{G}[-]{W}    Reloading...")
                print(f"{G}{D}---------------------{W}")
                sleep(0.5)
                os.system("reset")
                print()
                print(f"{G}{D}-----------------------------------------------------------------------------------------------------------------------------------------{W}")
                print()
                print(f"{B}[OK]{W}    {G}Colored{W}, {G}Progress{W} and {G}OmegaPSToolkit{W} PIP modules was succefully {G}installed{W}. Now you can run OPSTConsole with '{G}sudo opstconsole{W}'.")
                print()
                print(f"{G}{D}-----------------------------------------------------------------------------------------------------------------------------------------{W}")
                print()
                sys.exit()
            else:
                print()
                print(f"{G}{D}--------------------{W}")
                print(f"{B}{D}[+]{W}    Answer: {R}No{W}.")
                print(f"{G}{D}--------------------{W}")
                print()
                print(f"{G}{D}-----------------------------------------------------------------------------------------------------------------------------------------{W}")
                print()
                print(f"{B}[OK]{W}    {G}Colored{W}, {G}Progress{W} and {G}OmegaPSToolkit{W} PIP modules was succefully {G}installed{W}. Now you can run OPSTConsole with '{G}sudo opstconsole{W}'.")
                print()
                print(f"{G}{D}-----------------------------------------------------------------------------------------------------------------------------------------{W}")
                print()
                sys.exit()  
        except EOFError:
            abort()
        except KeyboardInterrupt:
            abort()
    except EOFError:
        abort()
    except KeyboardInterrupt:
        abort()
####