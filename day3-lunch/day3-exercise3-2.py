#!/usr/bin/env python3

import sys

#Looking for nearest protein-coding and non-protein-coding genes to 3R:21,378,950
#Filter by gene in column 2, then 3R in column 0.
#If my_dist=0, you're in the gene.

inFile = open(sys.argv[1])

find_pos = 21378950
dist_dict = {}

for line in inFile:
    if line.startswith("#!"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[2] == "gene" and fields[0] == "3R":
        fields2 = fields[8].split()
        gene_start = int(fields[3])
        gene_end = int(fields[4])
        id_index = fields2.index("gene_id")
        name_index = id_index + 1
        biotype_index = fields2.index("gene_biotype")
        type_index = biotype_index + 1
        if fields2[type_index] != '"protein_coding";':
            my_dist = 0
            if find_pos < gene_start:
                my_dist = gene_start - find_pos
                dist_dict[my_dist] = fields2[name_index]
            elif find_pos > gene_end:
                my_dist = find_pos - gene_end
                dist_dict[my_dist] = fields2[name_index]
            else:
                dist_dict[my_dist] = fields2[name_index]
            

dist_list = dist_dict.keys()
dist_min = min(dist_list)
print (dist_dict[dist_min])