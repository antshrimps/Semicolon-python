#!/bin/python3

from sys import argv
from pathlib import Path

filename = argv[1]

with open(filename, 'r') as f:
    nfile = ""
    for sym in f.read():
        if sym != ';':
            nfile += sym

outputfile = Path(f"{filename}.shadow.py")
outputfile.parent.mkdir(exist_ok=True, parents=True)

with open(outputfile, 'w') as f:
    f.write(nfile)
