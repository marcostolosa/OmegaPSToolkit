#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ update.py                     [Update: 2022-03-04 | 14:23 PM] #
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
    print("Checking for Internet connection... ",end="")
    if connection() == True:
        print(lime+"Connected!"+reset)
        pass
    else:
        print(red+"Not Internet\n"+reset+"connexion found, please check you are connected to Internet and retry!")
        sys.exit()
    try:
        print("The update tool will be install the latest version of OmegaDSToolkit")
        input("If you want to continue, press the [ENTER] to run the update. Else press [CTRL + C] combination to exit the update tool.")
        print("""
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗████████╗ ██████╗  ██████╗ ██╗     
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗     ██║   ██║   ██║██║   ██║██║     
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝     ██║   ██║   ██║██║   ██║██║     
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗   ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝   
 """)   # Police = ANSI Shadow from https://www.coolgenerator.com/ascii-text-generator
        print("+ ------------------- !* UpdateTool for OmegaDSToolkit  *! ------------------- +")

        # For OmegaDSToolkit
        print("Update the latest version of OmegaDSToolkit...")

        # Removing the current locl OmegaDSToolkit
        os.system("rm -f OmegaDSToolkit.py")

        # Download ODST with wget from github raw
        os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/OmegaDSToolkit.py")
        print("Done\n")

        # For the setuptool
        print("Update the latest version of OmegaDSToolkit setuptool...")

        # Removing the current locl setuptool
        os.system("rm -f setup.py")

        # Download setuptool with wget from github raw
        os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/setup.py")
        print("Done\n")

        # Apply execute rights
        print("Apply execution rights to files...")
        os.system('chmod +x OmegaDSToolkit.py')     # for OmegaDSToolkit
        os.system('chmod +x setup.py')              # for the setuptool

        print("Done\n")
        print('''
Update complete! For be sure, run the setup.py with "sudo python3 setup.py install" before running ODST. 
After, you can run OmegaDSToolkit with "sudo python3 OmegaDSToolkit.py"''')
        sys.exit()

    except KeyboardInterrupt:
        print()
        print("CTRL + C detected, stoping the update tool...")
        sys.exit()
