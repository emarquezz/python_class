"""
##  Name:
        seq_to_fasta.py
##  Version: [0.0]
##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>
##  Created: [2021-04-30]
##  Description:
        Program reads file 4_dna_sequences.txt, creates dna_sequences.fasta file
        with sequences in first file with correct format.

##  Usage:
        seq_to_fasta.py
##  Arguments:
        NA
##  Requirements:
        NA
##  Input:
        txt file containing DNA sequences, one per line, with format
        <name> = <sequence>
## Output:
        Creates fasta file with format
        > <name>
        <sequence>
        for each sequence in original file.

## Examples
        Input: seq_1 = "ATCGATCG" (in txt file)
        Output:
        > seq_1
        ATCGATCG
        (in fasta file)

## GitHub:
        https://github.com/CrisSotomayor/python_class/tree/master/src/seq_to_fasta.py
"""
#  Open file with dna sequences
file = open('../../data/4_dna_sequences.txt')

#  Save all lines in a list
all_lines = file.readlines()

#  Write output file, blank file ending with .fasta
output = open('../output/dna_sequences.fasta', 'w')
for line in all_lines:
    #  Sequences split by ' = ' to separate name and sequence
    split_sequence = line.split(' = ')
    #  Take sequence and capitalize it
    dna_seq = split_sequence[1].upper()
    #  Remove all characters that are not DNA bases
    for char in dna_seq:
        if char not in 'ATCG':
            dna_seq = dna_seq.replace(char, '')
    #  Write lines in fasta, name then sequence in new line
    output.write(f'> {split_sequence[0]}\n{dna_seq}\n')

# Close both files used
file.close()
output.close()
