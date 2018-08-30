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
log_fpkm1 = np.log(fpkm1 + 1)

name2 = sys.argv[2].split(os.sep)[-2]
fpkm2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name").loc[:, "FPKM"]
log_fpkm2 = np.log(fpkm2 + 1)

fit1 = np.polyfit(log_fpkm1, log_fpkm2, 1)
fit2 = np.poly1d(fit1)

x_new = np.linspace (min(log_fpkm1), max(log_fpkm1), 100)
y_new = fit2(x_new)

fig, ax = plt.subplots()
ax.set_title("FPKM  log scatter plot")
ax.set_xlabel(name1)
ax.set_ylabel(name2)
ax.scatter(log_fpkm1, log_fpkm2, alpha=0.5)
ax.plot(x_new, y_new, 'k-')
fig.savefig("scatter9.png")
plt.close(fig)

# fig, ax = plt.subplots()
# ax.set_title("FPKM scatter plot")
# ax.set_xlabel(name1)
# ax.set_ylabel(name2)
# ax.scatter(fpkm1, fpkm2)
# fig.savefig("scatter2.png")
# plt.close(fig)

# fig, ax = plt.subplots()
# ax.set_title("FPKM  log scatter plot")
# ax.set_xlabel(name1)
# ax.set_ylabel(name2)
# ax.scatter(log_fpkm1, log_fpkm2)
# fig.savefig("scatter3.png")
# plt.close(fig)

# fig, ax = plt.subplots()
# ax.set_title("FPKM  log scatter plot")
# ax.set_xlabel(name1)
# ax.set_ylabel(name2)
# ax.scatter(log_fpkm1, log_fpkm2, alpha = 0.5)
# fig.savefig("scatter4.png")
# plt.close(fig)