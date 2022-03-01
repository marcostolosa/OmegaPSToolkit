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

#-First-colors section-----------------------------------------------#

### Color for the starting's page (modules checker)
# Basic color's
gray ="\033[30m"
red = "\033[1;31m"
lime = "\033[1;32m"
orange = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
light_blue = "\033[1;36m"
ghostwhite = "\033[1;37m"

# Light color's
cyan = "\033[36m"
white = "\033[37m"
light_gray = "\033[90m"
light_red = "\033[91m"
light_lime = "\033[92m"
light_yellow = "\033[93m"
light_blue2 = "\033[94m"
light_purple = "\033[95m"

# Dark color's
darkblack = "\033[0,30m"
darkred = "\033[0,31m"
darkgreen = "\033[0,32m"
darkyellow = "\033[0,33m"
darkblue = "\033[0,34m"
darkmagenta = "\033[0,35m"
darkcyan = "\033[0,36m"
darkwhite = "\033[0,37m"

# Text formating
reset = "\033[0m"
bold = '\033[1m'
dark = "\033[2m"
italic = "\033[3m"
underscore = "\033[4m"
normal = "\033[22m"
###

#-End-of-the-first-colors section------------------------------------#

from setuptools import setup, find_packages
from time import sleep
import os, sys
import urllib.request

## Check for Internet connexion status
def connection(host='https://google.com'):              #
    try:                                                #
        urllib.request.urlopen(host)                    #
        return True                                     #
    except:                                             #   Check if the user have an Internet connection 
        return False                                    #
if connection() == True:                                #
    connectionstatus = (lime+"Connected"+reset)         #
else:                                                   #
    connectionstatus = (red+"No Internet"+reset)        #

if os.getuid() != 0:                                                            #   check if the user run ODST with root privilege
    print("The OmegaDSToolkit's setup could be run with root privilege")        #
    print("Re-run the setup.py with sudo")                                      #
    print('Run "sudo python3 setup.py install"')                                #
    sys.exit()                                                                  #
else:                                                                           #
    print("Checking for Internet connexion... ",end="")
    if connection() == True:
        print("Connected!")
        pass
    else:
        print("Not Internet connexion found, please check you are connected to Internet and retry!")
        sys.exit()
    try:
        print("The setup will install all pip packages that he needs.")
        input("If you want to continue, press the [ENTER] to run the setup. Else press [CTRL + C] combination to exit the setup.")
    except KeyboardInterrupt:
        print()
        print("CTRL + C detected, exiting the setup...")
        sys.exit()
    

    print()
    print("""
    /$$$$$$              /$$                      /$$$$$$$$                  /$$
    /$$__  $$            | $$                     |__  $$__/                 | $$
    | $$  \__/  /$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$ | $$  /$$$$$$   /$$$$$$ | $$
    |  $$$$$$  /$$__  $$|_  $$_/  | $$  | $$ /$$__  $$| $$ /$$__  $$ /$$__  $$| $$
    \____  $$| $$$$$$$$  | $$    | $$  | $$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$
    /$$  \ $$| $$_____/  | $$ /$$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$
    |  $$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$/| $$$$$$$/| $$|  $$$$$$/|  $$$$$$/| $$
    \______/  \_______/   \___/   \______/ | $$____/ |__/ \______/  \______/ |__/
                                            | $$
                                            | $$
                                            |__/
    """,end="")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to the ODST setuptool. ~~~~~~~~~~~~~~~~~~~~~~~~~")
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
    print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
    print(' Done! All modules are install, now go to the OmegaDSTookit folder and start it with "python3 OmegaDSToolkit[v0.0.0.8].py"')
    print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")