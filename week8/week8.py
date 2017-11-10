#!/usr/bin/env python

import numpy 
import sys


npz = open(sys.argv[1])
ctcf = open(sys.argv[2])
data=numpy.load(npz)
ctcf_pos = []
enrichment = data["0.enrichment"]
forward = data["0.forward"]
reverse = data["0.reverse"]
for i in ctcf:
    fields = i.split()
    ctcf_pos.append(float(fields[1]))


f_index=[]
r_index=[]

for i,frag in enumerate(forward):
    for j,pos in enumerate(ctcf_pos):
        if frag[0] <pos and frag[1]>pos:
            f_index.append(i)

for i,frag in enumerate(reverse):
    for j,pos in enumerate(ctcf_pos):
        if frag[0] <pos and frag[1]>pos:
            r_index.append(i)




print f_index
print r_index

ctcf_enrich=enrichment[f_index,:][:,r_index]

f_numpy = numpy.argmax(ctcf_enrich, axis = 0)
f_val = numpy.amax(ctcf_enrich, axis = 0)



#print numpy.argmax(ctcf_enrich, axis = 1)
#print numpy.amax(ctcf_enrich, axis = 1)
print len(f_index)
count = 0
for i in f_numpy:
    print reverse[f_index[i]] + " " + f_val[count]
    count += 1

print reverse
#for i in range(len(r_numpy)):


#for i,pos in enumerate([f_index,:]):
#    v = 0
#    index = 0
#    for j,frag in enumerate(ctcf_enrich.row()):
#        if frag > v:
#            v = frag
#            index = j
#            print "Coorderinates = " + str(f_index[j]) + "," +  str(r_index[i]) + " Val = " + str(v)











