# sbatch_transdecoder.sh

# Author 
Nithya Sarabudla

# Date Created
29-11-2022

# Scripts
longOrfs_args.sh
blastPep_args.sh
pfamScan_args.sh
predictProteins_args.sh
alignPredicted_args.sh
sbatch_transdecoder.sh

# Accessing Data
Using output data of module-08 assignment as input data in module-09 assignment.

# Running TransDecoder
# Methods

# Find longest open reading frames (ORFs)
 longOrfs_args.sh 
 #finds the longest open reading frames and translates them to amino acid (protein) sequences.

# Align Protein (from the ORFs) to SwissProt
 blastPep_args.sh
 # blastp 
 aligns the long ORFs to SwissProt to identify similar proteins that could guide the prediction process.

# Run hmmscan to find protein domains
pfamScan_args.sh
# hmmscan
uses a Hidden Markov Model (HMM) to find protein domains to guide the prediction process.
hmmscan takes the protein sequences found in the ORFs (open reading frames) and search for those against the profile-HMM database. More specifically, hmmscan is used to search protein sequences against collections of protein profiles. Then, for each sequence in the input file, use that query sequence to search the target database of profiles in hmm_db, and output ranked lists of the profiles with the most significant matches to the sequence.

# Predict proteins
 predictProteins_args.sh
# TransDecoder.Predict 
takes in the open reading frames, the BLAST output, and the domain information to refine the protein predictions and produce a protein fasta file (*.pep).The TransDecoder.Predict program predicts the likely coding regions from the ORFs identified by Transdecoder.LongOrfs and included results from homology searches (blast/hmmer results) as ORF retention criterion, and aligned with query sequences which are predicted protien sequences to Swissport.

# References
Alweshah, M., Alkhalaileh, S., Albashish, D., Mafarja, M., Bsoul, Q., & Dorgham, O. (2021). A hybrid mine blast algorithm for feature selection problems. Soft Computing (Berlin, Germany), 25(1), 517–534. https://doi.org/10.1007/s00500-020-05164-4
Kent, W. J. (2002). BLAT--the BLAST-like alignment tool. Genome Research, 12(4), 656–664. https://doi.org/10.1101/gr.229202
Haneef, J. (2014, February 2). Difference between PAM and BLOSUM Matrix. Major Differences. https://www.majordifferences.com/2014/02/difference-between-pam-and-blosum-matrix_1.html)
