#!/bin/bash

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstinstall-all.sh             [Update: 2022-05-04 | 9:42 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The tool for install Python3,PIP3 and write all command into the         #
#  /usr/bin/                                                                #
#                                                                           #
#  Language  ~  Bash                                                        #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright (C) 2022 MyMeepSQL - © PSociety™, 2022 All rights reserved     #
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
D='\033[2m'      # dims current color. {W} resets.

## Text formating
bold='\033[1m'
italic='\033[3m'
underscore='\033[4m'
normal='\033[22m'
####

opstinstallall_version="v2.2"

INSTALL_DIR="/usr/share/OmegaPSToolkit"
BIN_DIR="/usr/bin"
TEMP_DIR="/tmp/OmegaPSToolkit"

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
            echo -e " 
$R[!]$W  OPSTInstall-all could be run as the$R root user$W or with the$R sudo command$W
     Re-run the opstinstall-all with$R sudo$W or with the$R root$W user
     Run :$B sudo opstinstall-all $W"
                exit 1
        else # Switch to sudo (root)
            echo
            echo -e "
$R[!]$W  OPSTInstall-all could be run as the$R root user$W or with the$R sudo command$W
$G[-]$W  Switching to$R root user$W to run the$B opstinstall-all$W
"
            sudo -E bash $0 $@
            exit 0
        fi
    fi
####

# The main script
clear
echo -e "
$GR$D _______ ______ _______ _______ _______               __          __ __               __ __ $W$G  OPSTInstall-all $D$opstinstallall_version
$GR$D|       |   __ \     __|_     _|_     _|.-----.-----.|  |_.---.-.|  |  |______.---.-.|  |  |$G$D  Coded by MyMeepSQL for © PSociety™
$GR$D|   -   |    __/__     | |   |  _|   |_ |     |__ --||   _|  _  ||  |  |______|  _  ||  |  |$W$D  A massive penetration testing toolkit
$GR$D|_______|___|  |_______| |___| |_______||__|__|_____||____|___._||__|__|      |___._||__|__|$C$D  https://github.com/MyMeepSQL/OmegaPSToolkit$W
$GR$D + ------------------------ !* Welcome to the OPSTInstall-all *! ------------------------ +$W

$G[-]$W  Checking for internet connection...
"

#First check of setup for internet connection by connecting to google over http
wget -q --tries=10 --timeout=5 --spider http://google.com
if [ $? -eq 0 ]; then
    echo -e '+ -- --=[  Internet status.......... '"$G"'Connected'"$W"'.                                                                                       ]'
    echo -e '+ -- --=[  '$underscore'This tool will:'$W'                                                                                                            ]
        [  ...'$G'Update'$W' your system ('$R'apt update'$W'),                                                                                        ]
        [  ...Install '$G'Python3'$W' and '$G'PIP3'$W' ('$R'apt install python3 python3-pip'$W'),                                                             ]
        [  ...Install all '$G'tools'$W' that OPST must have                                                                                   ]
        [  ...Create the OmegaPSToolkit folder to "'$G'/usr/share/OmegaPSToolkit/'$W'" and '$R'clone OmegaPSToolkit files into it'$W' (from'$R' GitHub'$W'),  ]
        [  ...Create the commands "'$G'opstconsole'$W'", "'$G'opsthelp'$W'", "'$G'opstupdate'$W'", "'$G'opstsetup'$W'" and "'$G'opstinstall-all'$W'" into '$G'/usr/bin/'$W',          ]
        [  ...Apply all rights on the new file in "'$G'/usr/share/OmegaPSToolkit/'$W'" and for all commands in "'$G'/usr/bin/'$W'".                   ]'
    echo
    echo -ne "$C[?]$W  Do you want to continue? [Y/n] "
    read y_n
    if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ] || [ ! "$y_n" ]; then
        echo -e "
$G$D--------------------------------------------------------------------------------------$W

$G[-]$W  Updating..."
        sleep 0.5
        sudo apt-get install git htop -qq > /dev/null
        apt-get update -qq -y > /dev/null && apt-get update -qq --fix-missing -y > /dev/null
        echo -e "$G[+]$W  Update complete."
        sleep 1
        echo -e "
$G$D--------------------------------------------------------------------------------------$W

$G[-]$W  Installing Python3 and PIP3..."
        sleep 0.5
        apt-get install git python3 python3-pip whois traceroute net-tools -qq -y > /dev/null
        echo -e "$G[+]$W  Installation complete."
        sleep 1
        echo -e "
$G$D--------------------------------------------------------------------------------------$W
"
        if [ -d "$INSTALL_DIR" ]; then
            echo -e "$R[!]$W  A OmegaPSToolkit directory was Found."
            echo -ne "$C[?]$W  Do you want to replace it ? [Y/n] "
            read y_n
            if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ] || [ ! "$y_n" ]; then
                echo -e "
$G$D---------------------$W
$B$D[+]$W  Answer: "$G"Yes$W.
$G$D---------------------$W

$G[-]$W  Removing the current OmegaPSToolkit folder..."
                rm -fr "$INSTALL_DIR"
                rm -fr "$TEMP_DIR"
                rm -f "$BIN_DIR/opstconsole"
                rm -f "$BIN_DIR/opstsetup"
                rm -f "$BIN_DIR/opstupdate"
                rm -f "$BIN_DIR/opsthelp"
                rm -f "$BIN_DIR/opstinstall-all"

                echo -e "$G[+]$W  Done for the OmegaPSToolkit's remove."
                sleep 1
                echo -e "
