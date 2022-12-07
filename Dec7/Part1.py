import os
import re

data = open("Data.txt")

directories = {'/': 0}

def goIn (path, add):
    if path == "/":
        return str(path + add)
    else:
        return str(path + '/' + add)

def goOut (path):
    if re.search("^/\w+$", path):
        return "/"
    else:
        tokens = path.split('/')
        tokens.pop(-1)
        newPath = ''
        for part in tokens:
            if part:
                newPath += '/' + part
        return newPath

def toUpdate (path):
    holder = ''
    permutations = ['/']
    for part in path.split('/'):
        if part:
            holder += '/' + part
            permutations.append(holder)
    return permutations

currentDir = '/'

for f in data:
    line = f.strip()
    if re.search("dir \w+", line):
        directories[goIn(currentDir, line.split(" ")[1])] = 0
    elif re.search("\d+ \w+", line):
        up = toUpdate(currentDir)
        for level in up:
            directories[level] += int(line.split()[0])
    elif line == "$ cd ..":
        currentDir = goOut(currentDir)
    elif re.search("\$ cd \w+", line):
        currentDir = goIn(currentDir, line.split()[2])

total = 0
for key in directories.keys():
    if directories[key] <= 100000:
        total += directories[key]

print(total)
