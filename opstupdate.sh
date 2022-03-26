#!/bin/bash

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstupdate.sh                 [Update: 2022-03-24 | 10:00 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The UpdateTool for have the latest version of all OPST commands          #
#  Language  ~  Bash                                                        #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright (C) 2022 MyMeepSQL - © PSociety™                               #
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

# Colors
## Basic colors
W='\033[0m'      # white (normal)
R='\033[31m'     # red
G='\033[32m'     # green
O='\033[33m'     # orange
B='\033[34m'     # blue
P='\033[35m'     # purple
C='\033[36m'     # cyan
GR='\033[37m'    # gray
D='\033[2m'      # dims current color. $W resets.

## Text formating
bold='\033[1m'
dark='\033[2m'
italic='\033[3m'
underscore='\033[4m'
normal='\033[22m'
####

opstupdate_version="v1.8"
INSTALL_DIR="/usr/share/OmegaPSToolkit"
BIN_DIR="/usr/share/"

# Check if user have root privileges
if [ $(id -u) != "0" ]; then
    # Many fresh installed linux distros do not come with sudo installed
    which sudo > /dev/null 2>&1
    if [ "$?" != "0" ]; then
        echo "$R[!]$W   You Linux distribution doesn't have the \"sudo\" command pre-install. Install the current \"sudo\" command..."
        sleep 1
        apt update -y && apt-get install sudo -y
    fi
    ####
        if ! hash sudo 2>/dev/null; then
                echo "$R[!]$W    OPSTUpdate could be run as the 'root' user or with 'sudo'"
                echo "       Re-run the 'opstupdate.sh' with sudo or with the root user"
                echo '       Run sudo "sudo opstupdate"'
                exit 1
        else # Switch to sudo (root)
            echo
            echo "$R[!]$W    OPSTUpdate could be run as the 'root' user or with 'sudo'"
            echo "$G[-]$W    Switching to root user to run the 'opstupdate'"
            sudo -E sh $0 $@
            exit 0
        fi
    fi
####

# The main script

echo
echo "$GR$D _______ ______ _______ _______ _______           __         __ $W"
echo "$GR$D|       |   __ \     __|_     _|   |   |.-----.--|  |.---.-.|  |_.-----.$W$G  OPSTUpdate $D$opstupdate_version"
echo "$GR$D|   -   |    __/__     | |   | |   |   ||  _  |  _  ||  _  ||   _|  -__|$W$D  A massive penetration testing toolkit"          # Police = Chunky from https://www.coolgenerator.com/ascii-text-generator
echo "$GR$D|_______|___|  |_______| |___| |_______||   __|_____||___._||____|_____|$C$D  https://github.com/MyMeepSQL/OmegaPSToolkit$W"
echo "$GR$D +- !* Welcome to the OPSTUpdate. *! -+ |__|$W"
echo
echo "$G[-]$W    Checking for internet connexion..."
echo

#First check of setup for internet connection by connecting to google over http
wget -q --tries=10 --timeout=5 --spider http://google.com
if [ $? -eq 0 ]; then
    echo '+ -- --=[  Internet status.......... '"$G"'Connected'"$W"'.                                                              ]'
    echo '+ -- --=[  '$underscore'This tool will:'$W'                                                                                   ]
        [  ...'$G'Install'$W' the latest verion of '$R'OPSTConsole'$W', '$R'OPSTHelp'$W', '$R'OPSTUpdate'$W', '$R'OPSTInstall-all'$W' and '$R'OPSTSetup'$W'  ]'
    echo
    echo -n "$C[?]$W    Do you want to continue? [Y/n] "
    read y_n
    if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ]; then
        echo
        echo "$G$D""--------------------------------------------------------------------------------------"$W
        echo
        echo "$G[-]$W    Removing the current OPST's commands from '"$G"/usr/share/OmegaPSToolkit"$W"'..."
        rm -fr "$INSTALL_DIR/opstconsole.py"
        rm -fr "$INSTALL_DIR/opsthelp.py"
        rm -fr "$INSTALL_DIR/opstupdate.py"
        rm -fr "$INSTALL_DIR/opstsetup.py"
        rm -fr "$INSTALL_DIR/opstinstall-all.sh"

        rm -fr "$INSTALL_DIR/opstfunctions.py"
        rm -fr "$INSTALL_DIR/opstcolors.py"
        rm -fr "$INSTALL_DIR/opstversions.py"

        echo "$G[+]$W    Done for the OPST's commands remove."
        echo
        sleep 1
        echo "$G$D""--------------------------------------------------------------------------------------"$W
        echo
        echo "$G[-]$W    "$G"Updating"$W" all commands from "$G"GitHub"$W"..."
        echo
        sleep 0.5

        wget https://raw.githubusercontent.com/MyMeepSQL/OmegaPSToolkit/main/opstconsole.py -P /usr/share/OmegaPSToolkit/opstconsole.py
        wget https://raw.githubusercontent.com/MyMeepSQL/OmegaPSToolkit/main/opsthelp.py -P /usr/share/OmegaPSToolkit/opsthelp.py
        wget https://raw.githubusercontent.com/MyMeepSQL/OmegaPSToolkit/main/opstupdate.py -P /usr/share/OmegaPSToolkit/opstupdate.py
        wget https://raw.githubusercontent.com/MyMeepSQL/OmegaPSToolkit/main/opstsetup.py -P /usr/share/OmegaPSToolkit/opstsetup.py
        wget https://raw.githubusercontent.com/MyMeepSQL/OmegaPSToolkit/main/opstinstall-all.sh -P /usr/share/OmegaPSToolkit/opstinstall-all.sh

        wget https://raw.githubusercontent.com/MyMeepSQL/OmegaPSToolkit/main/opstfunctions.py -P /usr/share/OmegaPSToolkit/opstfunctions.py
        wget https://raw.githubusercontent.com/MyMeepSQL/OmegaPSToolkit/main/opstcolors.py -P /usr/share/OmegaPSToolkit/opstcolors.py
        wget https://raw.githubusercontent.com/MyMeepSQL/OmegaPSToolkit/main/opstversions.py -P /usr/share/OmegaPSToolkit/opstversions.py

        echo "#!/bin/bash
        python3 $INSTALL_DIR/opstconsole.py" '${1+"$@"}' > opstconsole
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opstupdate.py" '${1+"$@"}' > opstupdate
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opstsetup.py" '${1+"$@"}' > opstsetup
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opsthelp.py" '${1+"$@"}' > opsthelp
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opstinstall-all.sh" '${1+"$@"}' > opstinstall-all

        sudo cp opstconsole /usr/bin/
        sudo cp opstupdate /usr/bin/
        sudo cp opstsetup /usr/bin/
        sudo cp opsthelp /usr/bin/
        sudo cp opstinstall-all /usr/bin/

        sudo rm opstconsole
        sudo rm opstupdate
        sudo rm opstsetup
        sudo rm opsthelp
        sudo rm opstinstall-all

        echo
        echo "$G[+]$W    Update complete."
        echo
        sleep 1
        echo "$G$D""--------------------------------------------------------------------------------------"$W
        echo

        # Apply all rights
        echo "$G[-]$W    Apply all rights to files..."
        sleep 0.5

        # for '/usr/share/OmegaPSToolkit'
        chmod 777 /usr/share/OmegaPSToolkit/opstconsole.py
        chmod 777 /usr/share/OmegaPSToolkit/opstupdate.sh
        chmod 777 /usr/share/OmegaPSToolkit/opstsetup.py
        chmod 777 /usr/share/OmegaPSToolkit/opstinstall-all.sh
        chmod 777 /usr/share/OmegaPSToolkit/opsthelp.py

        chmod 777 /usr/share/OmegaPSToolkit/opstfunctions.py
        chmod 777 /usr/share/OmegaPSToolkit/opstcolors.py
        ##

        # for '/usr/bin'
        chmod 777 /usr/bin/opstconsole
        chmod 777 /usr/bin/opstupdate
        chmod 777 /usr/bin/opstsetup
        chmod 777 /usr/bin/opstinstall-all
        chmod 777 /usr/bin/opsthelp
        ##

        echo "$G[+]$W    Apply complete."
        sleep 1
        echo
        echo "$G$D""--------------------------------------------------------------------------------------"$W
        echo
        echo "$B[+]$W    All Done."
        echo
        sleep 1
        echo "$G$D""--------------------------------------------------------------------------------------"$W
        echo
        echo -n "$C[?]$W    Do you want to reload your terminal (just in case) ? [Y/n] "
        read y_n
        if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ]; then
            echo
            echo "$G$D""--------------------------------------------------------------------------------------"$W
            echo
            echo "$G$D""---------------------"$W
            echo "$G[-]$W    Reloading..."
            echo "$G$D""---------------------"$W
            sleep 0.5
            reset
            echo
            echo "$G$D""---------------------------------------------------------------------------------------------------------------------------------------------------------"$W
            echo
            echo "$B[OK]$W    '$R'OPSTConsole'$W', '$R'OPSTHelp'$W', '$R'OPSTUpdate'$W', '$R'OPSTInstall-all'$W' and '$R'OPSTSetup'$W' are now install with the latest version exist from GitHub."
            echo
            echo "$G$D""---------------------------------------------------------------------------------------------------------------------------------------------------------"$W
            echo
            exit 0
        else
            echo
            echo "$G$D""--------------------"$W
            echo "$B$D[+]$W    Answer: "$R"No"$W"."
            echo "$G$D""--------------------"$W
            echo
            echo "$G$D""---------------------------------------------------------------------------------------------------------------------------------------------------------"$W
            echo
            echo "$B[OK]$W    '$R'OPSTConsole'$W', '$R'OPSTHelp'$W', '$R'OPSTUpdate'$W', '$R'OPSTInstall-all'$W' and '$R'OPSTSetup'$W' are now install with the latest version exist from GitHub."
            echo
            echo "$G$D""---------------------------------------------------------------------------------------------------------------------------------------------------------"$W
            echo
            exit 0
        fi
    else
        echo "$GR$D[-]$W    Abort."
        exit 1
    fi
else
    echo "$R[!]$W   Internet status.......... "$R"Not connected"$W"."
    echo "$R[*]$W   Not Internet connexion found, please check you are connected to Internet and retry."
    exit 1
fi
