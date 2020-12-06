import os

# Read and prep the input
input_file = os.path.join(os.path.dirname(__file__), '6-in.txt')
file = open (input_file, 'r')
inp = file.read()
inp = inp.split('\n\n')
inp = [x.split('\n') for x in inp]

# Part 1
def get_unique_yes(group):
    all_group_answers = ''.join(group)
    return len(set(all_group_answers))

def p1():
    c = 0
    for group in inp:
        c += get_unique_yes(group)
    return c

print(p1())


# Part 2
def get_all_yes(group):
    all_yeses = []
    for g in group:
        all_yeses.append(set(g))
    if len(group) == 1:
        return len(all_yeses[0])
    return len(all_yeses[0].intersection(*all_yeses[1:]))

def p2():
    c = 0
    for group in inp:
        c += get_all_yes(group)
    return c

print(p2())