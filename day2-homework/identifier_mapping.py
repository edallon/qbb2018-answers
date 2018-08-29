#!/usr/bin/env python3

#This program adds the UniProt ID as the final column of a c_tab file.
#In order to run, 4 arguments are required:
    #a mapper file containing FlyBase ID in the first column and UniProt ID in the second column
    #a c_tab file from stringtie output
    #an output file name
    #"ignore" or "print"
#The final argument (ignore or print) determines whether genes with no UniProt ID are ignored or printed.
#If ignored, these lines are omitted from the output file. 
#If printed, the UniProt ID is listed as "none".

import sys
#As input, we need a mapping file, a c_tab file, an output file name, and an option for what to do if the gene is not found.
  
mapperFile = open(sys.argv[1])
tabFile = open(sys.argv[2])
outFile = open(sys.argv[3], 'w')
#Can be ignore or print.
#Ignore will omit any lines with no UniProt value.
#Print will print lines with UniProt value as "none".
no_ident_var = sys.argv[4]

mapper_dict = {}

#From the input file, we need to make a dictionary with the FlyBase gene as the key and the UniProt as the value.
for line in mapperFile:
    fields = line.rstrip("\r\n").split("\t")
    mapper_dict[fields[0]] = fields[1]

#With that dictionary,for each line in the c_tab file, we need to find the corresponding translation.
count = 0
for i, line in enumerate(tabFile):
    if i == 0:
        line = line.strip()
        outFile.write(line + "\t" + "identifier" + "\n")
        count += 1
    else:
        line = line.strip()
        fields = line.rstrip("\r\n").split("\t")
        #If the translation is found, print the line with the identifier.
        if fields[8] in mapper_dict:
            identifier = mapper_dict[fields[8]]
            outFile.write(line + "\t" + identifier + "\n")
            count += 1
        #If the translation is not found:
        #ignore the line
        elif no_ident_var == "ignore":
            continue
        #or print the line with a default value (none) instead
        elif no_ident_var == "print":
            outFile.write(line + "\t" + "none" + "\n")
            count += 1
    if count > 100:
        break

outFile.close()