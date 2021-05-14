"""
##  Name:
        drosophila.py
##  Version: [0.0]
##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>
##  Created: [2021-05-13]
##  Description:
        Given data file, prints genes according to specific conditions.

##  Usage:
        python drosophila.py
##  Arguments:
        NA
##  Requirements:
        NA
##  Input:
        Data file
## Output:
        Genes matching conditions
## GitHub:
        https://github.com/CrisSotomayor/python_class/blob/master/src/drosophila.py

"""
data_file = open('../data/6-data.csv')
lines = data_file.readlines()
data_file.close()

# Fix format, remove \n. Split into items separated by ','
lines = [line[:-1] for line in lines]
lines = [line.split(',') for line in lines]

# Each line has organism, sequence, gene name, expression level

def get_at_content(sequence):
    """Return content of AT in sequence, as float between 0 and 1, inclusive. """
    sequence = sequence.upper()
    a_content = sequence.count('A')
    t_content = sequence.count('T')
    return round((a_content+t_content)/len(sequence), 2)

get_at_content("TA")

# First condition
print("Los genes que pertenecen a Drosophila melanogaster o Drosophila "
      "simulans son: \n")
for line in lines:
    # organism is first item
    if line[0] in ['Drosophila melanogaster',  'Drosophila simulans']:
        print(line[2], '\n') # gene name is third item

# Second condition
print("Los genes que tienen longitud entre 90 y 110 bases son: \n")
for line in lines:
    # sequence is second item
    if len(line[1]) >= 90 and len(line[1]) <= 110:
        print(line[2], '\n') # gene name is third item

# Third condition
print("Los genes con contenido de AT menor a 0.5 y expresion mayor a 200 son: \n")
for line in lines:
    # sequence is second item
    at_content = get_at_content(line[1])
    # expression is fourth item
    if at_content < 0.5 and int(line[3]) > 200:
        print(line[2], '\n') # gene name is third item

# Fourth condition
print("Los genes cuyo nombre empieza con 'k' o 'h' y no pertenecen a "
      "Drosophila melanogaster son: \n")
for line in lines:
    # name is third item, keep first letter
    first_letter = line[2][0]
    if first_letter in ['k', 'h'] and line[0] != 'Drosophila melanogaster':
        print(line[2], '\n') # gene name is third item

# Fifth condition
print("Los genes y su nivel de contenido de AT son: \n")
for line in lines:
    # sequence is second item
    at_content = get_at_content(line[1])
    # name is third item
    if at_content < 0.45:
        print(f'{line[2]} tiene contenido de AT bajo')
    elif at_content < 0.65: # content is >= 0.45 because of previous statement
        print(f'{line[2]} tiene contenido de AT medio')
    else:
        print(f'{line[2]} tiene contenido de AT alto')
