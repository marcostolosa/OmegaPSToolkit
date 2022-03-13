#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ update.py                     [Update: 2022-03-13 | 16:40 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}         #
#                                                                           #
#  The update tool for have the latest version of ODST                      #
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
import sys
from time import sleep
from functions import *
####

version = "v1.7"

def updatetool():
    # heck if the user run update with root privilege
    try:
        if os.getuid() != 0:
            print("The OmegaDSToolkit's update tool could be run with root privilege") 
            print("Re-run the update.py with sudo")
            print('Run "sudo python3 update.py"')
            sys.exit()

    # If the user tries to run ODST from a non-Linux machine
    except AttributeError:
        print()
        criticalmsg = blue+"["+red+"CRITICAL"+blue+"]"+red+" You tried to run ODST on a no-linux machine, ODST can be run only on a Linux kernel"+reset#
        exit(criticalmsg)
    else:
        try:
            print(f"""
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗████████╗ ██████╗  ██████╗ ██╗
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗     ██║   ██║   ██║██║   ██║██║
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝     ██║   ██║   ██║██║   ██║██║
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗   ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ {version}""")   # Police = ANSI Shadow from https://www.coolgenerator.com/ascii-text-generator
            print("+ ------------------- !* UpdateTool for OmegaDSToolkit  *! ------------------- +")
            print()
            print("+ ----------------------------------- +")
            print("  Checking for internet connection...")
            print("+ ----------------------------------- +")
            print()

            if connection() == True:
                print("Internet status.......... "+lime+"Connected"+reset)
                pass
            else:
                print("Internet status.......... "+red+"Not connected"+reset)
                print("Not Internet connexion found, please check you are connected to Internet and retry.")
                sys.exit()

            print("The update tool will be install the latest version of OmegaDSToolkit")
            yn = str(input("Do you want to continue? [Y/n] "))

            if yn != 'y' and yn != 'Y':
                print("Abort.")
                sys.exit()
            elif not yn:
                print("Abort.")
                sys.exit()
            else:
                pass

            # Removing the current local OmegaDSToolkit, SetupTool and InstallTool
            print("+ -- --=[-------------------------------------------------------------------]")
            print("+ -- --=[  Remove the current OmegaDSToolkit, SetupTool and InstallTool...  ]")
            print("+ -- --=[-------------------------------------------------------------------]")
            os.system("rm -f /usr/share/OmegaDSToolkit/OmegaDSToolkit.py")
            os.system("rm -f /usr/share/OmegaDSToolkit/setup.py")
            os.system("rm -f /usr/share/OmegaDSToolkit/install.sh")
            print("+ -- --=[--------------------]")
            print("+ -- --=[  Remove complete.  ]")
            print("+ -- --=[--------------------]")
            sleep(1)

            print()
            print()

            os.system("cd /usr/share/OmegaDSToolkit/")
            # For OmegaDSToolkit
            print("+ -- --=[----------------------------------------------------]")
            print("+ -- --=[  Download the latest version of OmegaDSToolkit...  ]")
            print("+ -- --=[----------------------------------------------------]")
            print()
            ## Download OmegaDSToolkit with wget from github raw
            os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/OmegaDSToolkit.py")
            print()
            print("+ -- --=[----------------------------]")
            print("+ -- --=[  Done for OmegaDSToolkit.  ]")
            print("+ -- --=[----------------------------]")
            sleep(1)

            print()
            print()

            os.system("cd /usr/share/OmegaDSToolkit/")
            # For the SetupTool
            print("+ -- --=[-----------------------------------------------]")
            print("+ -- --=[  Download the latest version of SetupTool...  ]")
            print("+ -- --=[-----------------------------------------------]")
            print()
            ## Download SetupTool with wget from github raw
            os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/setup.py")
            print()
            print("+ -- --=[-----------------------]")
            print("+ -- --=[  Done the SetupTool.  ]")
            print("+ -- --=[-----------------------]")
            sleep(1)

            print()
            print()

            os.system("cd /usr/share/OmegaDSToolkit/")
            # For the InstallTool
            print("+ -- --=[-------------------------------------------------]")
            print("+ -- --=[  Download the latest version of InstallTool...  ]")
            print("+ -- --=[-------------------------------------------------]")
            print()
            ## Download InstallTool with wget from github raw
            os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/install.sh")
            print()
            print("+ -- --=[-------------------------]")
            print("+ -- --=[  Done the InstallTool.  ]")
            print("+ -- --=[-------------------------]")
            sleep(1)

            print()
            print()

            # Apply all rights to the new files
            print("+ -- --=[----------------------------------------]")
            print("+ -- --=[  Apply all rights to the new files...  ]")
            print("+ -- --=[----------------------------------------]")
            print()
            os.system('chmod +xrw OmegaDSToolkit.py')     # for the OmegaDSToolkit
            os.system('chmod +xrw setup.py')              # for the SetupTool
            os.system('chmod +xrw install.sh')            # for the InstallTool
            print("+ -- --=[-----------------------------]")
            print("+ -- --=[  Done for the right files.  ]")
            print("+ -- --=[-----------------------------]")
            sleep(1)

            print()

            print("+ -- --=[----------------------]")
            print("+ -- --=[  Update complete! .  ]")
            print("+ -- --=[----------------------]")

            print()
            print()

            print("+ -- --=[--------------------------------------------------------------]")
            print("+ -- --=[  You can run OmegaDSToolkit now. With \"sudo omegadstoolkit\"]")
            print("+ -- --=[--------------------------------------------------------------]")
            sys.exit()
        except KeyboardInterrupt:
            print()
            print("CTRL + C detected, stopping the update tool...")
            sys.exit()
        except EOFError:
            print()
            print("CTRL + C detected, stopping the update tool...")
            sys.exit()


# call the funtcion 'updatetool'
updatetool()
