'''

##  Name:
        start.py

##  Version: [0.0]

##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>

##  Created: [2021-06-10]

##  Description:
        File to run seq module. Gets sequence (DNA, RNA or protein) and gives
        user options to transcribe, translate, or search for specific regions.

##  Usage:
        python start.py [-t --type] [-s --sequence]

##  Arguments:
        [-t --type] type of sequence ('dna', 'rna', 'protein'). Optional.
        [-s --sequence] path to sequence file. Optional.
                If arguments not given, asks user for input

##  Requirements:
        re, argparse

##  Input:
        Sequence type and txt file with sequence or sequence input in command line.

## Output:
        Prints results according to user's questions

## Examples
        python start.py -t dna -s seq.txt (file contains AAATTT)

        What would you like to do? [1/2/3/4/5] 1




'''

## Packages
import argparse
import re
from verify import *
from change import *
from find import *


## Arguments
# Create parser to read arguments from command line
parser = argparse.ArgumentParser(description="If sequence to analyze is a file, "
                                "include type and sequence file path. ")

# Add agruments: type, sequence
parser.add_argument("-t", "--type",
                    help="Type of sequence [dna/rna/protein] ",
                    required=False)
parser.add_argument("-s", "--sequence",
                    help="Path to file with sequence ",
                    required=False)

# Get arguments
args = parser.parse_args()

# Type
# Ask if not given as argument, check valid type
if not args.type:
    type = input("Type of sequence [dna/rna/protein] : ")
else:
    type = args.type

while(type not in ['dna', 'rna', 'protein']):
    type = input("Enter a valid sequence type [dna/rna/protein]: ")

# Sequence
# Check if file is given and found, else ask for sequence. Then, validate sequence.
try:
    file = open(args.sequence, "r")
    seq = file.read()
except TypeError:
    seq = input("Insert sequence: ")
except IOError:
    seq = input("File not found, insert sequence: ")
finally:
    seq = seq.upper()
    check_bases(seq, type)

print(" This program has the following options: \n"
      " 1 Transcribe sequence [dna] \n"
      " 2 Translate sequence [rna] \n"
      " 3 Find motif in sequence [dna/rna/protein] \n"
      " 4 Find regions rich in specific bases or amino acids [dna/rna/protein] \n"
      " 5 Find open reading frames in sequence [rna] \n")


keep_going = 'y' # option to exit later
while(keep_going == 'y'):
    option = int(input("What would you like to do? [1/2/3/4/5]"))
    # Transcribe sequence
    if option == 1:
        if type != "dna": # Verify correct type
            print("This option is only valid for DNA sequences. \n")
        else:
            seq = dna_to_rna(seq)
            type = "rna"
            print(f"New sequence is: \n {seq} \n New type is RNA. \n")

    # Translate sequence
    if option == 2:
        if type != "rna": # Verify correct type
            print("This option is only valid for RNA sequences. \n")
        else:
            reading_frame = int(input("Which reading frame would you like to "
                           "translate?: [0/1/2]"))
            seq = rna_to_protein(seq, reading_frame)
            print(f"New sequence is: \n {seq} \nNew type is protein. \n")

    # Find motif in sequence
    if option == 3:
        motif = input("Enter motif to search for: ")
        find_motif(seq, motif)

    # Find rich region
    if option == 4:
        bases = input("Enter letters making up rich region: ")
        length = input("Enter minimum length for rich region: ")
        find_rich(seq, bases, length)

    # Find open reading frames
    if option == 5:
        if type != "rna": # Verify correct type
            print("This option is only valid for RNA sequences. \n")
        find_orfs(seq)

    keep_going = input("Would you like to try another option? [y/n]")
