# Names Scores
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
scores = {}

score = 1
for letter in alphabet:
    scores[letter] = score
    score+=1

with open("0022_names.txt","r") as file:
    for line in file:
        names = line.replace("\"","").split(",")

names.sort()

def get_scores(name, index):
    score = 0
    for letter in name:
        score += scores[letter]

    return score * index

total_score = 0
for i in range(len(names)):
    total_score += get_scores(names[i], i + 1)

print(total_score)