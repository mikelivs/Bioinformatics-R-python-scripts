import sys

commandLine = sys.argv[1]
f_genome = open(commandLine, "r") # open fasta file
baseCount = 0 
gcCount = 0
sequences = []
qualityScore =[]
qualityNum =0
x =1 #counter to read right lines 

for line in f_genome:
	line.strip()	
	if x ==2: #looks for second line
		sequences.append(line[0:-2])
	if x == 4: #looks for fourth lins
		qualityScore.append(line[0:-2])
		x =0
	x+=1

sequenceLengthList = []
for line in sequences: 
	baseCount += len(line) #counts number of bases by taking the length of each line 
	sequenceLengthList.append(len(line))
	gcCount +=line.count("G") #looks for G in sequence line 
	gcCount +=line.count("C") #looks for C in sequence line 
	
		

for line in qualityScore: #iterates through quality scores(ASCII characters)
	for character in line: #goes character by character 
		ascScore = (ord(character)-33) #variable that takes in the character and converts it to its score 
		qualityNum += ascScore
		
#calculations			
reads = len(sequences)			
avgQuality = qualityNum/reads			
avgLength = baseCount/reads
gcPercent = (float (gcCount)/ float (baseCount))*100


print "Number of base: "+str(baseCount)
print "Number of Reads: " + str(reads)
print "GC Base Count: "+str(gcCount)
print "GC percentage: "+str(gcPercent)+"%"
print "Average Read Length: "+str(avgLength)
print "Average Read Quality: "+str(avgQuality)
print "Max read length: "+ str(max(sequenceLengthList))
print "Min read length: "+ str(min(sequenceLengthList))