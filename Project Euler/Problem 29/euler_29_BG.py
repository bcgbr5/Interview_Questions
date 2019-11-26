#Project Euler Problem 29
#Solution : Brandon Greer

min = 2
max = 100

numbers = set()

for a in range(min, max+1):
    for b in range(min, max+1):
        numbers.add(a**b)
print(len(numbers))