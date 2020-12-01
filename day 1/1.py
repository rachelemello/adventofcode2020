import os

# Read and prep the input
input_file = os.path.join(os.path.dirname(__file__), '1-in.txt')
expenses = set()
with open(input_file, encoding='utf-8') as f:
    for line in f:
        expenses.add(int(line))

# Part 1
def p1():
    for exp in expenses:
        if 2020 - exp in expenses:
            return exp*(2020-exp)

print(p1())           

# Part 2
def p2():
    for exp1 in expenses:
        for exp2 in expenses:
            if exp1 != exp2 and (2020-exp1-exp2) in expenses:
                return exp1 * exp2 * (2020-exp1-exp2)

print(p2())