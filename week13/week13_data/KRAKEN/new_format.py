#!/usr/bin/env python

"""
./new_format.py <file>
"""

import sys

krak = open(sys.argv[1])

dic = {}

for i in krak:
    fields = i.split(";")
    if fields[-1] in dic:
        dic[fields[-1]] += 1
    else:
        dic[fields[-1]] = 1

krak.seek(0)
for i in krak:
    fields = i.split(";")
    fields[0] = str(dic[str(fields[-1])])
    print("\t".join(fields))






