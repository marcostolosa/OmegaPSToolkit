#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ critical_msg.py             [Created: 2022-05-25 | 11:31 AM]  #
#                                         [Update: 2022-05-25 | 18:45 PM]   #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The critical message function                                            #
#                                                                           #
#  Language  ~  Python3                                                     #
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

import sys
sys.path.insert(0, '/usr/share/OmegaPSToolkit/functions')
from system_colors import system_colors as sc

def critical_msg():
    print()
    critical_msg = f"{sc.R}[CRITICAL]{sc.W}  A current(s) module(s) was not installed, run the {sc.B}opstsetup{sc.W} for install it. ({sc.B}sudo opstsetup install{sc.W})\n"
    exit(critical_msg)