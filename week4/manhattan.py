#!/usr/bin/env python


import sys
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
import math

new_list = [
"plink.P1.assoc.linear",
"plink.P2.assoc.linear",
"plink.P3.assoc.linear",
"plink.P4.assoc.linear",
"plink.P5.assoc.linear",
"plink.P6.assoc.linear",
"plink.P7.assoc.linear",
"plink.P8.assoc.linear",
"plink.P9.assoc.linear",
"plink.P10.assoc.linear",
"plink.P11.assoc.linear",
"plink.P12.assoc.linear",
"plink.P13.assoc.linear",
"plink.P14.assoc.linear",
"plink.P15.assoc.linear",
"plink.P16.assoc.linear",
"plink.P17.assoc.linear",
"plink.P18.assoc.linear",
"plink.P19.assoc.linear",
"plink.P20.assoc.linear",
"plink.P21.assoc.linear",
"plink.P22.assoc.linear",
"plink.P23.assoc.linear",
"plink.P24.assoc.linear",
"plink.P25.assoc.linear",
"plink.P26.assoc.linear",
"plink.P27.assoc.linear",
"plink.P28.assoc.linear",
"plink.P29.assoc.linear",
"plink.P30.assoc.linear",
"plink.P31.assoc.linear",
"plink.P32.assoc.linear",
"plink.P33.assoc.linear",
"plink.P34.assoc.linear",
"plink.P35.assoc.linear",
"plink.P36.assoc.linear",
"plink.P37.assoc.linear",
"plink.P38.assoc.linear",
"plink.P39.assoc.linear",
"plink.P40.assoc.linear",
"plink.P41.assoc.linear",
"plink.P42.assoc.linear",
"plink.P43.assoc.linear",
"plink.P44.assoc.linear",
"plink.P45.assoc.linear",
"plink.P46.assoc.linear"]


seg = open(sys.argv[1])

p_sig = []
p_nosig = []

lines = -1
for i in seg:
    fields = i.split()
    # print fields[8]
    if "CHR" in i:
        continue
    elif "NA" in i:
        continue
    lines += 1


for i in range(lines+5):
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