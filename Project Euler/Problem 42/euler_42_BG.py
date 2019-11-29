#Project Euler Problem 42
#Solution : Brandon Greer
import math

def load_words(filename):
    words = list()
    with open(filename) as fp:
        for cnt, line in enumerate(fp):
                line = (line.rstrip()).split(',')
                words.append([x for x in line])
    return(words)

score_list = list(('"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))

triangular_numbers  = list()

for num in range(1,10000):
    triangular_numbers.append(.5*num*(num+1))

trangle_words = list()
words = load_words("words.txt")[0]
print(words)

for word in words:
    word_score = 0
    for letter in word:
        word_score += score_list.index(letter)
    if word_score in triangular_numbers:
        trangle_words.append(word)

print(len(trangle_words))








