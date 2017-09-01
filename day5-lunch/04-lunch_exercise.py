#!/usr/bin/env python

"""
./04-lunch_exercise.py <.ctab> <output.bed>
SRR072893/t_data.ctab
"""


import sys
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv( sys.argv[1], sep="\t")


for row in df.itertuples():
    chrom = row[2]
    strand = row[3]
    start = row[4]
    end = row[5]
    t_name = row[6]
    
    if strand == "+":
        if start >= 500:
            tss = start
    else:
        tss = end
    
    if tss - 500 < 0:
        tss = 500
        
    tss_range = tss - 500, tss + 500
    nl = str(chrom) + "\t" + str(tss_range[0]) + "\t" + str(tss_range[1]) + "\t" + str(t_name)
    print nl




        