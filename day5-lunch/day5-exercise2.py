#!/usr/bin/env python3

"""
Usage: ./day5-exercise2.py <ctab_file input> <.bed file output>
"""

import sys

inFile = open(sys.argv[1])
outFile = open(sys.argv[2], 'w')

#outFile.write("chromosome" + "\t" + "start" + "\t" + "end" + "\t" + "t_name" + "\n")

for i, line in enumerate(inFile):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    chr_name = fields[1]
    gene_start = int(fields[3])
    gene_end = int(fields[4])
    t_name = fields[5]
    if fields[2] == "+":
        if gene_start in range(500):
            p_start = gene_start
            p_end = gene_start + 500
        else:
            p_start = gene_start - 500
            p_end = gene_start + 500
    elif fields[2] == "-":
        if gene_end in range(500):
            p_start = gene_end + 500
            p_end = gene_end
        else:
            p_start = gene_end + 500
            p_end = gene_end -500
    outFile.write(chr_name + "\t" + str(p_start) + "\t" + str(p_end) + "\t" + t_name + "\n")