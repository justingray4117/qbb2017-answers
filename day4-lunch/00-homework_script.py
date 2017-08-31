#!/usr/bin/env python

"""
Usage: ./00-homework_script.py <.ctab1> <.ctab2>

- label axis and title of plot, one needs to be one color, the other file needs to have another color
- log transform values
- 
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import scipy

df1_fpkm = {}

coi = ["gene_names", "FPKM"]

df1 = pd.read_csv( sys.argv[1], sep="\t" )



df2_fpkm = {}

df2 = pd.read_csv( sys.argv[2], sep="\t" )


x = numpy.log1p(df1["FPKM"])

y = numpy.log1p(df2["FPKM"])

plt.figure()
plt.plot(numpy.unique(x), numpy.poly1d(numpy.polyfit(x, y, 1))(numpy.unique(x)))
plt.scatter(x,y, alpha=0.2, c="lightblue")
plt.xlabel("log(FPKM file 1)")
plt.ylabel("log(FPKM file 1)")

plt.savefig( sys.argv[3] + ".png")
plt.close()



