#!/usr/bin/env python3

"""
Usage: ./01-merge_FPKMs.py <samples.csv> <ctab_dir>

Merge FPKMs from files in samples.csv (16 total)
"""

import sys
import os
import pandas as pd

df = pd.read_csv(sys.argv[1])

fpkms = {}

for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
    ctab_df = pd.read_table(filename, index_col="t_name")
    fpkm = ctab_df.loc[:, "FPKM"]
    name = "{0}_{1}".format(sex, stage)
    fpkms[name] = fpkm
    
fpkms_df = pd.DataFrame(fpkms)
fpkms_df.to_csv(sys.stdout)