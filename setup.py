#---[Metadata]-----------------------------------------------------#
#  Filename: setup.py                         [Update: 05-01-2022] #
#---[Info]---------------------------------------------------------#
#  The setup for had all modules that the ODST use                 #
#  Language      - Python3                                         #
#---[Author]-------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                  #
#------------------------------------------------------------------#



#-Check module is installed------------------------------------------#
def install(package):
    pip.main(['install', package])
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import pip
import os
from time import sleep
cls()

print("""  /$$$$$$              /$$                      /$$$$$$$$                  /$$
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
print("================== Welcome to the ODST modules verification. ==================")
sleep(1.5)
print("                 Checking if the ODST modules are installed...    ")
sleep(0.6)
print()

### for time
# print('Checking for "time"...')
sleep(0.3)
try:
    import time
    # print("Time is already installed")
    # print()
    # sleep(1)
except ImportError:
    print("Time is not installed, I install it.")
    install('time')
    print()
    print("Done")

### for progress
import pip
# print('Checking for "progress"...')
sleep(0.3)
try:
    import progress
    # print("Progress is already installed")
    # print()
    # sleep(1)
except ImportError:
    print("Progress is not installed, I install it.")
    install('progress')
    print()
    print("Done")

### for colored
import pip
# print('Checking for "colored"...')
sleep(0.3)
try:
    import colored
    # print("Colored is already installed")
    # # print()
    # sleep(1)
except ImportError:
    print("Colored is not installed, I install it.")
    install('colored')
    print()
    print("Done")

### for nslookup
import pip
# print('Checking for "nslookup"...')
sleep(0.3)
try:
    import nslookup
    # print("Nslookup is already installed")
    # print()
    # sleep(1)
except ImportError:
    print("Nslookup is not installed, I install it.")
    install('nslookup')
    print()
    print("Done")

### for keyboard
import pip
# print('Checking for "keyboard"...')
sleep(0.3)
try:
    import keyboard 
    # print("Keyboard is already installed")
    # print()
except ImportError:
    print("keyboard is not installed, I install it.")
    install('keyboard')
    print()
    print("Done")

### for pythonping
import pip
# print('Checking for "pythonping"...')
sleep(0.3)
try:
    import pythonping
    # print("pythonping is already installed")
    # print()
except ImportError:
    print("Pythonping is not installed, I install it.")
    install('pythonping')
    print()
    print("Done")

print()
print("<========================================================================================================================>")
print(' Done! All modules are install, now go to the OmegaDSTookit folder and start it with `python OmegaDSToolkit[v0.0.0.6].py`')
print("<========================================================================================================================>")
