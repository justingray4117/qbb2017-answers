#!/usr/bin/env python


"""
./week10.py hema_data.txt 

Takes the microarray data in different cell lines from the hema file and gives 
you a heat graph, a graph depicted the genes that were differentially expressed
A dendrogram to go with the heat graph. The k-means clustering of genes plotted
against CFU and poly
"""

import numpy as np
import sys
from scipy import stats
import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
from sklearn import datasets
from scipy.cluster.vq import kmeans2,whiten

hema = open(sys.argv[1])

#reads file and makes a panda dataframe. Uses the 0th colum as the reference column
df = pd.read_csv(sys.argv[1],sep='\t',index_col=0)

#gets the linkage data and leaves_list from the rows. Should probably 
#set to average 
rows = hac.linkage(df.values)
leaves_rows = hac.leaves_list(rows)

#gets the linkage data and leaves_list from the columns. Should probably 
#set to average 
columns = hac.linkage(np.transpose(df).values)
leaves_columns = hac.leaves_list(columns)

#Builds a new matrix with the leaves_rows and leaves_columns
X = df.values
X = X[leaves_rows,:][:,leaves_columns]

print "Rows =", leaves_rows, "\nColumns =", leaves_columns

labels = []

row_header = list(df.columns.values)
for i in leaves_columns:
    labels.append(row_header[i])

m = np.max(np.abs(X))

#plt.figure()                                 # Open a blank canvas
#plt.title("Heatmap of Iris characteristics") # Add a title to the top
#plt.imshow(                                  # Treat the values like pixel intensities in a picture
#    X,                                       # ... Using X as the values
#    aspect='auto',                           # ... 'Stretch' the image to fit the canvas, so you don't get a skinny strip that is 4x150 pixels
#    interpolation='nearest',                 # ... Don't use any blending between pixel values
#    cmap="RdBu",                             # ... Use the Red-white-blue colormap to assign colors to your pixel values
#    vmin=-1*m,                               # ... Set the lowest value to show on the scale
#    vmax=m,                                  # ... Set the highest value to show on the scale. Since we are using a 'diverging' colormap, these should match.
#    )
#plt.grid(False)        # Turn of the grid lines (a feature added automatically by ggplot)
#plt.xticks(            # Edit the xticks being shown
#    range(X.shape[1]), # ... use the values centered on each column of pixels
#    labels,            # ... which corresponds to the indices of our labels
#    rotation=50,       # ... and rotate the labels 50 degrees counter-clockwise
#    )
#plt.yticks([])         # Edit the ticks on the y-axis to show....NOTHING
#plt.colorbar()         # Add a bar to the right side of the plot which shows the scale correlating the colors to the pixel values#
#plt.subplots_adjust( # Adjust the spacing of the subplots, to help make everything fit
#    left = 0.05,     # ... the left edge of the left-most plot will be this percent of the way across the width of the plot
#    bottom = 0.15,   # ... the bottom edge of the bottom-most plot will be this percent of the way up the canvas
#    right = 1.0,     # ... the right edge of the right-most plot will be this percent of the way across the width
#    top = 0.95,      # ... the top edge of the top-most plot will be this percent of the way from the bottom
#)#
#plt.savefig("clean_heatmap.png") # Save the image
#plt.close() # Close the canvas
#plt.figure()
#dn = hac.dendrogram(columns)
#plt.show()
#matrix_cfu_poly = df.as_matrix(columns=df.columns[1::4])##

#new_matrix = whiten(matrix_cfu_poly)#
#kmean,labels= kmeans2(new_matrix,2)##

#print kmean , labels##

#x = matrix_cfu_poly[:,0]
#y = matrix_cfu_poly[:,1]##
#

#label = []
#species = ["1","2","3","4"]##

#plt.figure()                     # Create a blank canvas
#plt.scatter(x,y)                 # Plot x vs y as points
#plt.savefig("first_scatter.png") # Save the figure
#plt.close()                      # Close the canvas##

#colors = ['darkblue','orange','cyan',"blue"] # List some colors to plot the points with
#ms = ['o','d','s','d']                    # Choose some marker styles for plotting, a circle, diamond, and a square.#
#plt.figure()                          # Create a new blank canvas
#plt.title("kmean")   # Add a title to the top, spanning two lines
#for i in range(len(species)):         # Iterate through indices corresponding to species names
#    plt.scatter(                      # ...Create a scatter plot
#        x[labels==i],                      # ... ... of x
#        y[labels==i],                      # ... ... vs y
#        c=colors[i],                  # ... ... set the color of these points
#        marker=ms[i],                 # ... ... and pick the marker style
#        label=species[i]              # ... ... finally, label the points of this set with the species name
#        )
#plt.legend(loc='upper left')          # Add a legend to the top left
#plt.xlabel("CFU")                 # label the x-axis
#plt.ylabel("poly")                 # label the y-axis
#plt.scatter(kmean[:,0],kmean[:,1])
#plt.savefig("clean_scatter.png")      # Save the figure
#plt.close()              #
#print len()


#diff_numpy = df.values

diff = df.ix[:,["CFU","mys","unk","poly"]]

diff_matrx = diff.as_matrix(columns = df.columns[0:5])

scipy_t = []

p_value = []

CFU_mys=  diff_matrx[:,0:2]

unk_poly = diff_matrx[:,2:4]

for i in range(len(diff)):
     t_stat,p_val = stats.ttest_ind(CFU_mys[i],unk_poly[i], axis=0)
     p_value.append(p_val)

print p_value
print sorted(p_value)




#for i in range(len(scipy_t)):
#    fields = scipy_t[i].split("pvalue=")
#    p_value.append(fields[1])#

#print p_value


#diff["CFU"] = diff[["CFU","mys"]].mean(axis=1)
#diff["unk"] = diff[["unk","poly"]].mean(axis=1)





