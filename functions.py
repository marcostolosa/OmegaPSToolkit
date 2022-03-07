#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ functions.py                  [Update: 2022-03-07 | 14:22 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}         #
#                                                                           #
#  The file wich include all functions                                      #
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

try:
    import os,sys
    from colors import *
except ModuleNotFoundError:
    print()
    criticalmsg = blue+"["+red+"CRITICAL"+blue+"]"+ghostwhite+"   A current(s) module(s) was not installed, run the 'setup.py' for install it. (sudo setup.py install)\n"
    exit(criticalmsg)
except NameError:
    print()
    criticalmsg = blue+"["+red+"CRITICAL"+blue+"]"+ghostwhite+"   A current(s) module(s) was not installed, run the 'setup.py' for install it. (sudo setup.py install)\n"
    exit(criticalmsg)

# Functions
def connection(host='https://google.com'):              #
    import urllib.request                               #
    try:                                                #
        urllib.request.urlopen(host)                    #
        return True                                     #
    except:                                             #   Check if the user have an Internet connection
        return False                                    #
    
def cls():
    os.system('clear')

def exitodst():
    print(bC+"["+gC+"Goodby"+bC+"]"+r)
    exit()

def error():
    print(bC+"["+rC2+"!"+bC+"]"+bC+"─["+gC+"Choose a option"+bC+"]"+r)                  # if the user doesn't choose option
    input(bC+"["+rC2+"-"+bC+"]"+bC+"─["+gC+"Press [ENTER] key to continue"+bC+"]"+r)    #

def y_or_n_error():
    print(bC+"["+rC2+"!"+bC+"]"+bC+"─["+gC+"Chose y or n"+bC+"]"+r)                     # If the user does not choose "y" or "n"
    input(bC+"["+rC2+"-"+bC+"]"+bC+"─["+gC+"Press [ENTER] key to retry"+bC+"]"+r)       #

def cli_helpmsg():
    print()
    print("All commands of the OmegaDSToolkit you can use is the main page\n")
    print("""COMMAND:
    1           ::   Go to the Information Gathering page
    2           ::   Go to the Wireless Tools page
    3           ::   Go to the Usefull tools page
    cli         ::   Use the OmegaDSToolkit like a CLIy
    help        ::   Print this help message
    exit        ::   Exit the OmegaDSToolkit""")
    input(bC+"["+rC2+"-"+bC+"]"+bC+"─["+gC+"Press [ENTER] key to continue"+bC+"]"+r)

def helpmsg():
    print()
    print("All commands of the OmegaDSToolkit you can use is the main page\n")
    print("""COMMAND:
    1           ::   Go to the Information Gathering page
    2           ::   Go to the Wireless Tools page
    3           ::   Go to the Usefull tools page
    cli         ::   Use the OmegaDSToolkit like a CLI
    help        ::   Print this help message
    exit        ::   Exit the OmegaDSToolkit""")
# End of functions section


