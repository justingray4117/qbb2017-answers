#!/usr/bin/env python


"""
./heatmap_week13.py abundance_table.tab

"""

import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd


# pull out the columns in order 
# set row index as the species

df = pd.read_csv(sys.argv[1],sep='\t',index_col=0)


samples = ['SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']

df_2 = df[samples]

print df_2

labels = {"bin.1":'Staphylococcus haemolyticus',"bin.2":'Leuconostoc citreum',"bin.3":'Staphylococcus lugdunensis',"bin.4":'Enterococcus faecalis',"bin.5":'Cutibacterium avidum',"bin.6":'Staphylococcus epidermidis',"bin.7":'Staphylococcus aureus',"bin.8":"Anaerococcus prevotii"}

bin_labels = []

for i in df_2.index.tolist():
    bin_labels.append(labels[i])
#indexed_labels = labels[]
print bin_labels





plt.figure()
plt.imshow(df_2, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Newborn Gut Bacteria ")
plt.colorbar()
plt.xticks( range(len( df_2.columns)), df_2.columns, rotation = 'vertical')
plt.yticks( [ x for x in range(len(bin_labels)) ], bin_labels)
plt.tight_layout()
plt.savefig("week13_heatmap.png") # Save the image
plt.close()
