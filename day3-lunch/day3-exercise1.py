#!/usr/bin/env python3

import sys

#Find protein coding genes from Ensembl file
#Ensembl file has 8 columns (starting with 0)
#The last column has multiple fields, including gene_biotype which is immediately followed by a designation.
#In this case, we're looking for protein_coding.

inFile = open(sys.argv[1])

count = 0

for line in inFile:
    if line.startswith("#!"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[2] == "gene":
        fields2 = fields[8].split()
        if "gene_biotype"  in fields2:
            biotype_index = fields2.index("gene_biotype")
            type_index = biotype_index + 1
            if fields2[type_index] == '"protein_coding";':
                count += 1

print (count)



