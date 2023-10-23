#!/usr/bin/env python3
"""Interleave mate-pair fastq sequences into a single file fasta file and
 capturing the resulting output into a log file.
"""

import argparse  # for command-line argument parsing
from datetime import datetime  # for getting current timestamp
from Bio import SeqIO  # for reading/writing FASTQ/A files


def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Interleave mate-pair FASTQ sequences into a single FASTA file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('first_file',  # variable to access this data later: args.output
                        help='Provide the path/filename for the first input FASTA file.',
                        # shorthand to represent the input value
                        )

    parser.add_argument('second_file',  # variable to access this data later: args.output
                        help='Provide the path/filename for the second input FASTA file.',
                        # shorthand to represent the input value
                        )

    # Get output FASTA file name
    parser.add_argument('-o', '--output',  # variable to access this data later: args.output
                        metavar='FASTA',  # shorthand to represent the input value
                        help='Provide the path for the output FASTA file.',
                        # message to the user, it goes into the help menu
                        type=str,
                        required=True)

    # extra arguments to help us format our log file output
    parser.add_argument('--logFolder',  # variable to access this data later: args.logFolder
                        help='Provide the folder for log files.',  # message to the user, it goes into the help menu
                        type=str,
                        default="results/logs/")
    parser.add_argument('--logBase',  # variable to access this data later: args.logBase
                        help='Provide the base for the log file name',
                        type=str,
                        default=parser.prog)  # get the name of the script

    return parser.parse_args()


def pathLogFile(logFolder, logBase):
    """Return a log file path and name using the current time and script name."""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")  # get current time in YYYY-MM-DD-HHMM
    return f"{logFolder}{timestamp}_{logBase}.log"


def interleave(mate1, mate2):
    """Return list of interleaved SeqRecords.Assumes mate1 and mate2 inputs are SeqIO.parse iterator objects."""
    interleaved = []
    for left, right in zip(mate1, mate2):
        interleaved.append(left)
        interleaved.append(right)

    return interleaved


def logInterleave(args):
    """Create log of Interleave progress."""
    logFile = pathLogFile(args.logFolder, args.logBase)

    with open(logFile, 'w') as log:
        log.write(f"Running interleaved.py on {datetime.now()}\n")

        log.write("\n**** Summary of arguments ****")
        # TODO log the two mate files and the output file

        log.write("\n\n")  # add some space between argument data and the rest of the log
        log.write(f"Mate1 File: {args.first_file}\n")
        log.write(f"Mate2 File: {args.second_file}\n")
        log.write(f"Output File: {args.output}\n")
        log.write("\n\n")
        # TODO add log lines and commands to do the following steps. Unsure what/how to log?
        #  I've provided a sample
        #  of my log file in the results/logs/2022-10-13-1544_interleaved.py.log file in this repo

        #  1. Get the FASTQ sequences with SeqIO.parse
        left_reads = SeqIO.parse(f"{args.first_file}", "fastq")
        right_reads = SeqIO.parse(f"{args.second_file}", "fastq")
        log.write(f"Opening FASTQ mate-pair files: {args.first_file} and {args.second_file}\n")
        interleaved = interleave(left_reads, right_reads)
        log.write("Interleaving the two FASTQ files\n")

        #  2. Get the interleaved list of SeqRecord objects
        SeqIO.write(interleaved, f"{args.output}", "fasta")
        log.write(f"Writing interleaved data to: {args.output}\n")

        #  3. Write the interleaved list of SeqRecord objects to our FASTA file with SeqIO.write
        log.write(f"\nScript has finished at {datetime.now()}")


if __name__ == "__main__":
    logInterleave(get_args())  # pass arguments directly into the primary function
