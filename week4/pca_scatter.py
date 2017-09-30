#!/usr/bin/env python


import sys
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math



pca = open(sys.argv[1])

pca1 = []
pca2 = []


for i in pca:
    fields = i.split()
    pca1.append(fields[2])
    pca2.append(fields[3])



plt.figure()
plt.scatter(pca1,pca2)
plt.savefig("pca_test.png")
plt.close()