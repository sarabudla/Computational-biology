# sbatch_trinity.sh
Performing transcriptome assembly using Trinity.

# Author
 Nithya Sarabudla

# Date Created
21-11-2022

# Input Data
Using the output from module-07 as input for this week module-08.Used the symbolic links to input the data. Then using Trinity for both reference-guided and de novo assemblies.

# Trinity
TRINITY is a software package for conducting de novo (as well as the genome-guided version of) transcriptome assembly from RNA-seq data. The Trinity package also includes a number of perl scripts for generating statistics to assess assembly quality, and for wrapping external tools for conducting downstream analyses.It saves all the intermediate files so that when you restart after an error, it picks up where it left off. 

# samtools
For a reference-guided assembly, Trinity requires a single sorted bam file as input. 
samtools is used to merge the 24 bam files into a single bam file. 
The command samtools merge can take a list of individual bam files.
Using the -b parameter to pass the bamin.txt. 
The merged bam files will be written to AipAll.bam.

#Created the shell script analyzeTrinity.sh. This script runs TrinityStats.pl with your assembled transcriptome as input.
The output stored in results/trinity_guided_stats.txt) contains size of your assembled contigs. Numbers like N10 and N50 are indicators of the length distribution of your assembly.

# N50
To get the N50 contig length, simply sort all contigs of a genome by their length, go to the base in the center at 50% of the total genome length, get the contig size to which this base belongs to and you have the N50 contig length.The N50 is lower in this assembly than in a typical assembly because we used a very small set of QC reads. Think about why this might create a lower N50 than expected.
The N50 value in the genome guided assembly of all contigs is 570 where as the same parameter for de novo is 603. The N50 for the longest isoform contig is 514 whereas the same parameter for de novo is 513.

# Citations

[1] Li, H., Handsaker, B., Wysoker, A., Fennell, T., Ruan, J., Homer, N., Marth, G., Abecasis, G., &amp; Durbin, R. (2009). The sequence alignment/map format and SAMtools. Bioinformatics, 25(16), 2078–2079. https://doi.org/10.1093/bioinformatics/btp352 

[2] Haas, B. J., Papanicolaou, A., Yassour, M., Grabherr, M., Blood, P. D., Bowden, J., Couger, M. B., Eccles, D., Li, B., Lieber, M., MacManes, M. D., Ott, M., Orvis, J., Pochet, N., Strozzi, F., Weeks, N., Westerman, R., William, T., Dewey, C. N., … Regev, A. (2013). De novo transcript sequence reconstruction from RNA-seq using the Trinity Platform for reference generation and analysis. Nature Protocols, 8(8), 1494–1512. https://doi.org/10.1038/nprot.2013.084

[3] Bankar, K. G., Todur, V. N., Shukla, R. N., &amp; Vasudevan, M. (2015). Ameliorated de novo transcriptome assembly using Illumina paired end sequence data with Trinity Assembler. Genomics Data, 5, 352–359. https://doi.org/10.1016/j.gdata.2015.07.012

[4] Grabherr, M. G., Haas, B. J., Yassour, M., Levin, J. Z., Thompson, D. A., Amit, I., Adiconis, X., Fan, L., Raychowdhury, R., Zeng, Q., Chen, Z., Mauceli, E., Hacohen, N., Gnirke, A., Rhind, N., di Palma, F., Birren, B. W., Nusbaum, C., Lindblad-Toh, K., … Regev, A. (2011). Full-length transcriptome assembly from RNA-seq data without a reference genome. Nature Biotechnology, 29(7), 644–652. https://doi.org/10.1038/nbt.1883 


