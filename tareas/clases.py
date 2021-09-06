'''

##  Name:
        clases.py

##  Version: [0.0]

##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>

##  Created: [2021-09-05]

##  Description:
        Classes to handle genomic sequences.

##  Usage:
        python clases.py

##  Arguments:

##  Requirements:
        re

'''
import re


class Secuencia():
    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.longitud = len(secuencia)
        return

    def imprimir(self):
        """Imprime la secuencia en mayusculas. """
        print(self.secuencia.upper())
        return

    def extender(self, nueva_secuencia):
        """Modifica la secuencia original, añadiendo la nueva secuencia al final. """
        self.secuencia += nueva_secuencia
        self.longitud = len(self.secuencia)
        return


class DNA(Secuencia):
    tipo = 'DNA'

    def imprimir(self):
        """Verifica bases de DNA, imprime secuencia en mayusculas o error. """
        result = re.findall(r"[^ATCG]", self.secuencia.upper())
        if result:
            print("La secuencia tiene caracteres que no corresponden al DNA. ")
        else:
            print(self.secuencia.upper())
        return


class RNA(Secuencia):
    tipo = 'RNA'

    def imprimir(self):
        """Verifica bases de RNA, imprime secuencia en mayusculas o error. """
        result = re.findall(r"[^AUCG]", self.secuencia.upper())
        if result:
            print("La secuencia tiene caracteres que no corresponden al RNA. ")
        else:
            print(self.secuencia.upper())
        return

###################################

# Ejemplo de uso

seq1 = 'ATCGATCGTTTAG'  # Secuencia de DNA
seq2 = 'AUCGAUCGGGAUC'  # Secuencia de RNA

# Clase secuencia maneja ambos tipos
s1 = Secuencia(seq1)
s1.imprimir()

s2 = Secuencia(seq2)
s2.imprimir()

s1.extender('AUC')
s1.imprimir()

# Clase dna maneja DNA, pero hereda funcion de extender
dna1 = DNA(seq1)
dna1.imprimir()

dna2 = DNA(seq2)
dna2.imprimir()

dna1.extender('ATG')
dna1.imprimir()

# Clase rna maneja RNA, igual hereda funcion de extender
rna1 = RNA(seq1)
rna1.imprimir()

rna2 = RNA(seq2)
rna2.imprimir()

rna2.extender('AUG')
rna2.imprimir()

# La funcion de imprimir es tanto un override, porque cambia en las subclases,
# como un polimorfismo, pues es diferente en las clases de dna y rna.
# Las clases se pueden utilizar para manejar secuencias genomicas y comprobar
# el tipo que estamos manejando. 
