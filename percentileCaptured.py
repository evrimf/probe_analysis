#Last Edit: 2018-12-12 -percentiles for mathieson2015 were added, indices for probe chr and pos were changes
#           2018-11-18 -changed the indices of captured and probe files + updated percentiles for haak_ancient
#           2018-11-16 -updated percentile list and outfile path 
#Find the gccontent of each snp who has the capture number between the percentile interval
#writes those snps in the capperc files
#capperc: means that the probes of those snps are included in that capture-percentile 
##
#Takes 3 arguments
#argument1 : whole path of captured bed file
#argument2 : whole path of gc-content of probes
#argument3 : path for outfile

import sys

bed_file=sys.argv[1]
probegc=sys.argv[2]
path=sys.argv[3]

infile1=open("%s" %bed_file,"r")
infile2=open("%s" %probegc,"r")

##use these capture percentiles for mathieson2015
percentile=[0,80,122,155,180,201,218,233,247,263,377]
##use these capture percentiles for haak_ancient 
#percentile=[0,58,70,78,83,86,90,92,96,100,121]
##use these capture percentiles for sheep 
#percentile=[1,2,2,2,3,4,4,5,6,7,9]

captured=[]
for line in infile1:
    line=line.strip().split()
    captured.append(line)

probes={}
for line in infile2:
    line=line.strip().split()
    #chr=line[0], position=line[1],  meangc=line[6]
    #the indices can be changed according to probe file		
    probes[str(line[0])+"-"+str(line[1])]=line[6]   

for i in range(0,len(percentile)-1):
    outfile=open(path + "_" + str(i) + ".bed","a")
    for k in range(0,len(captured)):
        if  int(captured[k][3])>=percentile[i] and int(captured[k][3])<=percentile[i+1]:
            chrno=captured[k][0]
            position=captured[k][2]
            snp=str(chrno)+"-"+str(position)
            try:
                outline=str(chrno)+"\t"+str(position)+"\t"+probes[snp]+"\n"
                outfile.write(outline)
            except KeyError:
                continue
