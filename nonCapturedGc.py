##Last edit: 2018-12-12 -probe indices were changed 
#2018-12-11
##Find the gc-content of the snps that are not captured


import sys

bed=sys.argv[1]
probegc=sys.argv[2]
out=sys.argv[3]

infile1=open("%s" %bed, "r")
infile2=open("%s" %probegc, "r")
outfile=open("%s" %out, "a")

probesGC={}
for line in infile2:
    line=line.strip().split()
    probesGC[str(line[0])+"-"+str(line[1])]=line[6]

non_captured=[]
for line in infile1:
    line=line.strip().split()
    if line[3]==str(0):
        non_captured.append(str(line[0])+"-"+str(line[2]))

print(non_captured)
for i in non_captured:
    try:
        outline=str(i)+"\t"+str(probesGC[i])+"\n"
        outfile.write(outline)
    except KeyError:
        continue
