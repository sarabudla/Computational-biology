#!user/bin/env python3
"""Test behavior of identify_sequence_refactored.py"""

# import the function to test (make sure you rename your script to "indentify_sequence_refactored.py")
from identify_sequence_refactored import identify_sequence


def test_dna_sequence():
    """Identify a DNA sequence"""
    assert identify_sequence("ATGATGA") == "nucleic acid", "expect ATGATGA identifies as nucleic acid"


def test_dna_lowercase_sequence():
    """Identify a DNA sequence in lowercase"""
    assert identify_sequence("atgatga") == "nucleic acid", "expect atgatga identifies as lowercase nucleicacid"



def test_rna_sequence():
    """Identify an RNA sequence"""
    assert identify_sequence("AUGAUGA") == "RNA sequence", "expect AUGAUGA identifies as RNA sequence "




def test_aminoacid_sequence():
    """Identify an amino acid sequence"""
    assert identify_sequence("MAPKKA") == "amino acid", "except MAPKKA identifies as amino acid sequence "




# Note: we expect this test to fail right now, but perhaps we can refactor the code again to make it pass in the future!
# For now, let's write the test to have that reminder.
def test_nonsequence():

    assert identify_sequence("ZZXy43") == "non sequence",  "This test case fails, provide the correct sequence "
