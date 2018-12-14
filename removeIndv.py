#2018-12-12
#remove chimpanzee, human reference and the ancients that are used in previous studies
#we want to include only the new samples (230 Eurasians) 
infile=open("/mnt/NAS/projects/2018_human_capture/probe_content/mathieson2015/math_data.ped","r")
outfile=open("/mnt/NAS/projects/2018_human_capture/probe_content/mathieson2015/math_data2.ped","a")

for line in infile:
    line=line.strip().split()
    if (line[1]=="Chimp") | (line[1]=="Href") | (line[1]=="Kostenki14") | (line[1]=="MA1") | (line[1]=="Ust_Ishim") :
        continue
    else:
        outline=" ".join(line)
        outline=outline+"\n"
        outfile.write(outline)
