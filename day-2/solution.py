def getinput(file):
    """
    get input for the problem
    """
    with open(file,"r") as file:
        return '\n'.join([i.strip() for i in file if i.strip()])

def parse_ranges(data):
    """
    Make tuple pairs of each of the ranges in the input
    """
    return [tuple(map(int, part.split('-'))) for part in data.split(',')]

def iter_nums(ranges):
    """
    iterate through each tuple pair generator
    """
    for start , end in ranges:
        for n in range(start, end+1):
            yield n 
            

if __name__ == "__main__":
    input = getinput("input.txt")
    data = parse_ranges(input)



    




