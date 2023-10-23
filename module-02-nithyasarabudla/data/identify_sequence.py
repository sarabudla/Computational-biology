# nucleic acid -> [a,t,c,g]
#nucleic = true
# read line
# split the line into nucleotides
# check if the nucleotide belongs to the sequence in nucleic acid
# if it is true
# else set nucleic=false
# after reading all line, if nucleic == True,
# print it is nucleic acid
# else
# print it is an amino acid


# open a file and read its contents
nucleic_acid_sequence=["A","T","G","C", "a", "t", "c", "g"]
nucleic= True

with open("sequence1.txt") as file:
    for line in file:
        for nucleotide in line.strip():
            if nucleotide in nucleic_acid_sequence:

                continue
            else:
                nucleic= False

if nucleic==True:
    print("it is an nucleic acid sequence")
else:
    print("it is an amino acid sequence")

