#Project Euler Problem 25
#Solution : Brandon Greer
#Super slow. I'll come take a look at it if I think about it later
import math 
import numpy

def primesfrom3to(n): #From https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

def find_num_consective_primes(a,b,prime_list):
    n = 0
    while (n**2 + a*n + b) in prime_list:
        n+=1
    return n

prime_list = list(primesfrom3to(5000))
prime_list.append(2)
prime_max = 0
a_max = 0
b_max = 0

for a in range(-1000,1001):
    for b in range(-1000,1001):
        if b%2!=0:
            a_b_primes = find_num_consective_primes(a,b,prime_list)
            if a_b_primes > prime_max:
                prime_max = a_b_primes
                a_max = a
                b_max = b

print(a_max , b_max , a_max*b_max)