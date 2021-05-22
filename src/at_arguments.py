"""
##  Name:
        at_arguments.py
##  Version: [0.0]
##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>
##  Created: [2021-05-22]
##  Description:
        Given file with sequences, program calculates AT percentage of each
        sequence and saves results in txt file.

##  Usage:
        python at_arguments.py -i path/to/input/file [-o path/to/output] [-r round]
##  Arguments:
        -i --input path/to/input/file
        -o --output path/to/output/file, optional
        -r --round number of digits to round results to, optional
##  Requirements:
        NA
##  Input:
        txt file with DNA sequences, one in each line

## Output:
        txt file with AT content of each sequence:

## GitHub:
        https://github.com/CrisSotomayor/python_class/blob/master/src/at_arguments.py

## Examples
        Input: file containing:
                    seq1 = "ATCGATCG"
                    seq2 = "ATATATAT"

        Output: file containing:
                    seq1 has 0.50 AT content
                    seq2 has 1.00 AT content
"""

import sys
import argparse

# Create parser to get arguments
parser = argparse.ArgumentParser(description="Script que calcula contenido de "
            "AT utilizando argumentos en linea de comando")

# Add agruments: input, output and round
parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="Archivo con secuencias de DNA",
                    required=True)
parser.add_argument("-o", "--output",
                    help="Archivo output para almacenar contenido de AT",
                    default="output_at_content.txt", required=False)
parser.add_argument("-r", "--round",
                    help="Cuantos decimales para redondear contenido",
                    default=2, required=False)

# Get arguments from command line
args = parser.parse_args()

# Function to calculate AT content
def get_at_content(dna, decimals=2):
    # Sequences with N are invalid
    if dna.count("N") > 0:
        raise ValueError(f'La secuencia contiene {dna.count("N")} Ns.')
    at_content = dna.count("A") + dna.count("T")
    return round(at_content/len(dna), decimals)

# Read input file
try:
    #  Open file with dna sequences
    file = open(args.input)
except  IOError:
    print("El archivo no existe, ingresa un archivo valido: ")
    file = input()
finally:
    # Save lines and close file
    all_lines = file.readlines()
    file.close()

names_seqs = [] # Store names and sequences

for line in all_lines:
    # Sequences split by ' = ' to separate name and sequence
    split_sequence = line.split(' = ')
    # Take sequence and capitalize it
    dna_seq = split_sequence[1].upper()
    # Remove all characters that are not DNA bases
    for char in dna_seq:
        if char not in 'ATCG' and char!='N':
            dna_seq = dna_seq.replace(char, '')
    # Save pairs with name and sequence in list
    names_seqs.append((split_sequence[0], dna_seq))

# Output file, if no output file is given, creates output_at_content.txt in same path
output = open(args.output, 'w')
dec = int(args.round)

# For each sequence, if seq is valid, add line to output
for name, sequence in names_seqs:
    try:
        output.write(f'{name} has AT content {get_at_content(sequence, dec)}\n')
    except ValueError as ex:
        print(f'Secuencia {name} invalida: {ex.args[0]}')
