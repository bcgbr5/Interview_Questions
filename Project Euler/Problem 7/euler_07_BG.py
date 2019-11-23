#Project Euler Problem 7
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

primes_list = primesfrom3to(200000)#wild shot in the dark on size


print(primes_list[9999])#we lose 1 to the lack of 2 and one to indexing

