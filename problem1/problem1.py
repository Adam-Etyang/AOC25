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

if __name__ == "__main__":
    codes : list = []
    for i in range (0,100):
        codes.append(i)


    instructions : list = []
    pos = len(codes)//2
    password = 0

    with open('input.txt', 'r') as file:
        for line in file:
            instructions.append(line.strip())

    for ins in instructions:
        dir_char = ins[0].upper() #direction of jump
        k = int(ins[1:]) #size of jump
        if k < 0:
            k = abs(k)
            dir_char = 'L' if dir_char == 'R' else 'R'

        k %= len(codes) # reduce large steps modulo n for circular movement

        if dir_char == "R":
            pos += k
        elif dir_char == "L":
            pos -= k 
        else:
            continue

        pos %= len(codes) # wrap-around
        
        if codes[pos] == 0:
            password += 1


    print (password)












