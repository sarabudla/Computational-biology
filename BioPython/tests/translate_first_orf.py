#!/usr/bin/env python
"""TODO: Say what the code does

TODO: Elaborate on what the code does
"""

import argparse
# TODO import other libraries needed
from Bio import Seq
from Bio import SeqIO
import re


def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="TODO: say what the script does.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the FASTA file of sequences
    parser.add_argument('filename',  # variable to access this data later: args.filename
                        metavar='FASTA',  # shorthand to represent the input value
                        help='Provide name and path to FASTA file to process.',
                        # message to the user, it goes into the help menu
                        type=str)
    parser.add_argument('-p', '--pattern',  # access with args.pattern
                        help='Provide a regex pattern for filtering FASTA entries',
                        default='^\d{1}\D*$')  # default works for Drosophila chromosomes

    return (parser.parse_args())


def find_first_orf(rna):
    """Return first open-reading frame of RNA sequence as a Bio.Seq object.

    Must start with AUG
    Must end with UAA, UAG, or UGA
    Must have even multiple of 3 RNA bases between
    """
    try:
        # TODO update regex to find the ORF

        orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
    except AttributeError:  # if no match found, orf should be empty
        orf = ""

    return (Seq(orf))


def translate_first_orf(dna):
    """TODO: what it does
     takes a DNA sequence, transcribes it into RNA, finds the first ORF,
      translates said ORF into a protein, and returns that protein

    Assumes input sequences is a Bio.Seq object.
    """

    # TODO: transcribe the DNA, find the first ORF, translate said ORF

    rna = dna.transcribe()
    # print(rna)
    orf = re.search('AUG([AUGC]{3})+(UAA|UAG|UGA)', str(rna)).group()
    # print(orf)
    translated_orf = Seq.translate(orf)
    # print(translated_orf)
    return (translated_orf)


if __name__ == "__main__":
    # TODO: get command-line arguments

    args = get_args()

    # TODO: use SeqIO to get the records in the fasta file provided by the command-line input
    for filename in args.filename:
        for record in SeqIO.parse(args.filename, "fasta"):

            # TODO: if the FASTA record's ID matches the regex pattern,
            # then print out its record ID then a tab space then the translated first ORF

            if re.match("^\d{1}\D*$", record.id):
                # translate_first_orf(record.seq)
                print(record.id + "\t" + translate_first_orf(record.seq))
