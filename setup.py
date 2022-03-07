#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ setup.py                      [Update: 2022-03-07 | 14:21 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}         #
#                                                                           #
#  The SetupTool for ODST                                                   #
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

# Import Section
import urllib.request
import os,sys
from setuptools import setup,find_packages
from time import sleep
####

# Colors
red = '\033[1;31m'
lime = '\033[1;32m'
blue = '\033[1;34m'
reset = '\033[0m'
####

# The SetupTool
try:
    if os.getuid() != 0:                                                            #   check if the user run ODST with root privilege
        print("The OmegaDSToolkit's setup could be run with root privilege")        #
        print("Re-run the setup.py with sudo")                                      #
        print('Run "sudo python3 setup.py install"')                                #
        sys.exit()                                                                  #
# If the user tries to run ODST from a non-Linux machine
except AttributeError:
    print()
    criticalmsg = blue+"["+red+"CRITICAL"+blue+"]"+red+" You tried to run ODST on a no-linux machine, ODST can be run only on a Linux kernel"+reset#
    exit(criticalmsg)
else:
    try:
        print()
        print("""
███████╗███████╗████████╗██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗ ██╗
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║
███████╗█████╗     ██║   ██║   ██║██████╔╝   ██║   ██║   ██║██║   ██║██║
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝    ██║   ██║   ██║██║   ██║██║
███████║███████╗   ██║   ╚██████╔╝██║        ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝""")    # Police = ANSI Shadow from https://www.coolgenerator.com/ascii-text-generator
        print("+ ------------------ !* Welcome to the ODST setuptool. *! ------------------ +")
        print()
        print("+ ----------------------------------- +")
        print("  Checking for internet connection...")
        print("+ ----------------------------------- +")
        print()
        try:
            urllib.request.urlopen('https://google.com')
            connection = True
        except:
            connection =  False

        if connection == True:
            print("Internet status.......... "+lime+"Connected"+reset)
            pass
        else:
            print("Internet status.......... "+red+"Not connected"+reset)
            print("Not Internet connexion found, please check you are connected to Internet and retry.")
            sys.exit()

        print("The setup will install all pip packages that ODST needs ")
        yn = str(input("Do you want to continue? [Y/n] "))

        if yn != 'y' and yn != 'Y':
            print("Abort.")
            sys.exit()
        elif not yn:
            print("Abort.")
            sys.exit()
        else:
            pass

        requirements = ["requests"]
        setup_requirements = ["requests"]
        test_requirements = ["requests"]
        setup(classifiers=[
                "Copyright                          :: Copyright (C) 2022, Thomas Pellissier aka MyMeepSQL from © Delta_Society™",
                "Author                             :: Thomas Pellissier",
                "Developed for                      :: Linux",
                "Development Status                 :: 2 - In Development",
                "Natural Language                   :: English",
                "Environment                        :: Terminal",
                "Intended Audience                  :: Developers, Sec.",
                "Programming Language               :: Python :: 3.10-3.10.X",
                "Programming Language compatible    :: Python :: 3.1-3.x.x",
                "Other Programming Language         :: Bash (Linux)",
            ],
            name='OmegaDSToolkit',
            description='A massive penetration testing toolkit',
            url='https://github.com/MyMeepSQL/OmegaDSToolkit',
            author='MyMeepSQL',
            author_email='thomas.pellissier@outlook.com',
            license='GNU-GPL-3.0',
            keywords="omegadstoolkit",
            version='0.0.1.3',
            python_requires='>3.1.0',
            packages=find_packages(),
            zip_safe=False,
            include_package_data=True,
            install_requires=[
                'progress', 'colored', 'nslookup', 'keyboard',
                'pythonping'
            ],
        )
        print()
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
        print(' Done! All packages are install, now you can run OmegaDSToolkit with "sudo python3 OmegaDSToolkit.py" ')
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")


    except KeyboardInterrupt:
        print()
        print("Abort.")
        sys.exit()
####