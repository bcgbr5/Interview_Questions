#Project Euler Problem 50
#Solution : Brandon Greer

import math
from primes_generator import primesfrom3to
primes_max = 1000000

primes = list(primesfrom3to(primes_max))
primes.append(2)
primes.sort()

primes_set = set(primes)#Used to lookup if a number is prime,
                        #the in() operator on lists is slow
consecutive_prime_sums = list()
prime_count = len(primes)
for index in range(0,prime_count):
    candidate = primes[index]
    i=1
    while index+i < prime_count and candidate < primes_max:
        candidate = candidate+primes[index+i]
        if candidate in primes_set:
            consecutive_prime_sums.append((i+1,candidate))
        i+=1

consecutive_prime_sums = sorted(consecutive_prime_sums, key = lambda x:x[0])
print(consecutive_prime_sums[-1][-1])



