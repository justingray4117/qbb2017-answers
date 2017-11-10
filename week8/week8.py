#!/usr/bin/env python

import numpy 
import sys
"""
./week8.py week8_enrichment.heat.npz chrx_ctcf_peaks.tsv 
"""

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
r_numpy = numpy.argmax(ctcf_enrich, axis = 1)
r_val = numpy.amax(ctcf_enrich, axis = 1)

print 'Top reverse primer interactions'
rev_i = 0
for fwd_i in f_numpy:
    print 'Reverse region = %s, Forward region = %s, enrichment = %s' % (reverse[rev_i], forward[fwd_i], f_val[rev_i])
    rev_i += 1
print '\nTop forward primer interactions'
fwd_j = 0
for rev_j in r_numpy:
    print 'Forward region = %s, Reverse region = %s, enrichment = %s' % (forward[fwd_j], reverse[rev_j], r_val[fwd_j])
    fwd_j += 1







