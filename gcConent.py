with open('1b.fasta') as f:
    protein = f.readlines()
#protein = file.readlines()
#protein = ">ACTG"


def GCcalc(prot):


	total =0.0
	GC = 0.0
	prot = prot.strip()
	for i in prot:
		if i.startswith(">"):
			pass
		else:
			total+=1
			if i == "G" or i == "C":
				GC +=1

			
	GCcontent = float(GC/total)	*100
	return GCcontent 
	return total+GC


print GCcalc(protein)


