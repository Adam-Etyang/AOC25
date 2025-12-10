def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def parse_rotation(rotation):
    return rotation[0], int(rotation[1:])

def part_one(data):
    position = 50
    count = 0
    for rotation in data:
        direction, distance = parse_rotation(rotation)
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        if position == 0:
            count += 1
    return count

def count_zeros(position, direction, distance):
    """Count how many times dial hits 0 during a rotation."""
    if direction == 'L':
        first_hit = position if position > 0 else 100
    else:
        first_hit = (100 - position) if position > 0 else 100
    
    if distance >= first_hit:
        return 1 + (distance - first_hit) // 100
    return 0

def part_two(data):
    position = 50
    count = 0
    for rotation in data:
        direction, distance = parse_rotation(rotation)
        count += count_zeros(position, direction, distance)
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
    return count

if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")
