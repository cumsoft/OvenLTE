
#!/bin/bash
#################################################################
#################################################################
#                                                               #
#     `-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"          #
#        `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/            #
#          y==/        y==/        y==/        y==/             #
#        ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.           #
#     ,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_          #
#                                                               #
#    ▄▄█▀▀▀▄█                                      ▄▀█▄   ▄     #
#  ▄█▀     ▀  ▄▄▄ ▄▄▄  ▄▄ ▄▄ ▄▄    ▄▄▄▄    ▄▄▄   ▄██▄   ▄██▄    #
#  ██          ██  ██   ██ ██ ██  ██▄ ▀  ▄█  ▀█▄  ██     ██     #
#  ▀█▄      ▄  ██  ██   ██ ██ ██  ▄ ▀█▄▄ ██   ██  ██     ██     #
#   ▀▀█▄▄▄▄▀   ▀█▄▄▀█▄ ▄██ ██ ██▄ █▀▄▄█▀  ▀█▄▄█▀ ▄██▄    ▀█▄▀   #
#                                                               #
#      `-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"         #
#         `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/           #
#           y==/        y==/        y==/        y==/            #
#         ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.          #
#      ,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_         #
#################################################################
#   Copyright © 2022-Present by Cumsoft. All rights reserved.   #
#        This page was last updated on 20 December 2022.        #
#                                                               #
#           https://cumsoft.wixsite.com/cumsoft                 #
#               https://github.com/cumsoft                      #
#              https://cumsoft.gumroad.com                      #
#################################################################
#################################################################

# Please dont forget to 

# Check if Python 3 is installed
if command -v python3 &>/dev/null; then
    echo "Python 3 is already installed."
else
    # Check if apt is available
    if command -v apt &>/dev/null; then
        # Install Python 3 using apt
        sudo apt update
        sudo apt install python3 -y
    # Check if yum is available
    elif command -v yum &>/dev/null; then
        # Install Python 3 using yum
        sudo yum update
        sudo yum install python3 -y
    else
        echo "Error: Could not find package manager (apt or yum) to install Python 3."
        exit 1
    fi
fi

# Check if pip is installed
if command -v pip3 &>/dev/null; then
    echo "pip is already installed."
else
    # Check if apt is available
    if command -v apt &>/dev/null; then
        # Install pip using apt
        sudo apt update
        sudo apt install python3-pip -y
    # Check if yum is available
    elif command -v yum &>/dev/null; then
        # Install pip using yum
        sudo yum update
        sudo yum install python3-pip -y
    else
        echo "Error: Could not find package manager (apt or yum) to install pip."
        exit 1
    fi
fi

# Use pip to install the vcgencmd package
pip3 install vcgencmd
