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

def is_invalid(n: int) -> bool:
    s = str(n)
    mid = len(s)//2
    if len(s) %2 != 0:
        return False
    elif s[:mid] == s[mid:]:
        return True
    return False
            

if __name__ == "__main__":
    input = getinput("input.txt")
    data = parse_ranges(input)
    invalids = []

    for num in iter_nums(data):
        if is_invalid(num):
            invalids.append(num)

    print(sum(invalids))




    




