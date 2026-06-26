#!/bin/sh

echo if you are not on a debian based distro change the install in install.sh

sudo apt install python3-rich

mkdir -p ~/.semicolon-python/

cp terminal.py ~/.semicolon-python/

cp rm-semicolon.py ~/.semicolon-python/
mv rm-semicolon.py rm-semicolon.backup.py

chmod a+x python4
sudo mv python4 python4.backup

echo moving python4 to /bin
sudo mv python4.backup /bin/python4
