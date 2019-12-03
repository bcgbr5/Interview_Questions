#Project Euler Problem 51
#Solution : Brandon Greer
import math

def combinatorial(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

def find_combinatorials(num):
    combinatorials = list()
    for r in range(1,num):
        if combinatorial(num,r) > 10**6:
            combinatorials.append((num,r))
    return combinatorials

combinatorials = list()
for num in range(1,101):
    combinatorials +=find_combinatorials(num)
print(len(combinatorials))





