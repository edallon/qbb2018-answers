#!/usr/bin/env python3

"""
Usage: ./diff_exp_genes.py expression_file
This code identifies differentially expressed genes from 4 cell populations based on a t test.
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

ratios = []
genes = {}

for line in open(sys.argv[1]):
    early = []
    late = []
    fields = line.rstrip('\r\n').split('\t')
    if fields[0] == 'gene':
        continue
    cfu = fields[1]
    mys = fields[5]
    unk = fields[3]
    poly = fields[2]
    ratio = (float(cfu)+float(mys))/(float(unk)+float(poly))
    early.append(float(cfu))
    early.append(float(mys))
    late.append(float(unk))
    late.append(float(poly))
    t, p = stats.ttest_ind(early, late)
    if p <= .05:
        if ratio >= 2:
            ratios.append(ratio)
            genes[ratio] = fields[0]
            # print (fields[0], ratio)
        elif ratio <= .5:
            ratios.append(ratio)
            genes[ratio] = fields[0]
            # print (fields[0], ratio)
ratios.sort()
for num in ratios:
    print (genes[num], num)