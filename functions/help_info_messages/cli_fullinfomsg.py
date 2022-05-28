#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ cli_fullinfomsg.py          [Created: 2022-05-25 | 18:08 PM]  #
#                                         [Update: 2022-05-25 | 18:20 PM]   #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The biggest version of CLI info                                          #
#                                                                           #
#  Language  ~  Python3                                                     #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright © 2022 MyMeepSQL - © PSociety™, 2022 All rights reserved       #
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

"""
=====================
Colors informations :
=====================
{R} = Option
{O} = Option's argument 
{G} = Option and argument (not with option, for exemple 'nmap 1.1.1.1', the '1.1.1.1' is a argument with no option)
{B} = Command (for exemple 'clear' or 'leave')
{P} = The eaqual caractere (=)
"""

import sys
sys.path.insert(0, '/usr/share/OmegaPSToolkit/functions')
from system_colors import system_colors as sc
from versions.opst_commands_version import *
from versions.python_version import *
from get_private_ip import *
from get_public_ip import *
from get_mac_adress import *
from os_details import *
from distribution_name import *

def cli_fullinfomsg():
    print(f"""
{sc.GR}{sc.D} ______  ______ _______ _______ {sc.W}{sc.G}  OmegaPSToolkit {sc.D}v{opsthelp_version} (opsthelp's version)
{sc.GR}{sc.D}|       |   __ \     __|_     _|{sc.G}{sc.D}  Coded by MyMeepSQL for © PSociety™
{sc.GR}{sc.D}|   -   |    __/__     | |   |  {sc.W}{sc.D}  A massive penetration testing toolkit
{sc.GR}{sc.D}|_______|___|  |_______| |___|  {sc.C}{sc.D}  https://github.com/MyMeepSQL/OmegaPSToolkit{sc.W}

{sc.G}[>]{sc.W} All informations about OmegaPSToolkit and other{sc.W}
{sc.G}[*]{sc.W} This is the biggest version, for less informations, run {sc.B}info{sc.W}

{sc.C}Informations about OmegaPSToolkit{sc.GR}:{sc.W}

    {sc.G}Main commands{sc.GR}:{sc.W}
        odstconsole                Start the current tool
        odstupdate                 Update OPST with the latest version from GitHub
        odsthelp                   Print this message and exit

    {sc.G}Other commands (to install OPST the first time){sc.GR}:{sc.W}
        odstsetup                  Install all pip packages that OPST needs
        odstinstall-all            Update you system, copy OPST to {sc.G}"{sc.C}/usr/share/OmegaPSToolkit{sc.G}"{sc.W} and write all comamnds in {sc.G}"{sc.C}/usr/bin/{sc.G}"{sc.W}

    {sc.G}All OPST commands versions{sc.GR}:{sc.W}
        opstconsole                v{opstconsole_version}
        odstconsole CLI            v{opstconsole_cli_version}
        opstupdate                 {opstupdate_version}
        opsthelp                   v{opsthelp_version}
        odstsetup                  {opstsetup_version}
        odstinstall-all            {opstinstallall_version}

    {sc.G}Other informations{sc.GR}:{sc.W}
        GitHub page                {sc.underscore}{sc.C}https://github.com/MyMeepSQL/OmegaPSToolkit{sc.W}
        Changelogs                 {sc.underscore}{sc.C}https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md{sc.W}

{sc.C}Informations about author{sc.GR}:{sc.W}

    {sc.G}General informations{sc.GR}:{sc.W}
        Author                     {sc.italic}Thomas Pellissier{sc.W}
        Codename                   {sc.G}@{sc.W}MyMeepSQL{sc.W} or {sc.G}@{sc.W}th300905{sc.W}
        Email                      {sc.P}thomas.pellissier@outlook.com{sc.W} ({sc.R}only for professional{sc.W} or for {sc.G}repport bugs of OmegaPSToolkit{sc.W})
        Owner                      {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}.

    {sc.G}Other informations{sc.GR}:{sc.W}
        GitHub profile             {sc.underscore}{sc.C}https://github.com/MyMeepSQL{sc.W}
        Twitter profile            {sc.C}@{sc.W}MyMeepSQL

{sc.C}Ohter informations{sc.GR}:{sc.W}

    {sc.G}Other versions{sc.GR}:{sc.W}
        Python's version           v{python_version}

    {sc.G}Network{sc.GR}:{sc.W}
        Private IP                 {sc.O}{privateIP}{sc.W}        Public IP                  {sc.O}{publicIP}{sc.W}
        MAC adress                 {sc.O}{mac_adress}{sc.W}

        {sc.G}Details {sc.W}({sc.C}with all inrefaces{sc.W}){sc.GR}:{sc.W} """)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"            Interface: {sc.C}{interface_name}{sc.W}")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"""                  IP Address:      {sc.O}{address.address}{sc.W}
                  Netmask:         {sc.O}{address.netmask}{sc.W}
                  Broadcast IP:    {sc.O}{address.broadcast}{sc.W}""")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"""                  MAC Address:     {sc.O}{address.address}{sc.W}
                  Netmask:         {sc.O}{address.netmask}{sc.W}
                  Broadcast MAC:   {sc.O}{address.broadcast}{sc.W}""")
    print(f"""
    {sc.G}System{sc.GR}:{sc.W}
        Operating System           {OS}
        Distribution / Release     {distribution_name}
        PC's Name                  {my_system.node}
        Machine                    {my_system.machine}
        Processor                  {my_system.processor}""")

    print("GPU details:""")
    import GPUtil
    gpus = GPUtil.getGPUs()
    for gpu in gpus:

        # get the GPU id
        GPU_details_id = gpu.id
        # name of GPU
        GPU_details_gpuName = gpu.name
        # get % percentage of GPU usage of that GPU
        GPU_details_load = f"{gpu.load*100}%"
        # get free memory in MB format
        GPU_details_freeMemory = f"{gpu.memoryFree}MB"
        # get used memory
        GPU_details_usedMemory = f"{gpu.memoryUsed}MB"
        # get total memory
        GPU_details_totalMemoy = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        GPU_details_temperature = f"{gpu.temperature} °C"
        GPU_details_uuid = gpu.uuid

        print(rf"""
Card {GPU_details_id}:                                                                             /│\
    Name               {GPU_details_gpuName}                                        / │ \
    Total memory       {GPU_details_totalMemoy}                                                   /  │  \
    Free memory        {GPU_details_freeMemory}                                                      │
    Used memory        {GPU_details_usedMemory}                                                        │
    UUID               {GPU_details_uuid}                      │    Scroll up for the main informations
            """)