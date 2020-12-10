import os

# Read and prep the input
input_file = os.path.join(os.path.dirname(__file__), '10-in.txt')
inp = [0]
with open(input_file, encoding='utf-8') as f:
    for line in f:
        inp.append(int(line))
inp.sort()
end = inp[-1]+3
inp.append(end)

# Part 1
def p1(inp):
    g1 = 0
    g3 = 0
    for i in range(len(inp)-1):
        if inp[i+1] - inp[i] == 1:
            g1 += 1
        elif inp[i+1] - inp[i] == 3:
            g3 += 1
        else:
            print(inp[i], inp[i+1])
    return g1*g3

print(p1(inp))

# Part 2
def get_mandatory_adapters():
    mandatories = []
    for i in inp:
        if i+1 not in inp and i+2 not in inp:
            mandatories.append(i)
    if 0 not in mandatories:
        mandatories.append(0)
    if end not in mandatories:
        mandatories.append(end)
    mandatories.sort()
    return mandatories

def get_paths(start, end, i):
    global counters
    if start == end:
        counters[i] += 1
        return
    else:
        for j in range(1,4):
            if start + j in inp:
                get_paths(start + j, end, i)
        return

inp = set(inp)
mandatories = get_mandatory_adapters()
counters = [0 for i in range(len(mandatories)-1)]
for i in range(len(mandatories)-1):
    get_paths(mandatories[i], mandatories[i+1], i)
all_paths = 1
for c in counters:
    all_paths *= c
print(all_paths)