#Project Euler Problem 71
#Solution : Brandon Greer

import math
import fractions

d_max = 10**6
target_fraction = fractions.Fraction(3,7)
closest_fraction = 0
for d in range(12,d_max+1): # I know from testing that a fraction at 12 exists that closer than the given 2/5, this whole method does 
                            #produce erroneos results for extremly small D values due to rounding, these become irrelevant for the size of d we're working with
    n = int(math.floor(d*closest_fraction))#we're only intersted in fraction that fall between our current closest fraction and below our target fraction
    while fractions.Fraction(n,d) < target_fraction:
        if fractions.gcd(n,d)==1 and fractions.Fraction(n,d) > closest_fraction:
            closest_fraction = fractions.Fraction(n,d)
        n+=1
        

print(closest_fraction)