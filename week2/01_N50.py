#!/usr/bin/env python

"""
./01_N50 <contig.fa>
"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

fasta_file = open(sys.argv[1])


nucleotide_seq = []
for ident, sequences in fasta.FASTAReader( fasta_file ):
    nucleotide_seq.append(sequences)
    
print "Statistics for Velvet"

nucleotide_length = []
for i in range(len(nucleotide_seq)):
    nucleotide_length.append(len(nucleotide_seq[i]))

nucleotide_length.sort()


print "Max = " + str(max(nucleotide_length))
print "Min = " + str(min(nucleotide_length))


contig_length = 0
for i in nucleotide_length:
    contig_length += i


print contig_length/2
count = 0
for i in nucleotide_length:
    if count < contig_length/2:
        count += i
    else:
        print "N50 = " + str(i) 
        break
        
print "Mean = " + str(np.mean(nucleotide_length))

