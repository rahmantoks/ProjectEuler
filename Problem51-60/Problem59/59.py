# XOR Decriptyon
from itertools import permutations

with open("Problem51-60/Problem59/0059_cipher.txt","r") as file:
    coded_msg_raw = file.read()

coded_msg = coded_msg_raw.split(",")
key_candidates = [[ord(i) for i in perm] for perm in permutations("abcdefghijklmnopqrstuvwxyz",3)]
most_common_words = set(["the", "that", "be", "to", "of", "and"])

def dechiper(key, msg):
    return ''.join([chr(key[i] ^ int(msg[i])) for i in range(len(key))])

for key in key_candidates:
    decoded = ""
    for i in range(0, len(coded_msg), 3):
        decoded += dechiper(key, coded_msg[i:i+3])
    
    if all(decoded.find(word) > 0 for word in most_common_words):
        print(key)
        print(decoded)
        print(sum([ord(letter) for letter in decoded]))
        break

