#!/bin/python3

from sys import argv
from pathlib import Path

#try:
#    filename = argv[1]
#except:
 #   outputfile = Path(f"/home/maxi/stuff/{filename}.shadow.py")
  #  output_file.parent.mkdir(exist_ok=True, parents=True)
#
 #   with open outputfile as f:
  #      f.write("#!EMPTY)

filename = argv[1]

##print("Removing semicolons from" + filename)

with open(filename, 'r') as f:
    nfile = ""
    for sym in f.read():
        if sym != ';':
            nfile += sym

outputfile = Path(f"/home/maxi/stuff/{filename}.shadow.py")
outputfile.parent.mkdir(exist_ok=True, parents=True)

with open(outputfile, 'w') as f:
    f.write(nfile)
