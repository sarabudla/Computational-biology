#!/usr/bin/env python
"""
It checks a particular sequence and outputs whether it is a nucleic acid,
an RNA sequence or an amino acid.

The code first parses commandline argument to take in the files and then reads the files. The code then converts
the contents of the files to a sequence and outputs the type of sequence in the file. To check the type of sequence,
I have first converted the sequence into a set of characters and checked it against the nucleotides expected in the
amino acid sequence and then rna sequence. If both of these are not true, then I return that it is a nucleic acid
sequence.
"""

import argparse


def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="pass in the file list for which the type of sequence is to be checked",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get a list of text files to process
    parser.add_argument('file_list',  # variable to access this data later: args.file_list
                        metavar='FILE',  # shorthand to represent the input value
                        help='Provide file name to process. For multiple files, separate their names with spaces.',
                        # message to the user, it goes into the help menu
                        type=str,
                        required=True,
                        nargs="+"  # will combine multiple textfile inputs into a list
                        )

    return (parser.parse_args())


def identify_sequence(sequence):
    # open a file and read its contents

    nucleic_acid_sequence = ["A", "T", "G", "C", "a", "t", "c", "g"]
    rna_sequence = ["A", "U", "G", "C", "a", "u", "c", "g"]
    nucleic = True

    # It divides the sequence into list
    sequence = set(list(sequence))

    # check if the nucleotide belongs to the sequence in nucleic acid
    for nucleotide in sequence:
        if nucleotide not in nucleic_acid_sequence:
            nucleic = False

    # after reading all line, if nucleic == True
    if nucleic == True:
        # retruns it is nucleic acid
        return "nucleic acid"

    rna = True
    # checks if the nucleotides belong to the rna sequence
    for nucleotide in sequence:
        if nucleotide not in rna_sequence:
            rna = False

    # after reading all lines, if rna == True
    if rna == True:
        # returns it is RNA sequence
        return "RNA sequence"
    # else it retruns amino acid
    return "amino acid"


if __name__ == "__main__":
    # get the arguments
    args = get_args()

    # loop through args.file_list to:
    for file in args.file_list:
        sequence = ''

        #    1) Open each file
        with open(file, 'r') as f:
            for line in f:
                sequence += line.strip()
        #    2) Identify the sequence within the file (hint: call your indentify_sequence() function)
        sequence_type = identify_sequence(sequence)

        #    3) Print the filename, and its identity to the Terminal (don't print the sequence itself)
        print('{} : {}'.format(file, sequence_type))
