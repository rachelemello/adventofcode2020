import os

# Read and prep the input
input_file = os.path.join(os.path.dirname(__file__), '5-in.txt')
inp = []
with open(input_file, encoding='utf-8') as f:
    for line in f:
        inp.append(line.strip())

# Part 1
def upper_half(pos_range):
    return [(1 + pos_range[0] + pos_range[1]) // 2, pos_range[1]]

def lower_half(pos_range):
    return [pos_range[0], (1 + pos_range[0] + pos_range[1]) // 2 - 1]

def get_seat(coordinates, row_range, col_range):
    if coordinates == '':
        return [row_range[0], col_range[1]]
    else:
        if coordinates[0] == 'B':
            row_range = upper_half(row_range)
        elif coordinates[0] == 'F':
            row_range = lower_half(row_range)   
        elif coordinates[0] == 'R':
            col_range = upper_half(col_range)
        elif coordinates[0] == 'L':
            col_range = lower_half(col_range)
        return get_seat(coordinates[1:], row_range, col_range)

def get_seat_id(seat):
    return seat[0] * 8 + seat[1]

def p1():
    max_id = 0
    for i in inp:
        max_id = max(max_id, get_seat_id(get_seat(i, [0,127], [0,7])))
    return max_id

print(p1())

# Part 2
def get_occupied_seats():
    occupied = [set(), set()]
    for i in inp:
        seat = get_seat(i, [0,127], [0,7])
        id = get_seat_id(seat)
        occupied[0].add((seat[0], seat[1]))
        occupied[1].add(id)
    return occupied

def find_my_seat_id(occupied):
    for row in range(128):
        for col in range(8):
            if (row, col) not in occupied[0]:
                id = get_seat_id((row, col))
                if (id-1) in occupied[1] and (id+1) in occupied[1]:
                    return id           

def p2():
    occupied = get_occupied_seats()
    return find_my_seat_id(occupied)

print(p2())
                