data = open("Data.txt").read()
lenth = len(data) + 1
answers = []

for i in range(15, lenth):
    chunk = data[i-15:i-1]
    counter = 0
    for char in chunk:
        counter += 1
        if chunk.count(char) > 1:
            break
        elif counter > 13:
            answers.append([i-1, chunk])

print(answers[0])
