#Project Euler Problem 68
#Solution : Brandon Greer

import math
import fractions

d_max = 10**6
fractions_list = list()
for d in range(2,d_max+1):
    for n in range(1,d):
        if  fractions.gcd(n,d) == 1:
            fractions_list.append(fractions.Fraction(n,d))

fractions_list.sort()
print(fractions_list[fractions_list.index(fractions.Fraction(3,7))-1])
print(len(fractions_list))
 