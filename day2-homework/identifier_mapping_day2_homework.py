#!/usr/bin/env python

# ./identifier_mapping_day2_homework <fly_data> <.ctab file> [OPTIONAL]
#  -e for optional results in printing error in finding [gene ID]. 


import sys

identifier_map = {}

m = open(sys.argv[1])
for i in m:
    fields = i.split()
    f = fields[0]
    a = fields[1]
    identifier_map[f] = a
    


new_lines = open(sys.argv[2])
argument = sys.argv[-1]
for i in new_lines:
    fields = i.split("\t")
    f = fields[8]
    if "gene_id" in f:
        continue
    if argument == "-e":
        if f in identifier_map: 
            print i, "\t", identifier_map[f]
        else:
            print "error in finding: ", f
    else:
        if f in identifier_map:
            print i, "\t", identifier_map[f]
        
    





