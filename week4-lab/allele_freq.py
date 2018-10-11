#!/usr/bin/env python3

"""
Usage: ./allele_freq.py .frq file (from plink freq analysis)
In theory, this code should plot the allele frequencies as a histogram.
"""

import sys
import matplotlib.pyplot as plt

freqs = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    else:
        fields = line.rstrip('\r\n').split()
        freqs.append(float(fields[4]))
    
fig, ax = plt.subplots()

plt.hist(freqs, bins=50, color="blue")
# plt.xlim(0, 250)
# plt.ylim(0, 6000)
ax.set_title("Allele frequencies")

fig.savefig("AF.png")
plt.close(fig)   