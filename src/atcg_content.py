"""
##  Name:
        atcg_content.py
##  Version: [0.0]
##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>
##  Created: [2021-04-15]
##  Description:
        Given a DNA sequence, program prints number of each of the four bases.

##  Usage:
        atcg_content.py
##  Arguments:
        NA
##  Requirements:
        NA
##  Input:
        sequence (str): string with DNA sequence, consists of A, T, C, G
## Output:
        Prints how many of each base.
## GitHub:
        https://github.com/CrisSotomayor/python_class/blob/master/src/atcg_content.py

## Examples
        Input: 'AAGGATGTCGCGCGTTATTAGCTAA'
        Output:
            La secuencia contiene la siguiente cantidad de bases:
                A: 7
                T: 7
                C: 4
                G: 7
"""

sequence = input('Introduce la secuencia de DNA: ')
sequence = sequence.upper()  # all capital letters

print('La secuencia contiene la siguiente cantidad de bases:')

for base in ['A', 'T', 'C', 'G']:
    print(f'{base}: {sequence.count(base)}')