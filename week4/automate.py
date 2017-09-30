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


for i in range(len(new_list)):
    os.system("./manhattan.py " + str(new_list[i]) + " " + str(new_list[i][6:9]))
    #print "./manhattan.py " + str(new_list[i]) + " " + str(new_list[i][6:9])
