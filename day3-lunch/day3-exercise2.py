#!/usr/bin/env python3

import sys

#Find types of genes from Ensembl file
#Ensembl file has 8 columns (starting with 0)
#The last column has multiple fields, including gene_biotype which is immediately followed by a designation.
#We're counting how many of each designation there are in the file.

inFile = open(sys.argv[1])

type_count = {}

for line in inFile:
    if line.startswith("#!"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[2] == "gene":
        fields2 = fields[8].split()
        if "gene_biotype"  in fields2:
            biotype_index = fields2.index("gene_biotype")
            type_index = biotype_index + 1
            if fields2[type_index] in type_count:
                type_count[fields2[type_index]] += 1
            else:
                type_count[fields2[type_index]] = 1


for name, value in type_count.items():
    print (name, value)
