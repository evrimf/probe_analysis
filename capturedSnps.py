#!/usr/bin/env python3

import sys

#give path and file name as an argument
tped=sys.argv[1]
outbed=sys.argv[2]

infile=open("%s" %tped, "r")
outfile=open("%s" %outbed,"a")

for line in infile:
    line=line.strip().split()
    chr=line[0]
    rsid=line[1]
    position=line[3]
    genotypes=line[4:]

    count=0
    for i in range(0,len(genotypes)-1):
        if str(genotypes[i])!=str(0):
            count+=1
        else:
            continue
    out_line=str(chr)+"\t"+str(rsid)+"\t"+str(position)+"\t"+str(count)+"\n"
    outfile.write(out_line)
