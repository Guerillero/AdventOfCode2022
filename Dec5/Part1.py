data = open("Stacks.txt")
stacks = []
top = ""

fin = open("Moves.txt")

def prettyPrint(lin):
    op = ""
    counter = 0
    for line in lin:
        counter += 1
        op += str(counter) + " "
        for ch in line:
            op += ch
        op += "\n"
    print(op)

# Read in stacks into 3D array
for line in data:
    stacks.append(line.split())

prettyPrint(stacks)

# move crates
for line in fin:
    move = line.split()
    counter = 0
    while counter < int(move[1]):
        counter += 1
        stacks[(int(move[5]) - 1)].append(stacks[(int(move[3]) - 1)].pop(-1) )

prettyPrint(stacks)

for row in stacks:
    top+= row.pop(-1)

print(top)
