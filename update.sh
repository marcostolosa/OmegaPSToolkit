#---[Metadata]-------------------------------------------------------#
#  Filename ~ update.sh                        [Update: 01-03-2022]  #
#---[Info]-----------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}  #
#                                                                    #
#  The update tool for have the latest version of ODST               #
#  Language  ~  Bash                                                 #
#---[Author]---------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                    #
#  Copyright (C) 2022 MyMeepSQL - © Delta_Society™                   #
#---[Operating System]-----------------------------------------------#
#  Developed for linux                                               #
#--------------------------------------------------------------------#

#!/bin/bash

rm -f OmegaDSToolkit

git pul

REPO='/usr/share/OmegaDSToolkit/'

if [ -d "$REPO.git/" ]
then
        echo "Updating repo test"
        cd "$REPO"
        echo "Pulling"
        git pull
else
        echo "cannot find .git file"
fi