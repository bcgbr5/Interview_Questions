#Project Euler Problem 46
#Solution : Brandon Greer

import math
from primes_generator import primesfrom3to
primes_max = 10000


primes = set(primesfrom3to(primes_max))
primes.add(2)

odds_max = 10000
odds = set(range(1,odds_max,2)) - primes

sqaures_max = 1000
squares = list([n**2 for n in range(1,primes_max)])
# print(squares)

composites = set()

for square in squares:
    for prime in primes:
        composites.add(prime+2*square)
rule_breakers = odds - composites
rule_breakers.remove(1)
print(25 in composites)
print(min(rule_breakers))
