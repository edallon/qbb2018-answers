#!/usr/bin/env python3

"""
Usage: ./merge_fpkms.sh <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen>

Create csv file with FPKMs from multiple samples, where the FPKM sum is greater
than the desired threshold.
- assumes ctab_file in directory with same name
"""

import sys
import os
import pandas as pd

threshold = float(sys.argv[1])

del sys.argv[0:2]

fpkms = {}
cols_to_sum = []

for arg in sys.argv:
    name = arg.split(os.sep)[-2]
    fpkm = pd.read_csv(arg, sep="\t", index_col="t_name").loc[:, "FPKM"]
    fpkms[name] = fpkm
    cols_to_sum.append(name)
    
fpkms_df = pd.DataFrame(fpkms)

sums = fpkms_df.loc[:, cols_to_sum].sum(axis=1)
df2 = fpkms_df.assign(total=sums)

roi_fpkm = df2.loc[:, "total"] > threshold

df2.loc[roi_fpkm, :].to_csv(sys.stdout, sep="\t")