import os

# Read and prep the input
input_file = os.path.join(os.path.dirname(__file__), '3-in.txt')
inp = []
with open(input_file, encoding='utf-8') as f:
    for line in f:
        inp.append(line.strip())

# Part 1
def trees_in_slope(right, down):
    trees, col, row = 0, 0, 0
    map_width = len(inp[0])
    while row < len(inp):
        if inp[row][col%map_width] == '#':
            trees += 1
        col += right
        row += down
    return trees

print(trees_in_slope(3, 1))

# Part 2
def p2():
    res = 1
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    for slope in slopes:
        res *= trees_in_slope(slope[0], slope[1])
    return res

print(p2())
