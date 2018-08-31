#!/usr/bin/env python3

"""
Usage: ./day5-exercise6.py <ctab_file> <tab1> <tab2> <tab3> <tab4> <tab5>
"""

import sys
import os
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

expr = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name").loc[:, "FPKM"]
expr_log = np.log(expr + 1)

means = {}
names = []

for tab in sys.argv[2:]:
    filename = tab + ".tab"
    ctab_df = pd.read_table(filename, index_col=0)
    mean = ctab_df.iloc[:, 4]
    names.append(tab)
    means[tab] = mean

means["fpkm"] = expr_log

means_df = pd.DataFrame(means)

name_string = " + ".join(names)
form = "fpkm ~ " + name_string

var1 = smf.ols(formula=form, data=means_df)
res = var1.fit()
#print (res.resid)
#Plot res.resid as a histogram

fig, ax = plt.subplots()
ax.hist(res.resid, bins=100)
ax.set_title("Residuals")
ax.set_xlabel("Residual")
ax.set_ylabel("Number of transcripts")
ax.set_xlim(left=-4, right=7)
#ax.set_ylim(0, 8000)
fig.savefig("resid_log.png")
plt.close(fig)