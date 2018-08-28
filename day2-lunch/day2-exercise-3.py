#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    inFile = open(sys.argv[1])
else :
    #This stdin allows the python script to be piped to and from in the commandline
    inFile = sys.stdin
  
oneloc_count = 0 
for i, line in enumerate( inFile ) :
    if line.startswith("@"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    #if fields[1] != "4":
    if "NH:i:1" in fields :
        oneloc_count += 1
   
print (oneloc_count)