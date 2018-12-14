#Last edit: 2018-11-16
setwd("/mnt/NAS/projects/2018_human_capture/probe_content/sheep/")
gc_content=read.table("sheep_probe_gc.bed")
captured=read.table("sheep.tped.bed")
quantile(captured[,4],c(0.0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00)) #for capture number
quantile(gc_content[,8],c(0.0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.0)) #for gc contenti

###########################################################################
setwd("/mnt/NAS/projects/2018_human_capture/probe_content/sheep/percentile_capture/")
capperc0=read.table("capperc_1611_0.bed",sep="\t",header=F)
capperc1=read.table("capperc_1611_1.bed",sep="\t",header=F)
capperc2=read.table("capperc_1611_2.bed",sep="\t",header=F)
capperc3=read.table("capperc_1611_3.bed",sep="\t",header=F)
capperc4=read.table("capperc_1611_4.bed",sep="\t",header=F)
capperc5=read.table("capperc_1611_5.bed",sep="\t",header=F)
capperc6=read.table("capperc_1611_6.bed",sep="\t",header=F)
capperc7=read.table("capperc_1611_7.bed",sep="\t",header=F)
capperc8=read.table("capperc_1611_8.bed",sep="\t",header=F)
capperc9=read.table("capperc_1611_9.bed",sep="\t",header=F)

p0=capperc0[,3]
p1=capperc1[,3]
p2=capperc2[,3]
p3=capperc3[,3]
p4=capperc4[,3]
p5=capperc5[,3]
p6=capperc6[,3]
p7=capperc7[,3]
p8=capperc8[,3]
p9=capperc9[,3]

boxplot(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,
        names=c(".0-.1",".1-.2",".2-.3",".3-.4",".4-.5",".5-.6",".6-.7",".7-.8",".8-.9",".9-1"),ylab="gc-content",
        main="Sheep Capture Data 2018-11-16",xlab="percentiles based on capture number",las=2)

######################################################################
setwd("/mnt/NAS/projects/2018_human_capture/probe_content/sheep/percentile_gc/")
gcperc0=read.table("gcperc_1611_0.bed",sep="\t",header=F)
gcperc1=read.table("gcperc_1611_1.bed",sep="\t",header=F)
gcperc2=read.table("gcperc_1611_2.bed",sep="\t",header=F)
gcperc3=read.table("gcperc_1611_3.bed",sep="\t",header=F)
gcperc4=read.table("gcperc_1611_4.bed",sep="\t",header=F)
gcperc5=read.table("gcperc_1611_5.bed",sep="\t",header=F)
gcperc6=read.table("gcperc_1611_6.bed",sep="\t",header=F)
gcperc7=read.table("gcperc_1611_7.bed",sep="\t",header=F)
gcperc8=read.table("gcperc_1611_8.bed",sep="\t",header=F)
gcperc9=read.table("gcperc_1611_9.bed",sep="\t",header=F)

p0=gcperc0[,3]
p1=gcperc1[,3]
p2=gcperc2[,3]
p3=gcperc3[,3]
p4=gcperc4[,3]
p5=gcperc5[,3]
p6=gcperc6[,3]
p7=gcperc7[,3]
p8=gcperc8[,3]
p9=gcperc9[,3]

boxplot(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,
        names=c(".0-.1",".1-.2",".2-.3",".3-.4",".4-.5",".5-.6",".6-.7",".7-.8",".8-.9",".9-1"),
        ylab="number of captures",main="Sheep Capture Data 2018-11-16",
        xlab="percentiles based on mean GC-content of probes",las=2)
