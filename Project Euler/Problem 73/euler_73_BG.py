#Project Euler Problem 73
#Solution : Brandon Greer
#Note, extroidinarily slow
import math
import fractions

d_max = 12*10**3
fractions_list = list()
for d in range(2,d_max+1):
    for n in range(1,d):
        if  fractions.gcd(n,d) == 1:
            fractions_list.append(fractions.Fraction(n,d))

fractions_list.sort()
min_index = fractions_list.index(fractions.Fraction(1,3))
max_index = fractions_list.index(fractions.Fraction(1,2))

print(max_index-min_index-1)