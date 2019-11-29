#Project Euler Problem 41
#Solution : Brandon Greer
import math
from primes_generator import primesfrom3to

primes_max = 1000000000
primes_list = list(primesfrom3to(primes_max))
primes_list.append(2)
primes_list = set(primes_list)

def is_pandigtal(num):
    num_str = str(num)
    digits = list(('1','2','3','4','5','6','7','8','9'))
    for digit in range(0,len(num_str)):
        if digits[digit]  not in num_str:
            return False
    return True


pandigital_primes = list()
for prime in primes_list:
    if is_pandigtal(prime):
        pandigital_primes.append(prime)
print(max(pandigital_primes))




