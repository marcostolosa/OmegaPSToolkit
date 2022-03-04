#---[Metadata]------------------------------------------------------#
#  Filename: setup.py                          [Update: 27-02-2022] #
#---[Info]----------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL} #
#                                                                   #
#  The setup of ODST                                                #
#  Language  ~  Python3                                             #
#---[Author]--------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                   #
#  Copyright (C) 2022 MyMeepSQL                                     #
#-------------------------------------------------------------------#

from setuptools import setup, find_packages
from time import sleep
import os, sys
import urllib.request
from functions import *

if os.getuid() != 0:                                                            #   check if the user run ODST with root privilege
    print("The OmegaDSToolkit's setup could be run with root privilege")        #
    print("Re-run the setup.py with sudo")                                      #
    print('Run "sudo python3 setup.py install"')                                #
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
        print("The setup will install all pip packages that he needs.")
        input("If you want to continue, press the [ENTER] to run the setup. Else press [CTRL + C] combination to exit the setup.")
        print()
        print("""
    ███████╗███████╗████████╗██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗ ██╗     
    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    ███████╗█████╗     ██║   ██║   ██║██████╔╝   ██║   ██║   ██║██║   ██║██║     
    ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝    ██║   ██║   ██║██║   ██║██║     
    ███████║███████╗   ██║   ╚██████╔╝██║        ██║   ╚██████╔╝╚██████╔╝███████╗
    ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝""")    # Police = ANSI Shadow from https://www.coolgenerator.com/ascii-text-generator
        print("~~~~~~~~~~~~~~~~~~~~~~~ Welcome to the ODST setuptool. ~~~~~~~~~~~~~~~~~~~~~~~")
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
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
        print(' Done! All packages are install, now you can run OmegaDSToolkit with "python3 OmegaDSToolkit.py" ')
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")

    except KeyboardInterrupt:
        print()
        print("CTRL + C detected, exiting the setup...")
        sys.exit()
