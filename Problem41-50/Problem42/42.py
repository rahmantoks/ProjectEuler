# Coded Triangle Numbers



with open("Problem41-50/Problem42/0042_words.txt","r") as file:
    content = file.read()
words = content.replace("\"","").split(",")

scores = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in alphabet:
    scores[letter] = alphabet.index(letter) + 1

def triangle(n):
    return int(n * (n + 1) / 2)

def wordscore(word):
    score = 0
    for letter in word:
        score += scores[letter]
    
    return score

triangle_nums = [0]
count = 0
for word in words:
    score = wordscore(word)
    max_index = len(triangle_nums)-1
    while triangle_nums[max_index] < score:
        max_index += 1
        triangle_nums.append(triangle(max_index))

    if score in triangle_nums:
        count+=1

print(count)
