#Project Euler Problem 78
#Solution : Brandon Greer

import math
from project_euler_library import primesfrom3to
# max_num = 50
max_num = 5*10**7
max_prime = math.ceil(math.sqrt(max_num))



primes = list(primesfrom3to(max_prime))
primes.append(2)
primes.sort()

squares = [prime**2 for prime in primes]#we're making a list of each power
cubes = list()                          #becuase it saves a massive amount of 
fourths = list()                        #computation time later
i = 0
length = len(primes)
while primes[i]**3 < max_num:
    cubes.append(primes[i]**3)
    i+=1
i=0
while primes[i]**4 < max_num:
    fourths.append(primes[i]**4)
    i+=1 



prime_power_triples = set()

for square in squares:
    for cube in cubes:
        for fourth in fourths:
            candidate = square + cube + fourth
            if candidate < max_num:
                prime_power_triples.add(candidate)

print(len(prime_power_triples))




