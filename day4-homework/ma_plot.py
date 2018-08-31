#!/usr/bin/env python3

"""
Usage: ./day4-exercise2.py <ctab_file1> <ctab_file2>
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name1 = sys.argv[1].split(os.sep)[-2]
fpkm1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name").loc[:, "FPKM"]

name2 = sys.argv[2].split(os.sep)[-2]
fpkm2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name").loc[:, "FPKM"]

x = (1/2)*np.log2((fpkm1+1)+(fpkm2+1))
#log_x = np.log(x + 1)
y = np.log2((fpkm1+1)/(fpkm2+1))
#log_y = np.log(y + 1)


# fit1 = np.polyfit(log_fpkm1, log_fpkm2, 1)
# fit2 = np.poly1d(fit1)
#
# x_new = np.linspace (min(log_fpkm1), max(log_fpkm1), 100)
# y_new = fit2(x_new)

fig, ax = plt.subplots()
ax.set_title("MA plot")
ax.set_xlabel("average of {0} and {1}".format(name1, name2))
ax.set_ylabel("{0}/{1}".format(name1, name2))
ax.scatter(x, y, alpha=0.5)
#ax.plot(x, y, 'k-')
fig.savefig("MA-1.png")
plt.close(fig)