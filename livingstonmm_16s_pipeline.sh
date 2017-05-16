#read variables 
r1=$2
r2=$3
samplename=$1
#outdir=$4
#function create_dir{
#	if [[!-d$1]];
#	then
#		mkdir $1
#	fi 
#}
#create_dir$outdir 
echo "MEFIT - merging overlapping reads and quality filetering"
#MEFIT - merging overlapping reads and quality filetering 
mefit -s ${samplename}.q25 -r1$r1 -r2$r2-nonovlp -n 15 -avgq 25
#combine the high quality overlapping and nonovlp reads
cat ${samplename}.q25.ovlp.hq.fastq ${samplename}.q25.nonovlp.hq.fastq > ${samplename}.q25.combined.hq.fastq
#convert fastq to fasta file 
python /usr/local/bnfo/bin/fastq2fasta.py -i ${samplename}.q25.combined.hq.fastq -o ${samplename}.q25.combined.hq.fasta 
#RDP rdp_output.txt
java -Xmx2g -jar /usrcd /local/bnfo/rdp_classifier_2.12/dist/classifier.jar classify -c 0.80 -o rdp_output.txt ${samplename}.hq.nochimera.fasta 
##RDP rdp_hier.txt 
java -Xmx2g -jar /usr/local/bnfo/rdp_classifier_2.12/dist/classifier.jar classify -f filterbyconf -c 0.80 -o rdp_output.txt -h rdp_hier.txt ${samplename}.hq.nochimera.fasta
#Usearch 
sh /usr/local/bnfo/scripts/usearch_otu_pipeline.sh -s ${samplename} -f ${samplename}.hq.combined.fasta -r 3.0 -i 0.90 -d /usr/local/bnfo/refdb/SILVA123/forUsearch/97_otus_16S.forUsearch.udb