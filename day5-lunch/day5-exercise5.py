#!/usr/bin/env python3

"""
Usage: ./day5-exercise5.py <ctab_file> <tab1> <tab2> <tab3> <tab4> <tab5>
"""

import sys
import os
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

expr = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name").loc[:, "FPKM"]

means = {}
names = []

for tab in sys.argv[2:]:
    filename = tab + ".tab"
    ctab_df = pd.read_table(filename, index_col=0)
    mean = ctab_df.iloc[:, 4]
    names.append(tab)
    means[tab] = mean
    
means["fpkm"] = expr
    
means_df = pd.DataFrame(means)

name_string = " + ".join(names)
form = "fpkm ~ " + name_string

var1 = smf.ols(formula=form, data=means_df)
res = var1.fit()
#print (res.resid)
#Plot res.resid as a histogram

fig, ax = plt.subplots()
ax.hist(res.resid, bins=1000)
ax.set_title("Residuals")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_xlim(left=-100, right=100)
fig.savefig("resid.png")
plt.close(fig)
