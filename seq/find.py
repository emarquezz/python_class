""" Find module:

Includes functions to search for motifs or regions.

- find_motif(seq, motif): finds exact match for motif
- find_rich(seq, bases, length): finds region rich for specific bases and length
- find_orfs(seq): finds open reading frames of sequence

"""
import re
from change import rna_to_protein

def find_motif(seq, motif):
    """Find all exact matches of motif in sequence.

    Parameters:
        - seq (str): sequence
        - motif (str): subsequence to find in sequence
    Returns:
        None, prints matches.
    """
    if re.search(motif, seq):
        # if any matches, iter over them to print all
        for m in re.finditer(motif, seq):
            m_found = m.group()
            pos_start  = m.start()
            pos_end = m.end()
            print(f"Match for {m_found} found at ({pos_start}, {pos_end-1}). \n")
    else:
        print("No matches found. ")
    return

def find_rich(seq, bases, length):
    """Finds regions rich in bases, defined as at least length bases in a row.

    Parameters:
        - seq (str): sequence to search
        - bases (str): letters making up rich region
        - length (int): minimum number of letters defining rich region
    Returns:
        - None, prints regions
    """

    # format expression to search for
    regex = "[" + bases + "]{" + str(length) + ",}"
    if re.search(regex, seq):
        # if any matches, iter over them
        for m in re.finditer(regex, seq):
            m_seq = m.group()
            pos_start  = m.start()
            pos_end = m.end()
            print(f"Region ({pos_start}, {pos_end-1}) is {bases} rich: {m_seq}")
    else:
        print(f"No {bases} rich regions found. ")
    return

def find_orfs(seq):
    """Finds all open reading frames of sequence, defined as a start and stop
    codon in same reading frame.

    Parameters:
        - seq (str): valid RNA sequence
    Returns:
        None, prints open reading frames
    """

    # Start codons are not necessarily orfs, keep track if any have been found
    orfs = False
    # First, find start codons
    if re.search("AUG", seq):
        # Iter over matches
        for m in re.finditer("AUG", seq):
            pos_start =  m.start()
            # iter over stop codons
            for n in re.finditer(r"(UAA|UAG|UGA)", seq):
                pos_stop = n.start()
                if pos_start%3 == pos_stop%3: # same reading frame
                    print(f"Open reading frame found at ({pos_start}, {pos_stop+2})")
                    print(f"Protein sequence is {rna_to_protein(seq[pos_start:pos_stop+3], 0)}")
                    orfs = True # at least one orf found
                    # exit loop after first stop in frame found
                    break

    if not orfs:
        print("No open reading frames found in sequence. ")

    return
