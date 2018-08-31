#!/usr/bin/env python3

"""
Usage: ./03-timecourse_reps14.py <t_name> <samples.csv>  <replicates.csv> <ctab_dir>
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

def plot(csv, gender):
    frame = pd.read_csv(csv)
    soi = frame.loc[:, "sex"] == gender
    frame = frame.loc[soi, :]

    fpkms = []

    for index, sample, sex, stage in frame.itertuples():
        filename = os.path.join(sys.argv[4], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col="t_name")
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        
    return fpkms


female_fpkm_samp = plot(sys.argv[2], "female")
female_fpkm_rep = plot(sys.argv[3], "female")
male_fpkm_samp = plot(sys.argv[2], "male")
male_fpkm_rep = plot(sys.argv[3], "male")
stages_samp = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
stages_rep = ["14A", "14B", "14C", "14D"]
    
fig, ax = plt.subplots()
ax.set_title(sys.argv[1])
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (FPKM)")
#ax.plot(stages_samp, male_fpkm_samp, color="blue", label="male")
ax.plot(stages_samp, female_fpkm_samp, color="red", label="female")
ax.plot(stages_rep, male_fpkm_rep, color="black", label="male rep")
#ax.plot(stages_rep, female_fpkm_rep, color="green", label="female rep")
plt.tight_layout()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5), frameon = False)
plt.xticks(stages_samp, rotation="vertical")
fig.savefig("timecourse_reps14-5.png")
plt.close(fig)