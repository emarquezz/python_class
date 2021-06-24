"""Change module:

Includes functions to change sequence type.

- dna_to_rna(seq): transcribe DNA sequence
- rna_to_protein(seq, reading_frame): translate RNA sequence

"""
import re

def dna_to_rna(seq):
    """Transcribe DNA sequence.

    Parameters:
        - seq (str): sequence
    Returns:
        - seq (str): corresponding RNA sequence
    """
    return seq.replace('T', 'U')

def rna_to_protein(seq, reading_frame):
    """Translate RNA to protein.

    Parameters:
        - seq (str): sequence
        - reading_frame (int): 0, 1, 2, where to start translating
    Returns:
        - protein (str): corresponding protein sequence
    """

    codon_table = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}
    # start at correct reading frame
    seq = seq[reading_frame:]
    protein = ''
    while len(seq) >= 3:
        codon, seq = seq[0:3], seq[3:]
        aminoacid = codon_table[codon]
        if aminoacid == '_': # if stop codon
            break
        else:
            protein += codon_table[codon]
    return protein
