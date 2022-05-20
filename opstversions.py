#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstversion.py                 [Update: 2022-04-16 | 2:32 AM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}         #
#                                                                           #
#  The file wich include all version of all 'opst' commands                 #
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


# OPST's commands versions

## Console
opstconsole_version = "0.0.1.3"

## CLI Beta
opstconsole_cli_version = "0.0.1.5"

## Help
opsthelp_version = "3.0"

## Setup
opstsetup_version = "v2.6"


## Update
opstupdate_version = "v2.9"

## Install-all
opstinstallall_version = "v2.2"
####


# Other version
import platform
python_version = platform.python_version()
####


# Other informations

## Get the OS name
my_system=platform.uname()

OS=my_system.system
Node_Name=my_system.node
Release=my_system.release
Version=my_system.version
Machine=my_system.machine
Processor=my_system.processor

## Get usage of RAM
import psutil
# Total RAM
RAM_total_memory=f"{round(psutil.virtual_memory().total/1000000000, 2)} GB"
# Available RAM
RAM_avalable_memory=f"{round(psutil.virtual_memory().available/1000000000, 2)} GB"
# Used RAM
RAM_used_memory=f"{round(psutil.virtual_memory().used/1000000000, 2)} GB"
# RAM usage
RAM_usage=f"{psutil.virtual_memory().percent}%"

## For the distribution's name
class distribName():
    import csv
    RELEASE_DATA = {}
    with open("/etc/os-release") as f:
        reader = csv.reader(f, delimiter="=")
        for row in reader:
            if row:
                RELEASE_DATA[row[0]] = row[1]

    if RELEASE_DATA["ID"] in ["debian", "raspbian"]:
        with open("/etc/debian_version") as f:
            DEBIAN_VERSION = f.readline().strip()
        major_version = DEBIAN_VERSION.split(".")[0]
        version_split = RELEASE_DATA["VERSION"].split(" ", maxsplit=1)
        if version_split[0] == major_version:
            # Just major version shown, replace it with the full version
            RELEASE_DATA["VERSION"] = " ".join([DEBIAN_VERSION] + version_split[1:])
    global distribution
    distribution = "{} {}".format(RELEASE_DATA["NAME"], RELEASE_DATA["VERSION"])