'''

##  Name:
        [programName].py

##  Version: [#.#]

##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>

##  Created: [YYYY-MM-DD]

##  Description:


##  Usage:
        program_name [options list] arguments

##  Arguments:
        [name] description

##  Requirements:
        [libraries]

##  Input:
        [files]

## Output:
        [files]

## Examples
        [Example 1: describe the example, input and outputs]

'''

## Packages
import sys
import argparse

## Arguments
# Create parser to read arguments from command line
parser = argparse.ArgumentParser(description="Argument parser description. ")

# Add agruments: input, output
parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="Input file",
                    required=True)
parser.add_argument("-o", "--output",
                    help="Output file",
                    required=False)

## Function template
def function(argument1, argument2):
    """ Description of function.

    Parameters:
        argument1 (type): description of argument1
        argument2 (type): description of argument2

    Output:
        output1 (type): description of output1
    """
    return 

## 1. [ Describe the step 1 ]

## 2. [ Describe the step 2 ]
