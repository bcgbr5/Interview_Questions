#Project Euler Problem 1
#Solution : Brandon Greer
i = 3
multiples = list()
while i < 1000:
    multiples.append(i)
    i+=3
i = 5
while i < 1000:
    if(i not in multiples):
        multiples.append(i)
    i += 5
print(sum(multiples))