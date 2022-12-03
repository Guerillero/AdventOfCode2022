import re

data = open("Data.txt")

triples = []
count = 0

for line in data:
    count += 1
    basket = []
    if count == 1:
        elf1 = line.strip()
    elif count == 2:
        elf2 = line.strip()
    elif count == 3:
        count = 0
        for charater in line.strip():
            if elf1.find(charater) > -1:
                if elf2.find(charater) > -1:
                    if re.search('[a-z]', charater):
                        basket.append(ord(charater) - 96)
                    else:
                        basket.append(ord(charater) - 38)
        triples.append(basket[0])
        basket = []

print(sum(triples))
