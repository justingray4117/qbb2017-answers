#!/usr/bin/env python

"""
./03-dN_dS <nucleotidesequence.fa>
"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

nucleotide = open(sys.argv[1])

dN = []

dS = []

#4871 represents the length of the protein sequence
# this is building lists that can be indexed later 
for i in range(0,4871):
    dN.append(0)
    dS.append(0)

#builds a list full of both the query and target sequence
nucleotide_seq = []
for ident, sequences in fasta.FASTAReader( nucleotide ):
    nucleotide_seq.append(sequences)

#separates the query sequence into its own list
#separates the target sequences into their own list
query_seq = nucleotide_seq[:1]
target_seq = nucleotide_seq[1:]



#goes through and adds to dN at the codon position whenever the amino acid 
#coded by the codon in the target sequence is different than the amino acid
#that is coded by the codon in the query sequence. 

for n in range(len(target_seq)):
    count = 0
    prot_count = 0
    while count < 14614:
        target = target_seq[n][count:count+3]
        query = query_seq[0][count:count+3]
        if "-" in target_seq[n][count:count+3]:
            count += 3
            prot_count += 1
        elif "-" in query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target_seq[n][count:count+3] == query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target not in codontable:
            count += 100000
        elif codontable[target] != codontable[query]:
            dN[prot_count] = dN[prot_count] + 1
            count += 3
            prot_count += 1
        elif codontable[target] == codontable[query]:
            dS[prot_count] = dS[prot_count] + 1
            count += 3
            prot_count += 1
        else:
            print "Error in code"
#zips together a new list that subtracts dN from dS at every single index
#in the list
dN_dS = [int(n) - int(s) for n,s in zip (dN, dS)]

#calculates mean, standard deviation and standard error of the mean, and zscore
mean_dN_dS = np.mean(dN_dS)
std_dev_dN_dS = np.std(dN_dS)
SE_dN_dS = std_dev_dN_dS / np.sqrt(len(dN_dS))
zscore_dN_dS = mean_dN_dS / std_dev_dN_dS

#calcualtes the zscore for every positon in the dN_dS list
zscore_list = []
for i in dN_dS:
    mean = i 
    zscore_list.append(float(mean) / float(std_dev_dN_dS))


non_zero_dN = []
non_zero_dS = []

#adds one to every sequence in dN and dS to allow for dividng dN/dS and for doing a log scale later
for i in range(len(dN)):
    non_zero_dN.append(dN[i] + 1)
    non_zero_dS.append(dS[i] + 1)


#makes the log(dNdS) list
log_non_zero_dN_dS = [np.log2(float(n)/float(s)) for n,s in zip(non_zero_dN, non_zero_dS)]



#making two lists, one with all the significant values and None for nonsignificant and another
#for just the nonsignificant values and None for significant
signif = []
graph_log_dN_dS = []
for i in range(len(log_non_zero_dN_dS)):
    signif.append(None)
    graph_log_dN_dS.append(None)


for i in range(len(log_non_zero_dN_dS)):
    if log_non_zero_dN_dS[i] > np.log2(779):
        signif[i] = log_non_zero_dN_dS[i]
    elif log_non_zero_dN_dS[i] < np.log2(float(1)/float(779)):
        signif[i] = log_non_zero_dN_dS[i]
    else:
        graph_log_dN_dS[i] = log_non_zero_dN_dS[i]

non_zero_dN_dS = [(float(n)/float(s)) for n,s in zip(non_zero_dN, non_zero_dS)]

mean_non_zero_dN_dS = np.mean(non_zero_dN_dS)
std_dev_non_zero_dN_dS = np.std(non_zero_dN_dS)
SE_non_zero_dN_dS = std_dev_non_zero_dN_dS / np.sqrt(len(non_zero_dN_dS))
zscore_non_zero_dN_dS = (mean_non_zero_dN_dS)-1 / SE_non_zero_dN_dS



plt.figure()
plt.scatter(range(len(graph_log_dN_dS)), graph_log_dN_dS, alpha=.5, c="blue")
plt.scatter(range(len(signif)), signif, alpha=.7, c= "red")
plt.xlabel("Gene Locations")
plt.ylabel("log2(dN/dS)")
plt.savefig( "scatter_dN_dS" + ".png")
plt.close()
    
plt.figure()
plt.scatter(range(len(zscore_list)), zscore_list, alpha=.3)
plt.xlabel("Gene Locations")
plt.ylabel("zscore")
plt.savefig( "zscore" + ".png")
plt.close()
    
