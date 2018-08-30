#!/usr/bin/env python3

"""
Usage: ./02-timecourse_reps.py <t_name> <samples.csv> <ctab_dir>
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

def plot(frame, gender):
    soi = frame.loc[:, "sex"] == gender
    frame = frame.loc[soi, :]

    fpkms = []

    for index, sample, sex, stage in frame.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col="t_name")
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        
    return fpkms

df = pd.read_csv(sys.argv[2])
female_fpkm = plot(df, "female")
male_fpkm = plot(df, "male")
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
fig.savefig("timecourse_both.png")
plt.close(fig)