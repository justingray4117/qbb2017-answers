#!/usr/bin/env python

"""
Usage ./00-boxplot.py <samples.csv> <ctab_dir> <replicates.csv> <gene_name>
- Plot timecourse of FBtr0331261 for females
"""

import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


gene = str(sys.argv[4])

df_samples = pd.read_csv( sys.argv[1] )




soi = df_samples["sex"] == "female"

fpkms_females = {}

for sample in df_samples["sample"][soi]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep = "\t")
    roi = df["gene_name"] == gene
    count = 0
    total = 0
    for fpkm in df["FPKM"][roi]:
         total += fpkm
         count += 1
    average = total/count
    fpkms_females[sample] = (average)


print fpkms_females

df_replicates = pd.read_csv( sys.argv[3] )

sroi = df_replicates["sex"] == "female"

fpkms_females_replicates = {}

for sample in df_replicates["sample"][sroi]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep = "\t")
    roi = df["gene_name"] == gene
    count = 0
    total = 0
    for fpkm in df["FPKM"][roi]:
         total += fpkm
         count += 1
    average = total/count
    fpkms_females_replicates[sample] = (average)


moi = df_samples["sex"] == "male"

fpkms_males = {}

for sample in df_samples["sample"][moi]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep = "\t")
    roi = df["gene_name"] == gene
    count = 0
    total = 0
    for fpkm in df["FPKM"][roi]:
         total += fpkm
         count += 1
    average = total/count
    fpkms_males[sample] = (average)
    

fpkms_males_replicates = {}

mroi = df_replicates["sex"] == "male"

for sample in df_replicates["sample"][mroi]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep = "\t")
    roi = df["gene_name"] == gene
    count = 0
    total = 0
    for fpkm in df["FPKM"][roi]:
         total += fpkm
         count += 1
    average = total/count
    fpkms_males_replicates[sample] = (average)

male_fpkm_values = []

for sample in df_samples["sample"][moi]:
    male_fpkm_values.append(fpkms_males[sample])

print male_fpkm_values

count = 0    
for sample in df_replicates["sample"][mroi]:
    value = fpkms_males_replicates[sample]
    male_fpkm_values[4+count] = ((male_fpkm_values[4+count]+value)/2)
    count += 1

print male_fpkm_values


female_fpkm_values = []

for sample in df_samples["sample"][soi]:
    female_fpkm_values.append(fpkms_females[sample])

print female_fpkm_values

fcount = 0    
for sample in df_replicates["sample"][sroi]:
    fvalue = fpkms_females_replicates[sample]
    female_fpkm_values[4+fcount] = ((female_fpkm_values[4+fcount]+fvalue)/2)
    fcount += 1

print female_fpkm_values
    

x_ticks_labels = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
     

plt.figure()
plt.plot(female_fpkm_values, c="red", label="female")
plt.plot(male_fpkm_values, c="blue", label="male")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2.0, borderaxespad=0.)
plt.xticks(range(len(x_ticks_labels)),x_ticks_labels)
plt.title(str(gene))
plt.ylabel("mRNA abundance (FPKM)")
plt.xlabel("developmental stage")
plt.savefig( gene + "_advanced_homework_day4_" + ".png", bbox_inches="tight")
plt.close()