#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ update.py                     [Update: 2022-03-07 | 11:51 AM] #
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

from functions import *

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
        print("""
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗████████╗ ██████╗  ██████╗ ██╗
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗     ██║   ██║   ██║██║   ██║██║
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝     ██║   ██║   ██║██║   ██║██║
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗   ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝""")   # Police = ANSI Shadow from https://www.coolgenerator.com/ascii-text-generator
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

        while not yn:
            yn = str(input("Do you want to continue? [Y/n] "))
        if yn != 'y' and yn != 'Y':
            print("Abort.")
            sys.exit()
        else:
            pass

        # For OmegaDSToolkit
        print("Download the latest version of OmegaDSToolkit...")
        ## Removing the current local OmegaDSToolkit
        os.system("rm -f OmegaDSToolkit.py")
        ## Download OmegaDSToolkit with wget from github raw
        os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/OmegaDSToolkit.py")
        print("Done for OmegaDSToolkit\n")

        # For the SetupTool
        print("Download the latest version of OmegaDSToolkit setuptool...")
        ## Removing the current locl SetupTool
        os.system("rm -f setup.py")
        ## Download SetupTool with wget from github raw
        os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/setup.py")
        print("Done the SetupTool\n")

        # For the InstallTool
        print("Download the latest version of OmegaDSToolkit setuptool...")
        ## Removing the current locl InstallTool
        os.system("rm -f install.py")
        ## Download InstallTool with wget from github raw
        os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/install.sh")
        print("Done the InstallTool\n")

        # Apply all rights to the new files
        print("Apply all rights to the new files...")
        os.system('chmod +xrw OmegaDSToolkit.py')     # for the OmegaDSToolkit
        os.system('chmod +xrw setup.py')              # for the SetupTool
        os.system('chmod +xrw install.sh')            # for the InstallTool

        print("Done\n")
        print('''
Update complete! For be sure, run the setup.py with "sudo python3 setup.py install" before running ODST. 
After, you can run OmegaDSToolkit with "sudo python3 OmegaDSToolkit.py"''')
        sys.exit()

    except KeyboardInterrupt:
        print()
        print("CTRL + C detected, stoping the update tool...")
        sys.exit()