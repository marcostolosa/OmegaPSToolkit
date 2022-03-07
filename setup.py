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

import os,sys
from setuptools import setup,find_packages
from time import sleep

red = '\033[1;31m'
lime = '\033[1;32m'
reset = '\033[0m'

def connection(host='https://google.com'):              #
    import urllib.request                               #
    try:                                                #
        urllib.request.urlopen(host)                    #
        return True                                     #
    except:                                             #   Check if the user have an Internet connection
        return False                                    #

if os.getuid() != 0:                                                            #   check if the user run ODST with root privilege
    print("The OmegaDSToolkit's setup could be run with root privilege")        #
    print("Re-run the setup.py with sudo")                                      #
    print('Run "sudo python3 setup.py install"')                                #
    sys.exit()                                                                  #
else:                                                                           #
    print("Checking for Internet connection.......... ",end="")
    if connection() == True:
        print(lime+"Connected!"+reset)
        pass
    else:
        print(red+"Not Connected"+reset)
        print("Not Internet connexion found, please check you are connected to Internet and retry!")
        sys.exit()
    try:
        print("The setup will install all pip packages that ODST needs ")
        input("If you want to continue, press the [ENTER] key to run the setup. Else press [CTRL + C] to exit the setup.")
        print()
        print("""
███████╗███████╗████████╗██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗ ██╗
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║
███████╗█████╗     ██║   ██║   ██║██████╔╝   ██║   ██║   ██║██║   ██║██║
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝    ██║   ██║   ██║██║   ██║██║
███████║███████╗   ██║   ╚██████╔╝██║        ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝""")    # Police = ANSI Shadow from https://www.coolgenerator.com/ascii-text-generator
        print("~~~~~~~~~~~~~~~~~~~~~~ Welcome to the ODST setuptool. ~~~~~~~~~~~~~~~~~~~~~~")
        sleep(1.2)
        print()
        requirements = ["requests"]

        setup_requirements = ["requests"]

        test_requirements = ["requests"]

        setup(classifiers=[
                "Copyright                          :: Copyright (C) 2022, Thomas Pellissier aka MyMeepSQL",
                "Author codename                    :: MyMeepSQL",
                "Developed for                      :: Linux",
                "Development Status                 :: 2 - Production/Stable",
                "Natural Language                   :: English",
                "Environment                        :: Terminal",
                "Intended Audience                  :: Developers",
                "Programming Language               :: Python :: 3.10-3.10.X",
                "Programming Language compatible    :: Python :: 3.1-3.x.x",
            ],
            name='OmegaDSToolkit',
            description='A massive penetration testing toolkit',
            url='https://github.com/MyMeepSQL/OmegaDSToolkit',
            author='Thomas Pellissier',
            author_email='thomas.pellissier@outlook.com',
            license='GNU-GPL-3.0',
            keywords="omegadstoolkit",
            version='0.0.0.8',
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
        print("CTRL + C detected, exiting the setup...")
        sys.exit()
