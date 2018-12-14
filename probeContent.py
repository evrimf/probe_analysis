#!/usr/bin/env python3
##Last edit:2018-12-12: changed prob indices, remove snpid, add mean 

import sys
import numpy as np

probe_list=sys.argv[1]
out=sys.argv[2]
infile=open("%s" %probe_list, "r")
outfile=open("%s" %out,"a")

for line in infile:
    line=line.strip().split()
    chrno=line[0]
    position=line[1]
    prob1=line[2]
    prob2=line[3]
    prob3=line[4]
    prob4=line[5]

    #calculate gc content of the first probe
    prob1gc=prob1.count("G")+prob1.count("C")
    prob1gc=prob1gc/len(prob1)

    #calculate gc content of the second probe
    prob2gc=prob2.count("G")+prob2.count("C")
    prob2gc=prob2gc/len(prob2)

    #calculate gc content of the third probe
    prob3gc=prob3.count("G")+prob3.count("C")
    prob3gc=prob3gc/len(prob3)

    #calculate gc content of the fourth probe
    prob4gc=prob4.count("G")+prob4.count("C")
    prob4gc=prob4gc/len(prob4)
    
    prob_gc=[prob1gc,prob2gc,prob3gc,prob4gc]
    meangc=np.mean(prob_gc)
    outline=str(chrno)+"\t"+str(position)+"\t"+str(prob1gc)+"\t"+str(prob2gc)+"\t"+str(prob3gc)+"\t"+str(prob4gc)+"\t"+str(meangc)+"\n"
    outfile.write(outline)
