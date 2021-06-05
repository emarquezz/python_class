'''

##  Name:
        at_rich.py

##  Version: [0.0]

##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>

##  Created: [2021-06-05]

##  Description:
        Program checks whether sequence has characters that are not ATCG and
        prints them, otherwise, prints AT rich regions.

##  Usage:
        at_rich.py [-i --input]

##  Arguments:
        [-i --input] optional, insert sequence file in command line, if not
            given, asks user for sequence

##  Requirements:
        re, argparse

##  Input:
        txt file with DNA sequence only

## Output:
        prints AT rich regions or characters that are not ATCG

## GitHub
        https://github.com/CrisSotomayor/python_class/blob/master/src/at_rich.py

## Examples
        Insert DNA sequence: ATATATATCGATG
            Region (0, 7) is AT rich: ATATATAT
        Insert DNA sequence: ATATGnAT
            AmbiguousBaseError: ambiguous base found: n

'''

## Packages
import argparse
import re

## Arguments
# Create parser to read arguments from command line
parser = argparse.ArgumentParser(description="Optionally, insert input sequence "
                                "file. ")

# Add agruments: input
parser.add_argument("-i", "--input",
                    help="Input file",
                    required=False)

# Exception for characters that are not ATCG
class AmbiguousBaseError(Exception):
    pass

# Function to check whether sequence only has valid characters (ATCG)
def check_bases(dna):
    """First, checks whether dna has valid bases, then, checks whether invalid
    bases (not ATCG) are found, and prints them as AmbiguousBaseError. """
    # If read from file, it will contain newline character
    dna = dna.replace("\n", "")
    # First, find bases
    if not re.search(r"[ATCG]", dna):
        raise AmbiguousBaseError('No bases found!')
    # Second, find ambiguous bases (not ATCG)
    result = re.findall(r"[^ATGC]", dna)
    if result:
        bases = list(set(result)) # remove duplicates
        raise AmbiguousBaseError(f'Ambiguous bases found: {", ".join(bases)}')
    return

# Function to get AT rich regions, only executed if no AmbiguousBaseErrors found
def get_at_rich(dna):
    """Finds AT rich regions, defined as at least 5 As or Ts in a row. """
    if re.search(r"[AT]{5,}", dna):
        # if any matches, iter over them
        for m in re.finditer(r"[AT]{5,}", dna):
            seq = m.group()
            pos_start  = m.start()
            pos_end = m.end()
            print(f"Region ({pos_start}, {pos_end-1}) is AT rich: {seq}")
    else:
        print("No AT rich regions found. ")
    return

# Get arguments from command line
args = parser.parse_args()
try:
    file = open(args.input, "r")
    dna = file.read()
except TypeError:
    dna = input("Insert DNA sequence: ")
except IOError:
    dna = input("File not found, insert DNA sequence: ")
finally:
    try:
        check_bases(dna)
    except AmbiguousBaseError as error:
        print(f"Something went wrong: {error}")
    else:
        get_at_rich(dna)
