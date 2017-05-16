# !/usr/bin/env python
# pipeline.py
import sys,re,subprocess #import subprocess and stuff.

try: #try to capture 4 arguments from cli, otherwise print an error message with the usage
    sub = sys.argv[1]
    qfile = sys.argv[2]
    outfile = sys.argv[3]
    dbtype = sys.argv[4]
	evalue = sys.argv[5]
	
	if(evalue > 100000):
		print "evalue is supposed to be less than 1e-05"
		quit()
		
except:
    print "Usage: python Pipeline.py <subject_file> <input_query> <outputfile> <nucl or prot>"
    quit()
blastn='blastn' #path to blastn
makedb='makeblastdb' #path to make blastdb
blastp='blastp' #path to blastp

# write an if that skips the makedb if it exsists
#subprocess.Popen([makedb,'-in',sub,'-dbtype',dbtype,'-out',sub]).wait() #invoke subprocess to open the makeblastdb program using the arugments -in, -out and -dbtype, given the arguments from the command line... .wait() asks the script to wait till this finishes before going on, the default behaviors is to just keep going.
# THIS IS THE EQUIVALENT TO RUNNING:
#/usr/local/ncbi-blast-2.2.29+/bin/makeblastdb -in SUBJECT.fasta -dbtype nucleotide -out SUBJECT
if (dbtype == 'nucl'): #if we asked for nucleotides...
    subprocess.Popen([blastn,'-query',qfile,'-db',sub,'-outfmt','7 stitle qstart sstart qend send qcovs qseqid salltitles','-out','blastout.txt',evalue]).wait() #open blastn using -query, -db, -outfmt and -out as options and the variables qfile and sub as arguments, also outfmt has the arugments specified in quotes and -out writes everything to blastout.txt
else: #if we asked for proteins
#THIS IS EQUIVALENT TO RUNNING:
#/usr/local/ncbi-blast-2.2.29+/bin/blastn -query query.fasta -db SUBJECT -outfmt 7 stitle qstart sstart qend send qcovs qseqid salltitles -out outfile.txt
    subprocess.Popen([blastp,'-query',qfile,'-db',sub,'-outfmt','7 stitle qstart sstart qend send qcovs qseqid salltitles','-out','blastout.txt', evalue]).wait()
#subprocess.Popen(['python','analysis.py']) just playing...

try:
    infile=open('blastout.txt','r')
    outfile=open(outfile,'w')
except:
    print "Error in infile/outfile"
    quit()
threshold=97
for line in infile:
    line=line.strip()
    if re.match('\#',line):
        if re.search('Organism',line):
            query = re.search('virus\s(.*?)\|',line)
            currentq=query.group(1)
    else:
        fields=line.split('\t')
        subsplit=fields[0].split('|')
        subject=subsplit[1]
        qstart=fields[1]
        sstart=fields[2]
        coverage=int(fields[5])
		print qstart,sstart,coverage,threshold,coverage >= threshold
        if int(coverage) >= threshold and int(qstart) == 1 and int(sstart)  == 1:
            outfile.write('%s \t %s \t %s \n' % (currentq,subject,coverage))
outfile.close()
