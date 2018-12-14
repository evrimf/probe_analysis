#Last Edit: 2018-12-12 - percentiles for mathieson2015 probes were added, probe indices were changed
#           2018-11-18 - changed captured and probe indices for haak_ancient,added argument4, updated percentiles for haak_ancient
#           2018-11-16 - updated the percentiles and change outfile path  
#Find the captured number of each snp who has the gc-content between the percentile interval
#writes those snps in the gcperc files
#gcperc: means that the probes of those snps are included in that GC-percentile 
##
#Takes 3 arguments
#argument1 : whole path of captured bed file
#argument2 : whole path of gc-content of probes
#argument3 : whole path of outfile 
#argument4 : number of individuals

import sys

captured=sys.argv[1]
probegc=sys.argv[2]
path=sys.argv[3]
ind_no=int(sys.argv[4])

infile1=open("%s" %captured,"r")
infile2=open("%s" %probegc,"r")

#use these percentiles for mathieson2015
percentile=[0.0000000,0.3125000,0.3461538,0.3750000,0.3942308,0.4182692,0.4423077,0.4663462,0.4951923,0.5384615,0.8990385]

#use these percentiles for haak_ancient
#percentile=[0.1346154,0.3317308,0.3605769,0.3846154,0.4038462,0.4230769,0.4423077,0.4663462,0.4903846,0.5288462,0.8028846]

#use these percentiles for sheep_capture
#percentile=[0.1475410,0.3196721,0.3524590,0.3770492,0.4016393,0.4221311,0.4508197,0.4795082,0.5122951,0.5573770,0.7295082]

captured={}
for line in infile1:
    line=line.strip().split()
    captured[str(line[0])+"-"+str(line[2])]=str(float(line[3])/(2*ind_no))
print(captured)
probes=[]
for line in infile2:
    line=line.strip().split()
    probes.append(line)

for i in range(0,len(percentile)-1):
    outfile=open(path+"_"+str(i)+".bed","a")
    for k in range(0,len(probes)): 
        #probe indices can be changed according to probe file
        if float(probes[k][6])>=percentile[i] and float(probes[k][6])<=percentile[i+1]:
            chrno=probes[k][0]
            position=probes[k][1]
            snp=str(chrno)+"-"+str(position)
            try:
                outline=str(chrno)+"\t"+str(position)+"\t"+captured[snp]+"\n"
                outfile.write(outline)
            except KeyError:
                continue