$G$D--------------------------------------------------------------------------------------$W
"
            else
                echo -e "
$G$D--------------------$W
$B$D[+]$W  Answer: "$R"No$W.
$G$D--------------------$W

$GR$D[-]$W  Exiting opstinstall-all..."
                exit 1
            fi
        fi

        # for run the SetupTool (opstsetup) anywhere in the terminal. The "opstsetup" will be write into "/usr/share/OmegaPSToolkit"
        echo -e "$G[-]$W  Installing OmegaPSToolkit into \"/usr/share/OmegaPSToolkit/\"..."
        sleep 0.5

        mkdir $INSTALL_DIR
        mkdir $TEMP_DIR

        git clone -q https://github.com/MyMeepSQL/OmegaPSToolkit.git "$TEMP_DIR"

        # for the "/usr/share/OmegaPSToolkit"
        cp -r "$TEMP_DIR/"* "$INSTALL_DIR/"
        ##

        # for the "/usr/bin"
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opstconsole.py" '${1+"$@"}' > "$TEMP_DIR/opstconsole"
        echo "#!/bin/bash
        bash $INSTALL_DIR/opstupdate.sh" '${1+"$@"}' > "$TEMP_DIR/opstupdate"
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opstsetup.py" '${1+"$@"}' > "$TEMP_DIR/opstsetup"
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opsthelp.py" '${1+"$@"}' > "$TEMP_DIR/opsthelp"
        echo "#!/bin/bash
        bash $INSTALL_DIR/opstinstall-all.sh" '${1+"$@"}' > "$TEMP_DIR/opstinstall-all"

        cp "$TEMP_DIR/opstconsole" "$BIN_DIR"
        cp "$TEMP_DIR/opstupdate" "$BIN_DIR"
        cp "$TEMP_DIR/opstsetup" "$BIN_DIR"
        cp "$TEMP_DIR/opsthelp" "$BIN_DIR"
        cp "$TEMP_DIR/opstinstall-all" "$BIN_DIR"

        rm -fr "$TEMP_DIR"
        ##

        echo -e "$G[+]$W  Done for the OmegaPSToolkit's installation."
        sleep 1
        echo -e "
$G$D--------------------------------------------------------------------------------------$W
"

        # Apply all rights
        echo -e "$G[-]$W  Apply all rights to files..."
        sleep 0.5

        # for '/usr/share/OmegaPSToolkit'
        chmod 777 -R "$INSTALL_DIR"

        # chmod 777 "$INSTALL_DIR/opstconsole.py"
        # chmod 777 "$INSTALL_DIR/opstupdate.sh"
        # chmod 777 "$INSTALL_DIR/opstsetup.py"
        # chmod 777 "$INSTALL_DIR/opstinstall-all.sh"
        # chmod 777 "$INSTALL_DIR/opsthelp.py"

        # chmod 777 "$INSTALL_DIR/opstfunctions.py"
        # chmod 777 "$INSTALL_DIR/opstcolors.py"
        # chmod 777 "$INSTALL_DIR/opstversions.py"
        ##

        # for '/usr/bin'
        chmod 777 "$BIN_DIR/opstconsole"
        chmod 777 "$BIN_DIR/opstupdate"
        chmod 777 "$BIN_DIR/opstsetup"
        chmod 777 "$BIN_DIR/opstinstall-all"
        chmod 777 "$BIN_DIR/opsthelp"
        ##

        echo -e "$G[+]$W  Apply complete."
        sleep 1
        echo -e "
$G$D--------------------------------------------------------------------------------------$W

$B[+]$W  All Done.
"
        sleep 0.4
        echo -e "$G$D--------------------------------------------------------------------------------------$W
"
        echo -ne "$C[?]$W  Do you want to reload your terminal (just in case) ? [Y/n] "
        read y_n
        if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ] || [ ! "$y_n" ]; then
            echo -e "
$G$D--------------------------------------------------------------------------------------$W

$G$D---------------------$W
$G[-]$W  Reloading...
$G$D---------------------$W"
            sleep 0.5
            reset
            echo -e "
$G$D-----------------------------------------------------------------------------------------------------------------------------------$W

$B[OK]$W  "$G"Python3"$W","$G"PIP3"$W" and all '"$G"opst"$W"' commands are now "$G"install"$W" on you machine. Now run the OPSTSetup with '"$G"sudo opstsetup install"$W"'.

$G$D-----------------------------------------------------------------------------------------------------------------------------------$W
"
            exit 0
        else
            echo -e "
$G$D--------------------$W
$B$D[+]$W  Answer: "$R"No$W.
$G$D--------------------$W

$G$D-----------------------------------------------------------------------------------------------------------------------------------$W

$B[OK]$W  "$G"Python3"$W","$G"PIP3"$W" and all '"$G"opst"$W"' commands are now "$G"install"$W" on you machine. Now run the OPSTSetup with '"$G"sudo opstsetup install"$W"'.

$G$D-----------------------------------------------------------------------------------------------------------------------------------$W
"
            exit 0
        fi
    else
        echo -e "$GR$D[-]$W  Abort."
        exit 1
    fi
else
    echo -e "$R[!]$W  Internet status.......... "$R"Not connected"$W".
$R[*]$W   Not Internet connexion found, please check you are connected to Internet and retry."
    exit 1
fi
