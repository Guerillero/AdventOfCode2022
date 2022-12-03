# I wanted to prove to myself that I could do this with real-time calculating rather than pre-doing the logic

result = {
    "rock": {"rock": 3, "paper": 6, "scissors": 0},
    "paper": {"rock": 0, "paper": 3, "scissors": 6},
    "scissors": {"rock": 6, "paper": 0, "scissors": 3}
    }

throw = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

elf = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

me = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

def translate (plan):
    return [elf[plan.strip().split()[0]], me[plan.strip().split()[1]]]

data = open("Data.txt")
score = 0

for line in data:
    game = translate(line)
    score += (result[game[0]][game[1]] + throw [game[1]])

print(score)
