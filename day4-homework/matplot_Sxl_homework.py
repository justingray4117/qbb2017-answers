#!/usr/bin/env python

"""
Usage ./00-boxplot.py <samples.csv> <ctab_dir> <replicates.csv> 
- Plot timecourse of FBtr0331261 for females
"""

import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


transcript = "FBtr0331261"

df_samples = pd.read_csv( sys.argv[1] )

soi = df_samples["sex"] == "female"

fpkms_females = []

for sample in df_samples["sample"][soi]:
     fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
     df = pd.read_csv(fname, sep = "\t")
     roi = df["t_name"] == transcript
     fpkms_females.append(df[roi]["FPKM"].values)

df_replicates = pd.read_csv( sys.argv[3] )

fpkms_females_replicates = [0,0,0,0]

sroi = df_replicates["sex"] == "female"

for sample in df_replicates["sample"][sroi]:
     fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
     df = pd.read_csv(fname, sep = "\t")
     roi = df["t_name"] == transcript
     fpkms_females_replicates.append(df[roi]["FPKM"].values)


moi = df_samples["sex"] == "male"

fpkms_males = []

for sample in df_samples["sample"][moi]:
     fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
     df = pd.read_csv(fname, sep = "\t")
     roi = df["t_name"] == transcript
     fpkms_males.append(df[roi]["FPKM"].values)  



fpkms_males_replicates = [0,0,0,0]

mroi = df_replicates["sex"] == "male"

for sample in df_replicates["sample"][mroi]:
     fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
     df = pd.read_csv(fname, sep = "\t")
     roi = df["t_name"] == transcript
     fpkms_males_replicates.append(df[roi]["FPKM"].values)

x_ticks_labels = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
     

plt.figure()
plt.plot(fpkms_females, c="red", label="female")
plt.plot(fpkms_males, c="blue", label="male")
plt.plot(fpkms_males_replicates, c="lightblue", label="male replicate" )
plt.plot(fpkms_females_replicates, c="pink", label="female replicate")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2.0, borderaxespad=0.)
plt.xticks(range(len(x_ticks_labels)),x_ticks_labels)
plt.title("Sxl")
plt.ylabel("mRNA abundance (FPKM)")
plt.xlabel("developmental stage")
plt.savefig( "homework_day4_Sxl.png", bbox_inches="tight")
plt.close()
     
      
     
     
