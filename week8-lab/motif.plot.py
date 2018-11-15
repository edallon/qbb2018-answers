#!/usr/bin/env python3

"""
Usage: ./motif.plot.py motifs_file (fimo.gff) input_sequence_file (ER4.peaks.top100)
This code generates a plot showing where motif matches occur in input sequences.
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd    

peaks = {}

for line in open(sys.argv[2]):
    fields = line.rstrip('\r\n').split('\t')
    peak_name = fields[3]
    peak_start = int(fields[1])
    peak_stop = int(fields[2]) 
    peaks[peak_name] = [peak_start, peak_stop]

motif_vals = []
  
for line in open(sys.argv[1]):
    if line[0] == '#':
        continue
    fields = line.rstrip('\r\n').split('\t')
    name = fields[0]
    motif_start = int(fields[3])
    motif_stop = int(fields[4])
    peak_start = peaks[name][0]
    peak_stop = peaks[name][1]
    val = float((motif_start-peak_start)/(peak_stop-peak_start))
    motif_vals.append(val)
    
    

fig, ax = plt.subplots()
ax.hist(motif_vals, bins=150, color="blue")
ax.set_xlabel("motif position")
ax.set_ylabel("frequency")
plt.tight_layout()
fig.savefig("motifs.png")
plt.close(fig)