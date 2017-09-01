#!/usr/bin/env python

"""
./05-linear_regression.py <.tab> <.ctab>
"""


import sys
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv( sys.argv[2], sep="\t" )
#n,p = df.shape()
coi = ["FPKM"]


fpkms=[]

for value in df[coi].values:
    fpkms.append(float(value))
    

f = open( sys.argv[1] )

bigWig = []


for line in f:
    fields = line.rstrip("\r\n").split("\t")
    bigWig.append(float(fields[5]))


x = bigWig
y = fpkms
xc = sm.add_constant(x)


model = sm.OLS(y,xc)
results = model.fit()
print results.params
print results.summary()
print results.rsquared
plt.figure()
plt.scatter(x,y, alpha=0.8, c="lightblue")
plt.title(str(sys.argv[1]))
plt.ylabel("mRNA abundance (FPKM)")
plt.xlabel("bigWigAverageOverBed")
plt.savefig( "Histone_vs_FPKM" + ".png", bbox_inches="tight")

