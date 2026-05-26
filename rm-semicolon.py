#!/bin/python3

from sys import argv
from pathlib import Path
import os

filename = argv[1]
home = os.path.expanduser('~')

#print(filename)
if '/' in filename:
    filename = filename.replace("~", home)^

with open(filename, 'r') as f:
    nfile = ""
    for sym in f.read():
        if sym != ';':
            nfile += sym

outputfile = f"{filename}.shadow.py"

#open(outputfile, 'x')

with open(outputfile, 'w') as f:
    f.write(nfile)

#print(f"{outputfile} created")
