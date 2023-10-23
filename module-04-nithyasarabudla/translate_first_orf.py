#!/usr/bin/env python
"""
Firstly, it takes an RNA sequence and returns the first complete ORF as a Seq object.
secondly, it takes a DNA sequence, transcribes it into RNA, finds the first ORF,
translates said ORF into a protein, and returns that protein.
At last, it takes user input, open FASTA files, decide which FASTA entries to process,
and print the results to the command line.


"""

import argparse
from Bio.Seq import Seq
from Bio import SeqIO
import re

def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="passing in the fasta file to be checked.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the FASTA file of sequences
    parser.add_argument('filename',  # variable to access this data later: args.filename
                        metavar='FASTA', # shorthand to represent the input value
                        help='Provide name and path to FASTA file to process.', # message to the user, it goes into the help menu
                        type=str)
    parser.add_argument('-p', '--pattern',  # access with args.pattern
                        help='Provide a regex pattern for filtering FASTA entries',
                        default='^\d{1}\D*$')  # default works for Drosophila chromosomes

    return(parser.parse_args())


def find_first_orf(rna):
    """Return first open-reading frame of RNA sequence as a Bio.Seq object.

    Must start with AUG
    Must end with UAA, UAG, or UGA
    Must have even multiple of 3 RNA bases between
    """
    try:
       orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)',str(rna)).group()
    except AttributeError:  # if no match found, orf should be empty
        orf = ""

    return (Seq(orf))


def translate_first_orf(dna):
    """
     takes a DNA sequence, transcribes it into RNA, finds the first ORF,
      translates said ORF into a protein, and returns that protein

    Assumes input sequences is a Bio.Seq object.
    """

    # transcribe the DNA, find the first ORF, translate said ORF
    dna=Seq(dna)
    rna = dna.transcribe()
    translated_orf = find_first_orf(rna).translate()

    return(translated_orf)


if __name__ == "__main__":
    # get command-line arguments
    args = get_args()

    # use SeqIO to get the records in the fasta file provided by the command-line input
    f_file= args.filename
    for record in SeqIO.parse(f_file, "fasta"):


    #  if the FASTA record's ID matches the regex pattern,
    # then print out its record ID then a tab space then the translated first ORF

        if re.match(args.pattern, record.id):
            print(record.id, ":", "\t" + translate_first_orf(record.seq))
