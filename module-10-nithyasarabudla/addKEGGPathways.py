#!/usr/bin/env python
"""Filename :  addKEGGPathways.py 

search through web data from KEGG API to find out Genes, orthologs and Pathways associated with Uniprot IDs
and append to file.
"""

import argparse
import requests

def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="addKEGGPathways.py program to add KEGG Pathways to an output file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Create a sequential argument (eg. it has to come in the order defined)
    parser.add_argument('-i','--infile', '---infilename', # name of the argument, we will later use args.word to get this user input
                        metavar='filename', # shorthand to represent the input value
                        help='user should give filename', # message to the user, it goes into the help menu
                        type=str, # type of input expected, could also be int or float
                        default='../data/alignPredicted.txt', # default option if no input is given by the user
                        #required=False # whether this input must be given by the user, could also be True
                        )
    parser.add_argument('-e','--evalue', # name of the argument, we will later use args.word to get this user input
                        metavar='evalue', # shorthand to represent the input value
                        help='user should give e value', # message to the user, it goes into the help menu
                        type=str, # type of input expected, could also be int or float
                        default='1e-50', # default option if no input is given by the user
                        #required=False # whether this input must be given by the user, could also be True
                        )

    # Create a flagged argument (eg. input comes after a short "-i" or long "--input" form flag)
    parser.add_argument('-o','--outfile', # name of the argument, we will later use args.number to get this user input
                        metavar='outfile', # shorthand to represent the input value
                        help='user should include outfile path', # message to the user, it goes into the help menu
                        type=str, # type of input expected, could also be int or float
                        default="../results/alignPredicted_results.txt", # default option if no input is given by the user
                        #required=False # whether this input must be given by the user, could also be True
                        )

    return(parser.parse_args())


def name_of_function(word, n=1):
    """What the function does (eg. Return duplicated word.)"""

    # Do things with the parameters above
    # to get to defining the "thing" you will return
    duplicated_word = word * n

    return(duplicated_word)


def getUniProtFromBlast(blast_line, threshold):
    """Return UniProt ID from the BLAST line if the evalue is below the threshold.

    Returns False if evalue is above threshold.
    """
    cleaned_line = blast_line.strip()
    blast_fields = cleaned_line.split('\t')
    if float(blast_fields[7]) < float(threshold):
        return(blast_fields[1])
    else:
        return(False)


def loadKeggPathways():
    """Return dictionary of key=pathID, value=pathway name from http://rest.kegg.jp/list/pathway/ko

    Example: keggPathways["path:ko00564"] = "Glycerophospholipid metabolism"
    """
    keggPathways = {}
    result = requests.get('https://rest.kegg.jp/list/pathway/ko')
    for entry in result.iter_lines():
        if entry.decode(result.encoding):
            str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
            fields = str_entry.split("\t")
            keggPathways[fields[0]] = fields[1]
    return(keggPathways)


def getKeggGenes(uniprotID):
    """Return a list of KEGG organism:gene pairs for a provided UniProtID."""
    keggGenes = []
    result = requests.get(f'https://rest.kegg.jp/conv/genes/uniprot:{uniprotID}')
    for entry in result.iter_lines():
        if entry.decode(result.encoding):
            str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
            fields = str_entry.split("\t")
            keggGenes.append(fields[1])  # second field is the keggGene value
    return(keggGenes)


def getKeggOrthology(keggGenes):
    """function to return the
    KEGG Orthology ID (e.g., ko:K01108)
    for a provided KEGG ID (e.g., 'hsa:4534');
    model it on getKeggGenes() function"""
    keggOrthology = []
    result = requests.get(f'https://rest.kegg.jp/link/ko/{keggGenes}')
    for entity in result.iter_lines():
        if entity.decode(result.encoding):
            entity_str = entity.decode(result.encoding)
            lines = entity_str.split("\t")
            keggOrthology.append(lines[1])
    return(keggOrthology)


def getKeggPathIDs(keggOrthology):
    """function to return the KEGG Path
    IDs (e.g., path:ko01100, path:ko00562)
    for a provided KEGG Orthology ID
    (e.g., ko:K01108); model it on getKeggGenes()
    function"""

    keggPathIDs = []
    result = requests.get(f'https://rest.kegg.jp/link/pathway/{keggOrthology}')
    for entity in result.iter_lines():
        if entity.decode(result.encoding):
            entity_str = entity.decode(result.encoding)
            lines = entity_str.split("\t")
            keggPathIDs.append(lines[1])
    return(keggPathIDs)


def addKEGGPathways(blastFile, evalue, outputFile):
    """function to tie all the other
    functions together to accomplish the
    assignment prompt"""
    Pathways = loadKeggPathways()
    keggPathid = []
    outputFile = open(outputFile, "w")
    with open(blastFile, 'r') as blast_f:
        for line_strp in blast_f:
            line_strp = line_strp.strip()
            uniprotID = getUniProtFromBlast(line_strp, evalue)
            if uniprotID:
                # to get the KEGG gene IDs
                keggGenes = getKeggGenes(uniprotID)
                if keggGenes:
                    keggOrthology = getKeggOrthology(keggGenes[0])
                    if keggOrthology:
                        keggPathIDs = getKeggPathIDs(keggOrthology[0])
                        for id in keggPathIDs:
                            if not id.startswith("path:map"):
                                keggPathid.append(id)
                        if keggPathid:
                            for pathID in keggPathid:
                                f_line = line_strp + "\t" + keggOrthology[0] + "\t" + pathID + "\t" + keggPathways[pathID] + "\n"
                                outputFile.write(f_line)

    blast_f.close()
    outputFile.close()


if __name__ == "__main__":
    args = get_args()
    blastFile = args.infile
    evalue = args.evalue
    outputFile = args.outfile
    addKEGGPathways(blastFile, evalue, outputFile)

