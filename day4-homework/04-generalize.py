#!/usr/bin/env python3

"""
Usage: ./04-generalize.py <gene_name> <samples.csv> <ctab_dir>
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot(csv, gender, gene):
    frame = pd.read_csv(csv)
    soi = frame.loc[:, "sex"] == gender
    frame = frame.loc[soi, :]

    fpkms_avg = []

    for index, sample, sex, stage in frame.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col="t_name")
        roi = ctab_df.loc[:, "gene_name"] == gene
        fpkms = ctab_df.loc[roi, "FPKM"]
        fpkms_avg.append(np.mean(fpkms))
        
    return fpkms_avg

female_fpkm = plot(sys.argv[2], "female", sys.argv[1])
male_fpkm = plot(sys.argv[2], "male", sys.argv[1])
stages = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]


fig, ax = plt.subplots()
ax.set_title(sys.argv[1])
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (FPKM)")
ax.plot(stages, male_fpkm, color="blue", label="male")
ax.plot(stages, female_fpkm, color="red", label="female")
plt.tight_layout()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5), frameon = False)
plt.xticks(stages, rotation="vertical")
fig.savefig("timecourse_avg.png")
plt.close(fig)