#!/bin/bash

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstupdate.sh                 [Update: 2022-04-14 | 10:26 AM] #
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

opstupdate_version="v2.9"
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
                echo "$R[!]$W    OPSTUpdate could be run as the 'root' user or with 'sudo'"
                echo "       Re-run the 'opstupdate.sh' with sudo or with the root user"
                echo '       Run sudo "sudo opstupdate"'
                exit 1
        else # Switch to sudo (root)
            echo
            echo -e "$R[!]$W    OPSTUpdate could be run as the 'root' user or with 'sudo'"
            echo -e "$G[-]$W    Switching to root user to run the 'opstupdate'"
            sudo -E bash $0 $@
            exit 0
        fi
    fi
####

# The main script
# Font = Chunky from https://www.coolgenerator.com/ascii-text-generator

echo -e "
$GR$D _______ ______ _______ _______ _______           __         __  $W
$GR$D|       |   __ \     __|_     _|   |   |.-----.--|  |.---.-.|  |_.-----.$W$G  OPSTUpdate $D$opstupdate_version
$GR$D|   -   |    __/__     | |   | |   |   ||  _  |  _  ||  _  ||   _|  -__|$W$D  A massive penetration testing toolkit
$GR$D|_______|___|  |_______| |___| |_______||   __|_____||___._||____|_____|$C$D  https://github.com/MyMeepSQL/OmegaPSToolkit$W
$GR$D +- !* Welcome to the OPSTUpdate. *! -+ |__|$W

$G[-]$W    Checking for internet connexion...
"

#First check of setup for internet connection by connecting to google over http
wget -q --tries=10 --timeout=5 --spider http://google.com
if [ $? -eq 0 ]; then
    echo -en '+ -- --=[  Internet status.......... '"$G"'Connected'"$W"'.                                                                          ]
+ -- --=[  '$underscore'This tool will:'$W'                                                                                               ]
        [  ...'$G'Install'$W' the latest verion of '$R'OPSTConsole'$W', '$R'OPSTHelp'$W', '$R'OPSTUpdate'$W', '$R'OPSTInstall-all'$W' and '$R'OPSTSetup'$W' from '$G'Github'$W'  ]

'$C'[?]'$W'    Do you want to continue? [Y/n] '
    read y_n
    if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ]; then
        echo -e "
$G$D--------------------------------------------------------------------------------------$W

$G[-]$W    Removing the current OPST's commands from '"$G"/usr/share/OmegaPSToolkit"$W"'..."
        rm -fr "$INSTALL_DIR/opstconsole.py"
        rm -fr "$INSTALL_DIR/opsthelp.py"
        rm -fr "$INSTALL_DIR/opstsetup.py"
        rm -fr "$INSTALL_DIR/opstupdate.sh"
        rm -fr "$INSTALL_DIR/opstinstall-all.sh"

        rm -fr "$INSTALL_DIR/opstfunctions.py"
        rm -fr "$INSTALL_DIR/opstcolors.py"
        rm -fr "$INSTALL_DIR/opstversions.py"

        echo -e "$G[+]$W    Done for the OPST's commands remove.
"
        sleep 1
        echo "$G$D--------------------------------------------------------------------------------------$W

$G[-]$W    "$G"Updating"$W" all commands from "$G"GitHub"$W"..."
        sleep 0.5

        if [ -e $TEMP_DIR ];then
            echo "$G[*]$W    A OmegaPSToolkit folder already exist in "$G"/tmp/"$W", append the new files..."

            rm -fr /tmp/OmegaPSToolkit

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
        else
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
        fi

        echo -e "$G[+]$W    Update complete.
"
        sleep 1
        echo -e "$G$D--------------------------------------------------------------------------------------$W2
"

        # Apply all rights
        echo -e "$G[-]$W    Apply all rights to files..."
        sleep 0.5

        # for '/usr/share/OmegaPSToolkit'
        chmod 777 "$INSTALL_DIR/opstconsole.py"
        chmod 777 "$INSTALL_DIR/opstupdate.sh"
        chmod 777 "$INSTALL_DIR/opstsetup.py"
        chmod 777 "$INSTALL_DIR/opstinstall-all.sh"
        chmod 777 "$INSTALL_DIR/opsthelp.py"

        chmod 777 "$INSTALL_DIR/opstfunctions.py"
        chmod 777 "$INSTALL_DIR/opstcolors.py"
        chmod 777 "$INSTALL_DIR/opstversions.py"
        ##

        # for '/usr/bin'
        chmod 777 "$BIN_DIR/opstconsole"
        chmod 777 "$BIN_DIR/opstupdate"
        chmod 777 "$BIN_DIR/opstsetup"
        chmod 777 "$BIN_DIR/opstinstall-all"
        chmod 777 "$BIN_DIR/opsthelp"
        ##

        echo -e "$G[+]$W    Apply complete."
        sleep 1
        echo -e "
$G$D--------------------------------------------------------------------------------------$W

$B[+]$W    All Done.
"
        sleep 1
        echo -ne "$G$D--------------------------------------------------------------------------------------$W

$C[?]$W    Do you want to reload your terminal (just in case) ? [Y/n] "
        read y_n
        if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ]; then
            echo -e "
$G$D--------------------------------------------------------------------------------------$W

$G$D---------------------$W
$G[-]$W    Reloading...
$G$D---------------------$W"
            sleep 0.5
            reset
            echo -e "
$G$D-------------------------------------------------------------------------------------------------------------------------------------$W

$B[OK]$W    "$R"OPSTConsole"$W", "$R"OPSTHelp"$W", "$R"OPSTUpdate"$W", "$R"OPSTInstall-all"$W" and "$R"OPSTSetup"$W" are now install with the latest version exist from GitHub.

$G$D-------------------------------------------------------------------------------------------------------------------------------------$W
"
            exit 0
        else
            echo -e "
$G$D--------------------$W
$B$D[+]$W    Answer: "$R"No"$W".
$G$D--------------------$W

$G$D-------------------------------------------------------------------------------------------------------------------------------------$W

$B[OK]$W    "$R"OPSTConsole"$W", "$R"OPSTHelp"$W", "$R"OPSTUpdate"$W", "$R"OPSTInstall-all"$W" and "$R"OPSTSetup"$W" are now install with the latest version exist from GitHub.

$G$D-------------------------------------------------------------------------------------------------------------------------------------$W
"
            exit 0
        fi
    else
        echo -e "$GR$D[-]$W    Abort."
        exit 1
    fi
else
    echo -e "$R[!]$W   Internet status.......... "$R"Not connected"$W".
$R[*]$W   Not Internet connexion found, please check you are connected to Internet and retry."
    exit 1
fi
