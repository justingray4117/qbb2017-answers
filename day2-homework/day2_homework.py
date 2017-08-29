#!/usr/bin/env python

import sys


lines = sys.stdin.readlines()

for i in lines:
    if "DROME" in i:
        fields = i.split()
        if "FBgn" not in i:
            continue
        print fields[-1], "\t", fields[-2]