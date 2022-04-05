#!/usr/bin/python3.8.10

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ version.py                     [Update: 2022-04-05 | 1:30 PM] #
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

# Versions
opstconsole_version = "0.0.1.3"
opstconsole_cli_version = "0.0.0.9"
opstupdate_help = "v1.4"

opstsetup_version = "v2.6"
opstupdate_version = "v2.2"
opstinstallall_version = "v1.8"

# current python version
from platform import *
import os

OS = platform()
python_version = python_version()
####