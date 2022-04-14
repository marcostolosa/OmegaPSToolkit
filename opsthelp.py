#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opsthelp.py                   [Update: 2022-04-11 | 12:57 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The help message for OmegaPSToolkit                                      #
#  Language  ~  Python3                                                     #
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

# Import section
import sys
from opstcolors import GR,D,W,G,C
from opstversions import *
####

# The main command
# Police = Chunky from https://www.coolgenerator.com/ascii-text-generator
print(f"""
{GR}{D} ______  ______ _______ _______ {W}
{GR}{D}|       |   __ \     __|_     _|{W}{G}  OmegaPSToolkit {D}v{W}{opstconsole_version}
{GR}{D}|   -   |    __/__     | |   |  {W}{D}  A massive penetration testing toolkit
{GR}{D}|_______|___|  |_______| |___|  {C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}

{C}Informations about OmegaPSToolkit{GR}:{W}

    {G}Main commands{GR}:{W}
        odstconsole         Start the current tool
        odstupdate          Update OPST with the latest version from GitHub
        odsthelp            Print this message and exit

    {G}Other commands (to install OPST){GR}:{W}
        odstsetup           Install all pip packages that OPST needs
        odstinstall-all     Update you system, copy OPST to {G}"{C}/usr/share/OmegaPSToolkit{G}"{W} and write all comamnds in {G}"{C}/usr/bin/ss{G}"{W}

    {G}OPST Versions{GR}:{W}
        opstconsole         v{opstconsole_version}
        odstconsole CLI     v{opstconsole_cli_version}
        opstupdate          {opstupdate_version}
        opsthelp            {opstupdate_help}
        odstsetup           {opstsetup_version}
        odstinstall-all     {opstinstallall_version}

    {G}Other Versions{GR}:{W}
        python              v{python_version}

{C}Informations about author{GR}:{W}
    Author                  Thomas Pellissier
    Codename                MyMeepSQL
    Owner                   © PSociety™. 2022, All rights reserved.

{C}Ohter informations{GR}:{W}
    Operating System        {OS}
""")


sys.exit()