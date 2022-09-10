import numpy as np
corpus = []
for line in open("Gone-with-the-Wind.txt", "r").read().split("\n"):
    for unit in line.split(" "):
        corpus.append(unit.lower())

bigram_counter = {}
for i in range(len(corpus) - 2):
    bigram = (corpus[i].lower(), corpus[i + 1].lower())
    if bigram in bigram_counter.keys() and not (corpus[i + 2].lower() in bigram_counter[bigram]):
        bigram_counter[bigram].append(corpus[i + 2].lower())
    if not (bigram in bigram_counter.keys()):
        bigram_counter[bigram] = [corpus[i + 2].lower()]

def word_suggest(input1, input2):
    bigram2 = (input1.lower(), input2.lower())
    return(np.random.choice(bigram_counter[bigram2]))

print("Please, enter the first word:")
a = input()
print("Please, enter the second word:")
b = input()
print("Enter the number of words I'd like to be generated:")
n = int(input())
for i in range(n):
    c = word_suggest(a, b)
    print(c)
    a = b
    b = c
