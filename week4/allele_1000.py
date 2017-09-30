#!/usr/bin/env python


import sys
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

seg = open(sys.argv[1])


allele_freq=[]
for i in seg:
    if i.startswith("#"):
        continue 
    line = i.rstrip("\t\n").split()
    #af = line[7].split()
    af1 = line[7][3:]
    print af1
    if "," in af1:
        af2 = af1.split(",")
        for i in af2:
            allele_freq.append(float(i))
    else:
        allele_freq.append(float(af1))

plt.figure()
plt.hist(allele_freq, bins=20)
plt.savefig("histo_allele.png")
plt.close()
