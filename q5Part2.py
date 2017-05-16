from clustal import ClustalPipeline, ClustalReport
#from __future__ import division, print_function
import re
import subprocess as sp
import sys
seq1 = open("seq1.fasta", "w")

def parse_fasta(file):
   header, DNAseq = None, [] #creates a None type and an empty list to store the sequences that are separated over lines
   for line in file: #iterates through lines
       line = line.rstrip() #removes newline characters
       if line.startswith(">"): #grabs lines starting ">"....signifies a header
           if header: yield (header, ''.join(DNAseq)) #If header is not a None type then returns a tuple with the header and the sequence.
           header, DNAseq = line, [] #resets
       else:
           DNAseq.append(line)
   if header: yield (header, ''.join(DNAseq)) #If header is not a None type then returns a tuple with the header and the sequence.

#dir(object) gives what can be done with an object
#regex: [0-8] matches any number between 0 and 8

def splitter(file):     #will return a list of filenames that have separated sequences
    filenames = []
    segment1 = []#creates an empty list that will be appended to below
    with open(file) as fp:	#opens file and
        for header, DNAseq in parse_fasta(fp):
            data = header.split("|")
            filenames.append(data[3])
            if "l" in data[3]:
			    #seq1.write(header, DNAseq)
                segment1 += (header , DNAseq)
                      #HMMMM some important code seems to be missing here!!!!
        print(segment1)
       # return set(filenames) #removes redundant filenames
if __name__ == '__main__':
        try:
                infile = sys.argv[1]
                outfile = sys.argv[2]
        except:
                print ("No infile and outfile given, invoking demo mode... using bat_flu.fasta & testout.aln")
                print ("Next time specify a file to be aligned & and output filename")
                infile = 'bat_flu.fasta'
                outfile = 'testout.aln'
		print("Intializing and running Clustal Omega Pipeline")
		print("Intializing and running Clustal Omega Pipeline")
        clustalpipe = ClustalPipeline(infile,outfile,10)
        clustalpipe.run()
        print("Finished Running Clustal Pipeline.")
        print("Beginning Parsing")
        alignment_report = ClustalReport(outfile)
        print ("Found alignment of: ",alignment_report.type,"With: ",len(alignment_report),"alignments.")
        print ("Overall alignment score: ",alignment_report.score())
        print ("Done")
	print(splitter(infile))
	print("here")

