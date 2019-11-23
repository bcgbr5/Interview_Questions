#Project Euler Problem 10
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

primes = primesfrom3to(2000000)
print(primes[0])
print(primes[1])
print(primes[-1])
print(primes[-2])
print(sum(primes)+2)


