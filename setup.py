#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ setup.py                      [Update: 2022-03-13 | 17:00 PM] #
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
ghostwhite = '\033[1;37m'
reset = '\033[0m'
####

# Check if the user have a Internet connexion
# import urllib.request
# def connection(host='https://google.com'):              #
#     import urllib.request                               #
#     try:                                                #
#         urllib.request.urlopen(host)                    #
#         return True                                     #
#     except:                                             #
#         return False                                    #
####

version = "v2.1"

# The SetupTool
try:
    if os.getuid() != 0:                                                            #   check if the user run ODST with root privilege
        print("The SetupTool could be run with root privilege")                     #
        print("Re-run the setup.py with sudo")                                      #
        print('Run "sudo python3 setup.py install"')                                #
        sys.exit()                                                                  #
# If the user tries to run ODST from a non-Linux machine
except AttributeError:
    print()
    criticalmsg = blue+"["+red+"CRITICAL"+blue+"]"+reset+f" You tried to run ODST on a no-linux machine, ODST can be run only on a Linux kernel"+reset#
    exit(criticalmsg)
else:
    try:
        print()
        print(f"""
███████╗███████╗████████╗██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗ ██╗
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║
███████╗█████╗     ██║   ██║   ██║██████╔╝   ██║   ██║   ██║██║   ██║██║
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝    ██║   ██║   ██║██║   ██║██║
███████║███████╗   ██║   ╚██████╔╝██║        ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ {version}""")    # Police = ANSI Shadow from https://www.coolgenerator.com/ascii-text-generator
        print("+ ------------------ !* Welcome to the ODST setuptool. *! ------------------ +")
        print()
        print("+ ------------------------------------ +")
        print("   Checking for internet connexion...   ")
        print("+ ------------------------------------ +")
        print()
        
        try:
            urllib.request.urlopen('http://google.com')
            connexion = True
        except:
            connexion =  False

        if connexion == True:
            print("Internet status.......... "+lime+"Connected"+reset)
            pass
        else:
            print("Internet status.......... "+red+"Not connected"+reset)
            print("Not Internet connexion found, please check you are connected to Internet and retry.")
            sys.exit()

        print("The setup will install all pip packages that ODST needs and copy the OemgaDSToolkit path to \"/usr/share/OmegaDSToolkit\"")
        yn = str(input("Do you want to continue? [Y/n] "))

        if yn != 'y' and yn != 'Y':
            print("Abort.")
            sys.exit()
        elif not yn:
            print("Abort.")
            sys.exit()
        else:
            pass
        try:
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
                python_requires='>=3.1.0',
                packages=find_packages(),
                zip_safe=False,
                include_package_data=True,
                install_requires=[
                    'progress', 'colored'
                ],
            )
            print()
            print("+ -- --=[------------------------------------------------------------------]")
            print("+ -- --=[  Create OmegaDSToolkit folder to \"/usr/share/OmegaDSToolkit\"...  ]")
            print("+ -- --=[------------------------------------------------------------------]")

            os.system("sudo mkdir /usr/share/OmegaDSToolkit")

            print("+ -- --=[------------------------]")
            print("+ -- --=[  Done for the folder.  ]")
            print("+ -- --=[------------------------]")
            sleep(1)

            print()
            print()

            print("+ -- --=[-------------------------------------------------------------]")
            print("+ -- --=[  Copy the OmegaDSToolkit to \"/usr/share/OmegaDSToolkit\"...  ]")
            print("+ -- --=[-------------------------------------------------------------]")

            os.system("sudo cp -r * /usr/share/OmegaDSToolkit")

            print("+ -- --=[---------------------------------------]")
            print("+ -- --=[  Done for the OmegaDSToolkit's copy.  ]")
            print("+ -- --=[---------------------------------------]")
            sleep(1)

            print()
            print()

            print("+ -- --=[------------------------------------------------------------------]")
            print("+ -- --=[  Create the alias \"sudo \", \"omegadstoolkit\" and \"odstupdate\"...  ]")
            print("+ -- --=[------------------------------------------------------------------]")

            print()

            user = str(input("+ -- --=[  Type your current username: "))

            print()

            try:
                # make the alias for run odst just by typing "omegadstoolkit" to the current user ".bashrc" (home)
                if user != "root":
                    print("+ -- --=[--------------------------------------------------------------------------------]")
                    print(f"+ -- --=[  You username : {user} (not root user)                                        ")
                    print(f"+ -- --=[  Writing alias' into your \"/home/{user}/.bashrc\"...                         ")
                    print("+ -- --=[--------------------------------------------------------------------------------]")
                    sleep(1)

                    ##########################
                    # For /home/user/.bashrc #
                    ##########################

                    # Delete existing 'omegadstoolkit' alias (if exist)

                    ## 'omegadstoolkit' alias
                    ### Read file.txt
                    with open(f'/home/{user}/.bashrc', 'r') as file:
                        text = file.read()
                    ### Delete text and Write
                    with open(f'/home/{user}/.bashrc', 'w') as file:
                        #### Delete
                        new_text = text.replace("alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'", '')
                        #### Write
                        file.write(new_text)

                    ## 'odstupdate ' alias
                    ### Read file.txt
                    with open(f'/home/{user}/.bashrc', 'r') as file:
                        text = file.read()
                    ### Delete text and Write
                    with open(f'/home/{user}/.bashrc', 'w') as file:
                        #### Delete
                        new_text = text.replace("alias odstupdate='python3 /usr/share/OmegaDSToolkit/update.py'", '')
                        #### Write
                        file.write(new_text)

                    ## 'sudo ' alias
                    ### Read file.txt
                    with open(f'/home/{user}/.bashrc', 'r') as file:
                        text = file.read()
                    ### Delete text and Write
                    with open(f'/home/{user}/.bashrc', 'w') as file:
                        #### Delete
                        new_text = text.replace("alias sudo='sudo '", '')
                        #### Write
                        file.write(new_text)


                    # Writit aliases
                    alias =["alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'\n", "alias odstupdate='python3 /usr/share/OmegaDSToolkit/update.py'\n", "alias sudo='sudo '\n"]
                    with open(f"/home/{user}/.bashrc", "a") as aliasfile:
                        # Writing data to a file
                        aliasfile.writelines(alias)


                    ###############################
                    # For /root/.bashrc (in case) #
                    ###############################

                    # Delete existing 'omegadstoolkit' alias (if exist)

                    ## 'omegadstoolkit''s alias
                    ### Read file.txt
                    with open('/root/.bashrc', 'r') as file:
                        text = file.read()
                    ### Delete text and Write
                    with open('/root/.bashrc', 'w') as file:
                        #### Delete
                        new_text = text.replace("alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'", '')
                        #### Write
                        file.write(new_text)
                    
                    ## 'odstupdate ' alias
                    ### Read file.txt
                    with open(f'/home/{user}/.bashrc', 'r') as file:
                        text = file.read()
                    ### Delete text and Write
                    with open(f'/home/{user}/.bashrc', 'w') as file:
                        #### Delete
                        new_text = text.replace("alias odstupdate='python3 /usr/share/OmegaDSToolkit/update.py'", '')
                        #### Write
                        file.write(new_text)


                    # Writing alias
                    root_alias = ["alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'\n", "alias odstupdate='python3 /usr/share/OmegaDSToolkit/update.py'\n"]
                    with open("/root/.bashrc", "a") as aliasfile:
                        #### Writing data to a file
                        aliasfile.writelines(root_alias)

                else:
                    # make the alias for run odst just by typing "omegadstoolkit" to the root user ".bashrc" (root)
                    print("+ -- --=[--------------------------------------------------------------------------------]")
                    print(f"+ -- --=[  You username : {user} (root)")
                    print(f"+ -- --=[  Writing alias into your \"/root/.bashrc\"...")
                    print("+ -- --=[--------------------------------------------------------------------------------]")
                    sleep(1)


                    #####################
                    # For /root/.bashrc #
                    #####################

                    # Delete existing 'omegadstoolkit' alias (if exist)

                    ## 'omegadstoolkit''s alias
                    ### Read file.txt
                    with open('/root/.bashrc', 'r') as file:
                        text = file.read()
                    ### Delete text and Write
                    with open('/root/.bashrc', 'w') as file:
                        #### Delete
                        new_text = text.replace("alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'", '')
                        #### Write
                        file.write(new_text)
                    
                    ## 'odstupdate ' alias
                    ### Read file.txt
                    with open(f'/home/{user}/.bashrc', 'r') as file:
                        text = file.read()
                    ### Delete text and Write
                    with open(f'/home/{user}/.bashrc', 'w') as file:
                        #### Delete
                        new_text = text.replace("alias odstupdate='python3 /usr/share/OmegaDSToolkit/update.py'", '')
                        #### Write
                        file.write(new_text)


                    # Writing alias
                    root_alias = ["alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'\n", "alias odstupdate='python3 /usr/share/OmegaDSToolkit/update.py'\n"]
                    with open("/root/.bashrc", "a") as aliasfile:
                        #### Writing data to a file
                        aliasfile.writelines(root_alias)

            except FileNotFoundError:
                print()
                print(blue+"["+red+"ERROR"+blue+"]"+ghostwhite+f"""User '{user}' not found or file doesn't exist, check if you \".bashrc\" exist in your home repertory,
re-run the 'setup.py' and write a correct username\n"""+reset)
                sys.exit()

            print("+ -- --=[--------------------]")
            print("+ -- --=[  Done for alias'.  ]")
            print("+ -- --=[--------------------]")
            sleep(1)

            print()

            print("+ -- --=[-------------]")
            print("+ -- --=[  All done.  ]")
            print("+ -- --=[-------------]")

            print()
            print()

            print("+ -- --=[------------------------------------------------------------------------------------------------------------------------------]")
            print("+ -- --=[  All packages are install, now you can run OmegaDSToolkit with \"sudo omegadstoolkit\" (you can run omegadstoolkit anywhere).  ]")
            print("+ -- --=[------------------------------------------------------------------------------------------------------------------------------]")

        except EOFError:
            print()
            print("Abort.")
            sys.exit()

        except KeyboardInterrupt:
            print()
            print("Abort.")
            sys.exit()

    except EOFError:
        print()
        print("Abort.")
        sys.exit()

    except KeyboardInterrupt:
        print()
        print("Abort.")
        sys.exit()
####
