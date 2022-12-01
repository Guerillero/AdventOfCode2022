data = open("Data.txt")
elves = []
elf = []

for line in data:
    entry = line.strip()
    if entry:
        elf.append(line)
    else:
        cals = 0
        for entry in elf:
            cals += int(entry)
        elves.append(cals)
        elf = []

elves.sort()


print(elves[-3] + elves[-2] + elves[-1] )
