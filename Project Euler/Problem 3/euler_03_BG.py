#Project Euler Problem 3
#Solution : Brandon Greer
import math 
import numpy

def primesfrom3to(n): #From https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1
target_num = 600851475143
max_possible_factor = math.sqrt(target_num)

possible_primes = primesfrom3to(max_possible_factor)

possible_primes = possible_primes[::-1]
largest_prime_factor = 0
i = 0
while largest_prime_factor == 0:
    if target_num % possible_primes[i] == 0:
        largest_prime_factor = possible_primes[i]
    i+=1
print(largest_prime_factor)



