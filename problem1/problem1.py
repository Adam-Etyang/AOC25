"""
- figure out how to calculate where the pointer lands after a rotation.
Types of rotations : R and L
R -> +1
L -> -1

pointer starts at 50.
List runs from 0 - 99 
the list is circular.

- count number of 0s.
"""
from itertools import cycle

if __name__ == "__main__":
    codes : list = []
    for i in range (0,100):
        codes.append(i)


    instructions : list = []
    with open('input.txt', 'r') as file:
        for line in file:
            instructions.append(line.strip())







