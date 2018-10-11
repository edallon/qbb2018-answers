#!/usr/bin/env python3

"""
Usage: ./pca.py eigenvec file (from plink)
In theory, this code should plot the principal component analysis.
"""

import sys
import matplotlib.pyplot as plt

x = []
y = []
for line in open(sys.argv[1]):
    fields = line.rstrip('\r\n').split(' ')
    x.append(float(fields[2]))
    y.append(float(fields[3]))
    
fig, ax = plt.subplots()

plt.scatter(x, y, s=5, color="blue")
# plt.xlim(0, 250)
# plt.ylim(0, 6000)
ax.set_title("PCA")

fig.savefig("pca.png")
plt.close(fig)   