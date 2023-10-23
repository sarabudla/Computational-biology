# Genome assembly

## overview
Assembling the Rhodobacter spheroides genome.

## Author
Nithya Sarabudla

## Date Created
07-11-2022

## Methods

### fasterq-dump
The command-line utility to retrieve sequence data in FASTQ format from the SRA is fasterq-dump.
The flag --split-3 is required to separate paired reads into left and right ends.

### Trimmomatic
Trimmomatic is a trimmer that uses a sliding window to determine where quality scores have dropped below a specified threshold.Trimmomatic also removes any adapter sequences from the reads
LEADING and TRAILING determine the minimum quality for trimming the start and end of reads.
SLIDINGWINDOW indicates the sliding window size and the minimum average quality for the bases in that window. 
MINLEN specifies the minimum length for a read to be kept.

### SPAdes
 By SPAdes the quality-trimmed paired reads were assembled, producing contigs, scaffolds, and other output.

### Quast
Using the Rhodobacter genome as a reference the scaffold assembly from the prior phase was then processed 

## Conclusion
### Analysis 
The N50 value of the assembly is 25496.  Ifthe N50 value is higher then gemone assembly is good.
Lower the number of gaps, better is the genome assembly.
The number of N's per kbp is zero, that means no nucleotides are left unknown therefore it indicates good assembly.
The N90 value and NG50 is higher then better the genome assembly.






