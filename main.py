# Обработка текста
import numpy as np
corpus = []
for line in open("Gone-with-the-Wind.txt", "r").read().split("\n"):
    for unit in line.split(" "):
        corpus.append(unit.lower())
# Составление словаря
bigram_counter = {}

for i in range(len(corpus) - 2):
    bigram = (corpus[i].lower(), corpus[i + 1].lower())
    if not (bigram in bigram_counter.keys()):
        bigram_counter[bigram] = {corpus[i + 2].lower(): 1}
    if bigram in bigram_counter.keys() and not (corpus[i + 2].lower() in bigram_counter[bigram].keys()):
        bigram_counter[bigram][corpus[i + 2].lower()] = 1
    if bigram in bigram_counter.keys() and (corpus[i + 2].lower() in bigram_counter[bigram].keys()):
        bigram_counter[bigram][corpus[i + 2].lower()] += 1
# функция, предлагающая новые слова по префиксу из 2-х слов
def word_suggest(input1, input2):
    input1 = input1.lower()
    input2 = input2.lower()
    bigram2 = (input1, input2)
    list_of_p = []
    number_of_words = 0
    for i in bigram_counter[bigram2]:
        number_of_words += int(bigram_counter[bigram2][i])
    for i in bigram_counter[bigram2]:
        list_of_p.append(bigram_counter[bigram2][i]/number_of_words)
    return(np.random.choice(list(bigram_counter[bigram2].keys()), 1, list_of_p))

# Общение с пользователем: получение изначального префикса, чтобы сгенерировать дальнейший текст
print("Please, enter the first word:")
a = str(input())
print("Please, enter the second word:")
b = str(input())
print("Enter the number of words you'd like to be generated:")
n = int(input())
final_answer = a + ' ' +b + ' '
for i in range(n):
    c = word_suggest(a, b)[0]
    final_answer = final_answer + c + ' '
    a = b
    b = str(c)
print(final_answer)
