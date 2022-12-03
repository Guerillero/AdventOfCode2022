import re

data = open("Data.txt")

doubles = []

for line in data:
    basket = []
    compartmentBreak = int(len(line) / 2)
    compartment1 = line[:compartmentBreak]
    compartment2 = line.strip()[-compartmentBreak:]
    for charater in compartment1:
        if compartment2.find(charater) > -1:
            if re.search('[a-z]', charater):
                basket.append( ord(charater) - 96)
            else:
                basket.append(ord(charater) - 38)
    print(basket)
    doubles.append(basket[0])

print(sum(doubles))
