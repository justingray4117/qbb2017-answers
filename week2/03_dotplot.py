#!/usr/bin/env python

"""
./01_N50 <dotplot.tsv>
"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

data = open(sys.argv[1])



count = 0
plt.figure()
for i in data:
    if "zstart1" in i:
        continue
    else:
        fields = i.split("\t")
        plt.plot([count,count+1],[np.log10(int(fields[0])),np.log10(int(fields[1]))])
        count += 1


plt.xlabel("Contig Names")
plt.ylabel("Position")
#make some sort of tick mark with low font
plt.savefig( "good_cov_align" + ".png")
plt.close()