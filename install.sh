#!/bin/sh

sudo apt install python3-rich

mkdir -p ~/.semicolon-python/

cp terminal.py ~/.semicolon-python/

cp rm-semicolon.py ~/.semicolon-python/
#mv rm-semicolon.py rm-semicolon.py.backup

chmod a+x python4
