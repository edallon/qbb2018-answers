#!/usr/bin/env python3

"""
Usage: ./overlap_plot.py annotated.file(Mus_mus..._features.bed) unique.bed1 unique.bed2 
This code generates a two panel plot where the first panel is the number of sites in different types of regions
between cell types 1 and 2, and the second panel is the number of sites gained/lost between cell types.
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_positions(file_name):
    position = []
    for line in open(file_name):
        fields = line.rstrip('\r\n').split()
        start = int(fields[1])
        shift = int(fields[9])
        pos = start + shift
        position.append(pos)
    return position

def get_features(pos_list, feature_dict):
    introns = 0
    exons = 0
    promoters = 0
    for val in pos_list:
        if val in feature_dict['intron']:
            introns += 1
        elif val in feature_dict['exon']:
            exons += 1
        elif val in feature_dict['promoter']:
            promoters += 1
    return [introns, exons, promoters]        

features = {}

for line in open(sys.argv[1]):
    fields = line.rstrip('\r\n').split()
    feature = fields[3]
    start = int(fields[1])
    stop = int(fields[2]) 
    range_list = list(range(start, stop))
    if feature in features:
        for val in range_list:
            features[feature].append(val)
    else:
        features[feature] = []
        for val in range_list:
            features[feature].append(val)
        
prediff_pos = get_positions(sys.argv[2])
prediff_features = get_features(prediff_pos, features)

postdiff_pos = get_positions(sys.argv[3])
postdiff_features = get_features(postdiff_pos, features)

gained = sum(postdiff_features)
lost = sum(prediff_features)

fig, ax = plt.subplots(figsize=(20, 5))

ax = plt.subplot(1, 2, 1)
plt.bar([1, 2], [lost, gained], align='center')
ax.set_title("G1E vs ER4")
ax.set_xticklabels(['null', 'sites lost', 'sites gained'])


ax = plt.subplot(1, 2, 2)
plt.bar([1, 2, 3, 4, 5, 6], [prediff_features[0], prediff_features[1], prediff_features[2], postdiff_features[0], postdiff_features[1], postdiff_features[2]], align='center')
ax.set_title("Cell type categories")
ax.set_xticklabels(['null', 'G1E introns', 'G1E exons', 'G1E promoters', 'ER4 introns', 'ER4 exons', 'ER4 promoters'])


plt.tight_layout()
fig.savefig("differentiation.png")
plt.close(fig)
