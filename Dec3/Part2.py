import re

data = open("Data.txt")

basket = []
elves = []
triples = []

for line in data:
    elves.append(line.strip())
    if len(elves) == 3:
        for charater in elves[2]:
            if elves[0].find(charater) > -1 and elves[1].find(charater) > -1:
                if re.search('[a-z]', charater):
                    basket.append(ord(charater) - 96)
                else:
                    basket.append(ord(charater) - 38)
        triples.append(basket[0])
        basket = [] # set back to empty state for next run
        elves = []

print(sum(triples))
