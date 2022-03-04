#---[Metadata]-------------------------------------------------------#
#  Filename ~ update.sh                        [Update: 04-03-2022]  #
#---[Info]-----------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}  #
#                                                                    #
#  The update tool for have the latest version of ODST               #
#  Language  ~  Python3                                              #
#---[Author]---------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                    #
#  Copyright (C) 2022 MyMeepSQL - © Delta_Society™                   #
#---[Operating System]-----------------------------------------------#
#  Developed for linux                                               #
#--------------------------------------------------------------------#

#!/usr/bin/python3

import os
import sys
import importlib.util
from functions import *

if os.getuid() != 0:                                                            #   check if the user run update with root privilege
    print("The OmegaDSToolkit's update tool could be run with root privilege")  #
    print("Re-run the update.py with sudo")                                     #
    print('Run "sudo python3 update.py"')                                       #
    sys.exit()                                                                  #
else:                                                                           #
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
        print("+ ------------------- !* Updating OmegaDSToolkit repository *! ------------------- +")

        # For OmegaDSToolkit
        print("Update the latest version of OmegaDSToolkit...")
        os.system("rm -f OmegaDSToolkit.py")    
        os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/OmegaDSToolkit.py")
        print("Done\n")

        # For the setuptool
        print("Update the latest version of OmegaDSToolkit setuptool...")
        os.system("rm -f setup.py")              
        os.system("wget https://raw.githubusercontent.com/MyMeepSQL/OmegaDSToolkit/main/setup.py")
        print("Done\n")

        # Apply execute rights
        print("Apply execution rights to files...")
        os.system('chmod +x OmegaDSToolkit.py')
        os.system('chmod +x setup.py')

        print("Done\n")
        print('''Update complete! For be sure, run the setup.py with "sudo python3 setup.py install" before running ODST. 
After, you can run OmegaDSToolkit With "sudo python3 OmegaDSToolkit.py"''')





        sys.exit()

    except KeyboardInterrupt:
        print()
        print("CTRL + C detected, stoping the update phase...")
        sys.exit()