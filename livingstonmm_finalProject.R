# BNFO301 Final Project
# Name: Mihcael Livingston 

library(ggplot2)
options(stringsAsFactors = FALSE)


# part 2: metagenomics RDP data analysis ----------------------------------

# 3. load and prepare rdp-all-taxa.txt
dir.create("data", showWarnings = FALSE)
download.file("http://wolen.s3.amazonaws.com/bnfo301/rdp-all-taxa.txt",
              destfile = "data/rdp-all-taxa.txt")
rdp.all = read.table("data/rdp-all-taxa.txt", header = FALSE, sep = "\t", col.names = c("sample", "taxarank", "entity", "numreads", "abundance", "avgscore"))
rdp.all$taxarank <- as.factor(rdp.all$taxarank)

ggplot(data = rdp.all, aes(x = abundance, fill = rdp.all$taxarank)) + geom_histogram(binwidth = 5)  
# 4. genus-level data for all samples
rdp.genus = rdp.all[rdp.all$taxarank == "genus",]
ggplot(data = rdp.genus, aes(x = abundance, fill = taxarank)) + geom_histogram(binwidth = 7, fill = "yellow")

# 5. genus-level data for an individual sample
rdp.indiv = rdp.genus[rdp.genus$sample == "s4882",] 
rdp.sorted <- rdp.indiv[order(-rdp.indiv[5]),]
head(rdp.sorted,10)

# part 3: survey data -----------------------------------------------------

# 7. load and prepare rdp-genus-and-metadata.csv

dir.create("data", showWarnings = FALSE)
download.file("http://wolen.s3.amazonaws.com/bnfo301/rdp-genus-and-metadata.csv",
              destfile = "data/rdp-genus-and-metadata.csv")
metadata = read.table("data/rdp-genus-and-metadata.csv", header = TRUE, sep = ",")
metadata$age <- as.factor(metadata$age)
metadata$smoker = as.factor(metadata$smoker)
metadata$brush.freq  <- as.factor(metadata$brush.freq )
metadata$brush.method = as.factor(metadata$brush.method)
metadata$soda = as.factor(metadata$soda)
# 8. examine gender and oral hygiene

#Gender and brushing characteristics 
ggplot(data = metadata, aes(x = sex, fill = brush.freq)) + geom_bar(position = "stack")
ggplot(data = metadata, aes(x = sex, fill = brush.method)) + geom_bar(position = "stack")
ggplot(data = metadata, aes(x = sex, fill = brush.today)) + geom_bar(position = "stack")

ggplot(data = metadata, aes(x = sex, fill = soda)) + geom_bar(position = "stack")


# 9. examine bacteria (Streptococcus and Gemella) and brushing behavior (brush.today and brush.freq) relationships
ggplot(data = metadata, aes(x = Gemella, fill = brush.today)) + geom_histogram(binwidth = 3)
ggplot(data = metadata, aes(x = Streptococcus, fill = brush.today)) + geom_histogram(binwidth = 3)
ggplot(data = metadata, aes(x = Gemella, fill = brush.freq)) + geom_histogram(binwidth = 3)
ggplot(data = metadata, aes(x = Streptococcus, fill = brush.freq)) + geom_histogram(binwidth = 3)
# 10. examine smokers (combine daily and monthly smokers) and those who never smoke.
smokers = metadata$smoker != "Never"
nonSmokers = metadata$smoker == "Never"

ggplot(data = metadata, aes(x = smokers, y = Haemophilus, fill = smokers)) + geom_boxplot()
ggplot(data = metadata, aes(x = smokers, y = Haemophilus, fill = nonSmokers)) + geom_boxplot()

ggplot(data = metadata, aes(x = smokers, y = Actinomyces, fill = smokers)) + geom_boxplot()
ggplot(data = metadata, aes(x = smokers, y = Actinomyces, fill = nonSmokers)) + geom_boxplot()

ggplot(data = metadata, aes(x = smokers, y = Neisseria, fill = smokers)) + geom_boxplot()
ggplot(data = metadata, aes(x = smokers, y = Neisseria, fill = nonSmokers)) + geom_boxplot()

# 11. Calculate correlations among all pairwise combinations of the following genera: Streptococcus, Gemella, Fusobacterium, Neisseria.
cor(metadata$Streptococcus, metadata$Gemella)
cor(metadata$Gemella, metadata$Neisseria)
cor(metadata$Streptococcus, metadata$Fusobacterium)
cor(metadata$Fusobacterium, metadata$Neisseria)
cor(metadata$Streptococcus, metadata$Neisseria)
cor(metadata$Gemella, metadata$Fusobacterium)
