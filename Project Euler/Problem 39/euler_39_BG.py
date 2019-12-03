#Project Euler Problem 34
#Solution : Brandon Greer
#Slow : 38 sec
import math

p_solutions = list()
for p in range(1,1001):
    p_solutions.append(list())
for a in range(1,500):
    for b in range(1,500):
        for c in range(1,500):
            if(a+b+c <= 999):
                if(a**2 + b**2 - c**2 == 0):
                    if((b,a,c) not in p_solutions[a+b+c]):
                        p_solutions[a+b+c].append((a,b,c))
p_max = 0
for p in range(0,len(p_solutions)):
    if len(p_solutions[p]) > len(p_solutions[p_max]):
        p_max = p
print(p_max)
