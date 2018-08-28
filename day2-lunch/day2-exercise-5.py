#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    inFile = open(sys.argv[1])
else :
    #This stdin allows the python script to be piped to and from in the commandline
    inFile = sys.stdin
  
mapqsum = 0 
count = 0
for i, line in enumerate( inFile ) :
    if line.startswith("@"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    mapqsum += int(fields[4])
    count += 1
    
mapq_avg = float(mapqsum/count)
   
print (mapq_avg)