#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opsthelp.py                    [Update: 2022-04-16 | 2:32 AM] #
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
import sys,psutil,GPUtil
from opstcolors import GR,D,W,G,C,R,P,B,O,underscore,italic,bold
from opstversions import *
from opstfunctions import privateIP,publicIP,MAC_adress
# from opstfunctions import GPU_details_id,GPU_details_id,GPU_details_gpuName,GPU_details_totalMemoy, GPU_details_freeMemory,GPU_details_usedMemory,GPU_details_uuid

####

# The main command
## Font = Chunky from https://www.coolgenerator.com/ascii-text-generator
def opsthelp():
    print(f"""
{GR}{D} ______  ______ _______ _______ {W}
{GR}{D}|       |   __ \     __|_     _|{W}{G}  OmegaPSToolkit {D}v{opsthelp_version} (opsthelp's version)
{GR}{D}|   -   |    __/__     | |   |  {W}{D}  A massive penetration testing toolkit
{GR}{D}|_______|___|  |_______| |___|  {C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}

{G}[>]{W} All informations about OmegaPSToolkit and other{W}
{G}[*]{W} This is the biggest version, for less informations, run {B}info{W}

{C}Informations about OmegaPSToolkit{GR}:{W}

    {G}Main commands{GR}:{W}
        odstconsole                Start the current tool
        odstupdate                 Update OPST with the latest version from GitHub
        odsthelp                   Print this message and exit

    {G}Other commands (to install OPST the first time){GR}:{W}
        odstsetup                  Install all pip packages that OPST needs
        odstinstall-all            Update you system, copy OPST to {G}"{C}/usr/share/OmegaPSToolkit{G}"{W} and write all comamnds in {G}"{C}/usr/bin/{G}"{W}

    {G}All OPST commands versions{GR}:{W}
        opstconsole                v{opstconsole_version}
        odstconsole CLI            v{opstconsole_cli_version}
        opstupdate                 {opstupdate_version}
        opsthelp                   v{opsthelp_version}
        odstsetup                  {opstsetup_version}
        odstinstall-all            {opstinstallall_version}

    {G}Other informations{GR}:{W}
        GitHub page                {underscore}{C}https://github.com/MyMeepSQL/OmegaPSToolkit{W}
        Changelogs                 {underscore}{C}https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md{W}

{C}Informations about author{GR}:{W}

    {G}General informations{GR}:{W}
        Author                     {italic}Thomas Pellissier{W}
        Codename                   {G}@{W}MyMeepSQL{W} or {G}@{W}th300905{W}
        Email                      {P}thomas.pellissier@outlook.com{W} ({R}only for professional{W} or for {G}repport bugs of OmegaPSToolkit{W})
        Owner                      {italic}Copyright © 2021-2022 PSociety™{W}, {R}All rights reserved{W}. {italic}By Thomas Pellissier aka MyMeepSQL{W}

    {G}Other informations{GR}:{W}
        GitHub profile             {underscore}{C}https://github.com/MyMeepSQL{W}
        Twitter profile            {C}@{W}MyMeepSQL
        Discord profile            $_MyMeepSQL{C}#{G}0141{W}

{C}Ohter informations{GR}:{W}

    {G}Other versions{GR}:{W}
        Python's version           v{python_version}

    {G}Network{GR}:{W}
        Private IP                 {O}{privateIP}{W}        Public IP                  {O}{publicIP}{W}
        MAC adress                 {O}{MAC_adress}{W}

        {G}Details {W}({C}with all inrefaces{W}){GR}:{W}""")
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"            Interface: {C}{interface_name}{W}")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"""                  IP Address:      {O}{address.address}{W}
                  Netmask:         {O}{address.netmask}{W}
                  Broadcast IP:    {O}{address.broadcast}{W}""")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"""                  MAC Address:     {O}{address.address}{W}
                  Netmask:         {O}{address.netmask}{W}
                  Broadcast MAC:   {O}{address.broadcast}{W}""")
    print(f"""
    {G}System{GR}:{W}
        Operating System           {OS}
        Distribution / Release     {distribution}
        PC's Name                  {my_system.node}
        Machine                    {my_system.machine}
        Processor                  {my_system.processor}
""")

    print(f"""        {G}RAM details{GR}:{W}
            Total memory           {RAM_total_memory}
            Free memory            {RAM_avalable_memory}
            Used memory            {RAM_used_memory}
            RAM usage              {RAM_usage}""")

    import os 
    os.system("exit")
    print(f"\n        {G}GPU details{GR}:{W}")
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
        # get the driver version
        GPU_details_driverVersion = f"{gpu.driver}"
        # get the gpu uuid
        GPU_details_uuid = gpu.uuid
        GPU_details_id = GPU_details_id + 1

        if GPU_details_temperature >= "65":
            GPU_details_temperature = f"{R}{GPU_details_temperature}{W}"
        elif GPU_details_temperature <= "60":
            GPU_details_temperature = f"{O}{GPU_details_temperature}{W}"
        elif GPU_details_temperature <= "45":
            GPU_details_temperature = f"{B}{GPU_details_temperature}{W}"

        print(rf"""            Card {C}{GPU_details_id}{W}:
                Name               {C}{GPU_details_gpuName}{W}
                Total memory       {GPU_details_totalMemoy}
                Free memory        {GPU_details_freeMemory}
                Loaded memory      {GPU_details_load}
                Used memory        {GPU_details_usedMemory}
                Temperature        {GPU_details_temperature}
                Driver version     v{GPU_details_driverVersion}
                UUID               {GPU_details_uuid}             """)
    print(f"                                                                                            {G}/[{W} Scroll {O}UP{W} for the main informations {G}]\{W}\n")

if __name__ == '__main__':
    opsthelp()
    sys.exit(0)
