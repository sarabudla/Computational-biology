# overview

The overview of the code is that it checks a particular sequence and outputs whether it is a nucleic acid,
an RNA sequence or an amino acid.

The code first parses commandline argument to take in the files and then reads the files. The code then converts
the contents of the files to a sequence and outputs the type of sequence in the file. To check the type of sequence,
I have first converted the sequence into a set of characters and checked it against the nucleotides expected in the
amino acid sequence and then rna sequence. If both of these are not true, then I return that it is a nucleic acid
sequence.


## Author
Nithya Sarabudla

## Date created
14-10-2022
