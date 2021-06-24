""" Verify module:

Includes functions to check that sequences input by user are correct.

- check_bases(sequence, type): check whether sequence only has valid characters
        according to sequence type


"""
import re

# Exception for characters that are not allowed
class AmbiguousBaseError(Exception):
    pass

# Function to check whether sequence only has valid characters
def check_bases(sequence, type):
    """First, checks whether invalid bases are found, depending on type,
    and raises AmbiguousBaseError if so.

    Parameters:
        - sequence (str): dna, rna or protein sequence to verify
        - type (str): 'dna', 'rna', 'protein', type of sequence

    Returns:
        - Error if sequence is not valid, None otherwise

    """
    # If read from file, it will contain newline character
    sequence = sequence.replace("\n", "")
    # Invalid characters depending on type
    invalid = {'dna':r"[^ATCG]", 'rna':r"[^AUCG]",
               'protein':r"[^GALMFWKQESPVICYHRNDT]"}

    # Find ambiguous bases (invalid characters)
    result = re.findall(invalid[type], sequence)

    if result:
        bases = list(set(result)) # remove duplicates
        raise AmbiguousBaseError(f'Characters not corresponding to {type} found: '
                                 f'{", ".join(bases)}')
    return
