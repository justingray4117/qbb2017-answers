#!/usr/bin/env python


import sys
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
import math


seg = open(sys.argv[1])

p_sig = []
p_nosig = []

lines = 5
for i in seg:
    fields = i.split()
    # print fields[8]
    if "CHR" in i:
        continue
    elif "NA" in i:
        continue
    lines += 1


for i in range(liness):
    p_sig.append(None)
    p_nosig.append(None)


count = 0
seg.seek(0)
for i in seg:
    fields = i.split()
    # print fields[8]
    if "CHR" in i:
        continue
    elif "NA" in i:
        continue
    elif "ADD" not in i:
        continue
    elif float(fields[8]) <= 10e-5:
        p_sig[count] = -np.log10(float(fields[8]))
        count += 1
    elif float(fields[8]) > 10e-5:
        p_nosig[count] = -np.log10(float(fields[8]))
        count += 1

plt.figure()
plt.scatter(range(len(p_sig)),p_sig,s=5,alpha=.6,c= "red")
plt.scatter(range(len(p_sig)),p_nosig,s=5, alpha=.6,c = "blue")
plt.xlabel("Gene Locations")
plt.ylabel("-log10(p)")
plt.savefig(str(sys.argv[2]) + "_manhattan_plot.png")
plt.close()

p_sig = []
p_nosig = []

seg.close()