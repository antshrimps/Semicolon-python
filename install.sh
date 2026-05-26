#!/bin/sh

mkdir -p ~/.semicolon-python

cp -rf rm-semicolon.py ~/.semicolon-python/
mv rm-semicolon.py rm-semicolon.py.backup

chmod a+x python4
