#!/usr/bin/env python3

import sys
import numpy as np

#give path of probe file as an argument and path with file name for output
argv=sys.argv[1]
path=sys.argv[2]

infile=open("%s" %argv,"r")
outfile=open("%s.bed" %path,"a")

probes=infile.readlines()
line_no=len(probes)
print(line_no)
for i in range(0,line_no,8):
    chr_no=probes[i].split("-")[1]
    position=probes[i].split("-")[2]
    var_id=probes[i].split("-")[3]
    gc1=(probes[i+1].count("G")+probes[i+1].count("C"))/len(probes[i+1])
    gc2=(probes[i+3].count("G")+probes[i+3].count("C"))/len(probes[i+3])
    gc3=(probes[i+5].count("G")+probes[i+5].count("C"))/len(probes[i+5])
    gc4=(probes[i+7].count("G")+probes[i+1].count("C"))/len(probes[i+7])
    mean_gc=np.mean([gc1,gc2,gc3,gc4])
    outline=str(chr_no)+"\t"+str(position)+"\t"+str(var_id)+"\t"+str(gc1)+"\t"+str(gc2)+"\t"+str(gc3)+"\t"+str(gc4)+"\t"+str(mean_gc)+"\n"
    outfile.write(outline)
