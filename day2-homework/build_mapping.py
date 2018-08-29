#!/usr/bin/env python3

#This program takes fly.txt and converts it to a text file with the FlyBase ID in the first column and UniProt ID in the second.
#In order to run, two arguments are required: fly.txt and an output file name.

import sys
    
inFile = open(sys.argv[1])
outFile = open(sys.argv[2], 'w')

for line in inFile:
    if "DROME" in line:
        fields = line.rstrip("\r\n").split()
        if len(fields) == 4:
            outFile.write(fields[3] + "\t" + fields[2] + "\n")

outFile.close()
