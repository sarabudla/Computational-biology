# sbatch_alignRNAseq.sh
Aligning RNAseq Reads to a Reference genome.

# Author 
Nithya Sarabudla

# Date Created
14-11-2022

# shell scripts created

alignAll.sh - Align all samples
sortAll.sh - Sort the sam files
indexAll.sh - Index the bam files

# Methods

#Input Data
The input data for this assignment is a subset of an RNA-Seq experiment used to study immune response and symbiosis in sea anemones (Aiptasia pallida).
There were four treatment groups and six replicates per treatment group for a total of 24 anemones.The full data set would take too long to align, so we use QC sequencing run. A QC sequencing run produces a relatively small number of reads from a library to ensure everything is OK as far as the length and quality of the reads.

# Build GMAP Database
GSNAP will use this database to perform the alignment of the RNA-Seq reads. The GMAP database is indexed and optimized to allow much faster alignment than possible if the alignment were directly against the FASTA file.

we use for loop inside the bash script to write sam,bam and bai files at a time for all 24 fastq files.

# Reads were quality trimmed using with Trimmomatic

Trimmomatic is a Java-based quality trimmer that uses a sliding window to determine where quality scores have dropped below a specified threshold. Trimmomatic also removes any adapter sequences from the reads. The script trimAll.sh that trim all the reads.
LEADING and TRAILING determine the minimum quality for trimming the start and end of reads.
SLIDINGWINDOW indicates the sliding window size and the minimum average quality for the bases in that window.
MINLEN specifies the minimum length for a read to be kept.

# Reads were aligned with GSNAP

Wrote a bash script in the script alignAll.sh that allign all the samples.
GSNAP is a tool to align single- and paired-end reads to a reference genome.
Wrote a script in alignAll.sh.This shell script aligns the all samples in the data sets reads against the GMAP database.


# Alignments were sorted and indexed with samtools sort and samtools index

Wrote the bash script in sortAll.sh that sort all the sam files and indexAll.sh that index all the bam files.
samtools sort takes an input BAM-format file containing short DNA sequence reads and sorts it.
The samtools index command creates a new index file that allows fast look-up of the data in a sorted BAM file.
Indexing a genome sorted BAM file allows one to quickly extract alignments overlapping particular genomic regions.

# Reference citations

Wu, T. D., Reeder, J., Lawrence, M., Becker, G., & Brauer, M. J. (2016). GMAP and GSNAP for Genomic Sequence Alignment: Enhancements to Speed, Accuracy, and Functionality. Statistical Genomics, 283–334.https://doi.org/10. 1007/978-1-4939-3578-9_15

Bolger, A. M., Lohse, M., & Usadel, B. (2014). Trimmomatic: a flexible trimmer for Illumina sequence data. Bioinformatics, 30(15), 2114–2120. https://doi.org/10.1093/bioinformatics/btu170

Wu, T. D., & Watanabe, C. K. (2005). GMAP: a genomic mapping and alignment program for mRNA and EST sequences. Bioinformatics, 21(9), 1859–1875. https://doi.org/10.1093/bioinformatics/bti310

Li, H., Handsaker, B., Wysoker, A., Fennell, T., Ruan, J., Homer, N., Marth, G., Abecasis, G., & Durbin, R. (2009). The Sequence Alignment/Map format and SAMtools. Bioinformatics, 25(16), 2078–2079. https://doi.org/10.1093/bioinformatics/btp352


