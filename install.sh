#!/bin/bash

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ install.sh                    [Update: 2022-03-08 | 11:30 AM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}         #
#                                                                           #
#  The tool for install Python3 and PIP3                                    #
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

# Colors
lime='\033[1;32m'
red='\033[1;31m'
reset='\033[0m'
####

# Many fresh installed linux distros do not come with sudo installed
which sudo > /dev/null 2>&1
if [ "$?" != "0" ]; then
    echo "You Linux distribution doesn't have the \"sudo\" command pre-install. Install the current \"sudo\" command..."
    sleep 1
    apt-get install sudo -y
fi
####

# Check if user have root privileges
if [ $(id -u) != "0" ]; then
    echo 'The InstallTool could be run with root privilege.'
    echo 'Re-run the install.sh with sudo'
    echo 'Run sudo "sudo sh install.sh"';
    exit 0
fi
####

# The main script
echo '
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗  ████████╗ ██████╗  ██████╗ ██╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║  ╚══██╔══╝██╔═══██╗██╔═══██╗██║
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     ██║   ██║   ██║██║   ██║██║
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██║   ██║   ██║██║   ██║██║
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝    ╚═════╝  ╚═════╝ ╚══════╝'
echo '+ ------------------ !* Welcome to the ODST installation tool. *! ------------------ +'
echo
echo '+ ----------------------------------- +'
echo '  Checking for internet connection...'
echo '+ ----------------------------------- +'
echo
# First check of setup for internet connection by connecting to google over http
wget -q --tries=10 --timeout=20 --spider http://google.com
if [ $? -eq 0 ] 
then
    echo 'Internet status.......... '"$lime"'Connected.'"$reset"
    echo 'This tool will install Python3 and PIP3 on this PC to run OmegaDSToolkit.'
    read -p 'Do you want to continue? [Y/n] ' y_n

    if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ]
    then
        apt update -y
        apt install python3 -y
        apt install python3-pip -y

        # Apply all rights
        echo 'Apply all rights to files...'
        chmod +xrw OmegaDSToolkit.py     # for the OmegaDSToolkitz
        chmod +xrw setup.py              # for the SetupTool
        chmod +xrw update.py             # for the UpdateTool
        echo
        echo 'Done.'
        echo
        echo 'Python3 and PIP3 are now install on you PC. Now you can run the setup.py with "sudo python3 setup.py install".'
    else
        echo 'Abort.'
    fi
else
    echo 'Internet status.......... '"$red"'Not connected.'"$reset"
    echo 'Not Internet connexion found, please check you are connected to Internet and retry.'
    exit 0
fi
####
