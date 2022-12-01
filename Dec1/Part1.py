data = open("Data.txt")

elf = []
largestCals = 0

for line in data:
    entry = line.strip()
    if entry:
        elf.append(line)
    else:
        cals = 0
        for entry in elf:
            cals += int(entry)
        if cals > largestCals:
            largestCals = cals
        elf = []

print(largestCals)
