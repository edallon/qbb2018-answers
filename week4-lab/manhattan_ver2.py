#!/usr/bin/env python3

"""
Usage: ./manhattan.py .qassoc file (from plink)
In theory, this code should plot manhattan plots for a variable number of files.
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

for var in sys.argv[1:]:
    names = var.split('.')
    chromosomes = {}

    for i, line in enumerate(open(var)):
        if i == 0:
            continue
        else:
            fields = line.rstrip('\r\n').split()
            if "NA" in fields:
                continue

            chrom = fields[0]
            pos = int(fields[2])
            pval = float(fields[8])
            plog = -np.log10(pval)

            if fields[0] in chromosomes:
                chromosomes[chrom]['positions'].append(pos)
                chromosomes[chrom]['logpvals'].append(plog)
            else:
                chromosomes[chrom] = {'positions':[], 'logpvals':[]}

    fig, ax = plt.subplots(figsize=(20,5))

    colors = ['steelblue', 'gray']
    highlights = ['lightskyblue', 'silver']

    offset = 0
    tick_pos = []
    tick_labels = []
    for i, chrom in enumerate(chromosomes.keys()):
        x = chromosomes[chrom]['positions']
        y = chromosomes[chrom]['logpvals']
        x_ns = []
        y_ns = []
        x_sig = []
        y_sig = []
        for i, val in enumerate(y):
            if val > 5:
                y_sig.append(val)
                x_sig.append(x[i]+offset)
            else:
                y_ns.append(val)
                x_ns.append(x[i] + offset)

        ax.scatter(x_ns, y_ns, marker='.', color=colors[i%2])
        ax.scatter(x_sig, y_sig, marker='.', color=highlights[i%2])

        tick_labels.append(chrom)
        maxx = max(x)
        tick_pos.append(offset + maxx/2)
        offset += maxx
    

    ax.set_xticks(tick_pos)
    ax.set_xticklabels(tick_labels);

    ax.axhline(5, c='k', ls=':', label="Significance Cutoff")
    ax.legend()
    ax.set_xlabel('Genomic Position')
    ax.set_ylabel('Log10 P-value')
    ax.set_title('Manhattan Plot\n' + names[1]);

    fig.savefig(names[1] + '.png')
    plt.close(fig)
    