#!/bin/sh

echo if you are not on a debian based distro change the install in install.sh

sudo apt install python3-rich

mkdir -p ~/.semicolon-python/

sudo cp /bin/python3 /bin/python3-nos

cp terminal.py ~/.semicolon-python/

cp rm-semicolon.py ~/.semicolon-python/
#mv rm-semicolon.py rm-semicolon.py.backup

chmod a+x python4
