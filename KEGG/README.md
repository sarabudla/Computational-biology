# addKEGGPathways.py
search through web data from KEGG API to find out Genes, orthologs and Pathways associated with Uniprot IDs
and append to file.

# Input data 
The output of module-09 alignpredicted.txt is used as input data in module-10 assignment.

# KEGG API
An Application Programming Interface or API provides a programmatic way to access data from a service like KEGG. We change parameters in a URL to request specific data from the API.
curl and wget are two command-line programs that will capture data from a URL.

# getOneKegg.sh
It get the SwissProt to KEGG conversion for one protein and write the results in a tabular file.

# getOneKo.sh
gets the KEGG ortholog for one KEGG protein ID.

# getOnePath.sh
gets the KEGG pathways associated with a KEGG ortholog. 

writing a Python script to use our data/alignPredicted.txt tabular data as input and call the KEGG API to get pathway names.

# Script addKEGGPathways.py
Filtering to only BLAST output where evalue < 1e-50.
Appending the KEGG Ortholog ID, KEGG Pathway ID, and KEGG Pathway Description for each of the SwissProt (Uniprot) IDs.

# get_args():  
gets an input filename, e-value threshold, and output filename from the command line arguments.

# getUniProtFromBlast(): 
Returns UniProt ID from the BLAST line if the evalue is below the threshold.Returns False if evalue is above threshold.

# loadKeggPathways(): 
Returns dictionary of key=pathID, value=pathway name from http://rest.kegg.jp/list/pathway/ko 
Example: keggPathways["path:ko00564"] = "Glycerophospholipid metabolism"

# getKeggGenes():
Returns a list of KEGG organism:gene pairs for a provided UniProtID.

# getKeggOrthology(): 
Returns the KEGG Orthology ID (e.g., ko:K01108) for a provided KEGG ID (e.g., 'hsa:4534'); model it on getKeggGenes() function.

# getKeggPathIDs(): 
write yourself to return the KEGG Path IDs (e.g., path:ko01100, path:ko00562) for a provided KEGG Orthology ID (e.g., ko:K01108); model it on getKeggGenes() function.

# addKEGGPathways():
It ties all the other functions together to accomplish the assignment prompt.

# Author 
Nithya Sarabudla

# Date Created
09-12-2022

# References
1. KEGG: Kyoto Encyclopedia of Genes and Genomes. (n.d.). https://www.genome.jp/kegg/
2. KEGG PATHWAY Database. (n.d.). https://www.genome.jp/kegg/pathway.html 
3. KO (KEGG ORTHOLOGY) Database. (n.d.-b). https://www.genome.jp/kegg/ko.html 
