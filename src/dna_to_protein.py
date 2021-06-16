'''

##  Name:
        dna_to_protein.py

##  Version: [0.0]

##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>

##  Created: [2021-06-16]

##  Description:
        Program takes DNA sequence and outputs corresponding protein sequence.

##  Usage:
        dna_to_protein.py [-i --input]

##  Arguments:
        [-i --input] optional, insert sequence file in command line, if not
            given, asks user for sequence

##  Requirements:
        argparse

##  Input:
        txt file with DNA or RNA sequence only

## Output:
        prints protein sequence

## GitHub
        https://github.com/CrisSotomayor/python_class/blob/master/src/dna_to_protein.py

## Examples
        Insert DNA or RNA sequence: ATATATATCGATG
        Which reading frame would you like to translate?: [0/1/2] 0

        Protein sequence is:
                IYID


'''

## Packages
import argparse

## Arguments
# Create parser to read arguments from command line
parser = argparse.ArgumentParser(description="Optionally, insert input sequence "
                                "file. ")

# Add agruments: input
parser.add_argument("-i", "--input",
                    help="Input file",
                    required=False)

def dna_to_protein(seq, reading_frame):
    """Translate RNA to protein.

    Parameters:
        - seq (str): sequence
        - reading_frame (int): 0, 1, 2, where to start translating
    Returns:
        - protein (str): corresponding protein sequence
    """

    gencode = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
        'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
        'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
        'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
        'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
        'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
        'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
        'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
        'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
        'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    # start at correct reading frame
    seq = seq[reading_frame:]
    protein = ''
    while len(seq) >= 3:
        codon, seq = seq[0:3], seq[3:]
        aminoacid = gencode[codon]
        if aminoacid == '_': # if stop codon
            break
        else:
            protein += gencode[codon]
    return protein

# Get arguments from command line
args = parser.parse_args()

try:
    # First, try input file
    file = open(args.input, "r")
    dna = file.read()
except TypeError:
    # if not given, ask for sequence
    dna = input("Insert DNA or RNA sequence: ")
except IOError:
    # if file given but not found, ask for sequence
    dna = input("File not found, insert DNA or RNA sequence: ")
finally:
    dna = dna.upper()
    # dna_to_protein takes DNA, if U found, assume RNA and replace 
    if 'U' in dna:
        dna = dna.replace('U', 'T')
    reading_frame = int(input("Which reading frame would you like to "
                   "translate?: [0/1/2]"))
    protein = dna_to_protein(dna, reading_frame)
    print(f"Protein sequence is: \n{protein} \n")
