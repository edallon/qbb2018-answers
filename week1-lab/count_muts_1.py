#!/usr/bin/env python3

"""
Usage: ./count_muts_1.py <nuc-file> <pep-file>
This program calculates the number of synonymous (dS) and nonsynonymous (dN) mutations at each codon 
position of a query using the fasta formatted blastn results and an accompanying multiple sequence 
alignment. The plot generated shows the difference between dN and dS at each position, with a line 
indicating the significance cutoff.
"""

import sys
import fasta
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nucs = fasta.FASTAReader(open(sys.argv[1]))
peps = fasta.FASTAReader(open(sys.argv[2]))

align_seqs=[]

for (nuc_id, nuc_seq), (pep_id, pep_seq) in zip(nucs, peps):
    count = 0
    nseq = []
    for i in range(len(pep_seq)):
        a = pep_seq[i]
        if a == "-":
            nseq.append("---")
        else:
            nseq.append(nuc_seq[count*3:(count*3)+3])
            count += 1

    align_seqs.append(nseq)

dS_all = []
dN_all = []

aligns = list(range(1, len(align_seqs)))
query = list(range(len(align_seqs[0])))

codon = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

for j in query:
    dS = 0
    dN = 0
    for i in aligns:
        if align_seqs[0][j] not in codon:
            pass
        elif align_seqs[i][j] not in codon:
            pass
        elif align_seqs[i][j] == align_seqs[0][j]:
            pass
        elif codon[align_seqs[i][j]] == codon[align_seqs[0][j]]:
            dS += 1
        else:
            dN += 1
    dS_all.append(dS)
    dN_all.append(dN)

diff_all = []

i = 0
for num in dS_all:
    diff = float(dN_all[i])-float(num)
    diff_all.append(diff)
    i += 1
    
stand_dev = np.std(diff_all)
stand_err = stand_dev/np.sqrt(len(diff_all))

z_list = []
for var in diff_all:
    z = (float(var))/float(stand_err)
    z_list.append(z)

x = 0
fig, ax = plt.subplots()
ax.set_title("Nonsynonymous vs Synonymous Mutations")
ax.set_xlabel("codon position")
ax.set_ylabel("dN-dS")
ax.scatter(range(len(diff_all)), z_list, s=2, c='k', alpha=0.5)
ax.axhline(y=4, color='r', linestyle='--')
fig.savefig("diff_plot1.png")
plt.close(fig)