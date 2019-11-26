#Project Euler Problem 22
#Solution : Brandon Greer
score_list = list(('"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))
print(score_list.index('Z'))

def load_names(filename):
    names = list()
    with open(filename) as fp:
        for cnt, line in enumerate(fp):
                line = (line.rstrip()).split(',')
                names.append([x for x in line])
    return(names)

names = load_names("names.txt")[0]
names.sort()
print(names)
names_score = 0
for name in names:
    letter_score=0
    for letter in name:
        letter_score += score_list.index(letter)
    names_score += letter_score * (names.index(name) + 1)
    print(names_score)