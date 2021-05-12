"""
##  Name:
        amino_acid_percentage.py
##  Version: [0.0]
##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>
##  Created: [2021-05-08]
##  Description:
        Given protein sequence and list of amino acids, program calculates
        percentage of amino acids in list in the sequence.

##  Usage:
        python amino_acid_percentage.py
##  Arguments:
        NA
##  Requirements:
        NA
##  Input:
        sequence (str): string with protein sequence
        amino_acids (list): amino acids to include in percentage count. Default
                            is hydrophilic amino acids
## Output:
        Percentage of amino acids in list
## GitHub:
        https://github.com/CrisSotomayor/python_class/blob/master/src/amino_acid_percentage.py

## Examples
        Input: 'MSRSLLLRFLLFLLLLPPLP', ['M', 'L']
        Output:
            El porcentaje de M, L en la secuencia es 55%
"""

def get_aa_percentage(sequence, aa_list=['A','I','L','M','F','W','Y','V']):
    """ Calculates percentage of sequence made up of amino acids in aa list.
    If no list is given, default is hydrophilic amino acids.  """
    #  Right format
    sequence = sequence.upper()
    aa_list = [aa.upper() for aa in aa_list]
    aa_count = 0
    #  Add counts of all amino acids
    for aa in aa_list:
        aa_count += sequence.count(aa)
    #  Obtain percentage and round
    return round(100*aa_count/len(sequence), 2)

#  Check if function works correctly
assert get_aa_percentage('MSRSLLLRFLLFLLLLPPLP', ['M']) == 5
assert get_aa_percentage('MSRSLLLRFLLFLLLLPPLP', ['M', 'L']) == 55
assert get_aa_percentage('MSRSLLLRFLLFLLLLPPLP', ['F', 'S', 'L']) == 70
assert get_aa_percentage('MSRSLLLRFLLFLLLLPPLP') == 65

#  Get sequence from user
sequence = input("Introduce la secuencia de proteina: \n")
aa_list = input("Introduce los amino acidos para obtener el porcentaje, "
                "separados por un espacio. Para considerar los amino acidos "
                "hidrofobicos, deja la linea en blanco. \n")

#  If user inputs no amino acids, use default list
if not aa_list.replace(' ', ''):
    percentage = get_aa_percentage(sequence)
else:
    aa_list = aa_list.split(' ') #  turn input into list of individual aa
    percentage = get_aa_percentage(sequence, aa_list)

#  Fix aa_list format for printing
aa_list = [aa.upper() for aa in aa_list]

print(f"El porcentaje de {', '.join(aa_list)} en la secuencia es {percentage}%")
