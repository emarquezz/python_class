"""
##  Name:
        start_codon.py
##  Version: [0.0]
##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>
##  Created: [2021-04-09]
##  Description:
        Given a DNA sequence, program prints start codon ATG in sequence, and
        full coding sequence (start codon to codon before stop codon).

##  Usage:
        start_codon.py
##  Arguments:
        NA
##  Requirements:
        NA
##  Input:
        sequence (str): string with DNA sequence, consists of A, T, C, G
## Output:
        Prints site of start codon and sequence that gets transcribed (as RNA)

## Examples
        Input: 'AAGGATGTCGCGCGTTATTAGCTAA'
        Output:
            El codon ATG empieza en la posicion  4  y el marco de lectura termina en la posicion 24
            Fragmento de RNA que será transcrito
                AUGUCGCGCGUUAUUAGC
"""

sequence = input('Introduce la secuencia de DNA: ')
sequence = sequence.upper()  # all capital letters

start_position = sequence.find('ATG')
assert start_position != -1, 'La secuencia no tiene codon de inicio'

# Split by codons to search in same reading frame as start codon
codons = [sequence[i: i+3] for i in range(start_position, len(sequence), 3)]

# Search for each of the three codons, keep only first occurrence
stop_codon = -1
for i, codon in enumerate(codons):
    if codon in ['TAA', 'TAG', 'TGA']:
        stop_codon = i
        break

assert stop_codon != -1, 'No hay codon de paro en el mismo marco de lectura'

# stop_codon indicates number of codons, multiply by 3 to get position
stop_position = start_position + 3 * stop_codon
end_position = stop_position + 2

print(f'El codon ATG empieza en la posicion {start_position}  y '
      f'el marco de lectura termina en la posicion {end_position}')

transcribed_sequence = sequence[start_position:stop_position].replace('T', 'U')  # to RNA

print('Fragmento de RNA que sera transcrito\n', transcribed_sequence)
