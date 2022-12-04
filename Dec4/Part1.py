data = open("Data.txt")

pair = []
contains = 0

for line in data:
    for elf in line.strip().split(","):
        pair.append( range(int(elf.split("-")[0]), int(elf.split("-")[1]) + 1, 1) ) # range() is not inclusive of the final number. Adding 1 to it to fix
    if pair[1][0] in pair[0] and pair[1][-1] in pair[0]: # If first and last are in range, the whole range is
        contains +=1
    elif pair[0][0] in pair[1] and pair[0][-1] in pair[1]:
        contains +=1
    pair = []

print(contains)
