data = open("Data.txt").read()
lenth = len(data) + 1
answers = []

for i in range(5, lenth):
    chunk = data[i-5:i-1]
    counter = 0
    for char in chunk:
        counter += 1
        if chunk.count(char) > 1:
            break
        elif counter > 3:
            answers.append([i-1, chunk])

print(answers[0])
