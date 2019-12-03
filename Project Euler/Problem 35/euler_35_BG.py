#Project Euler Problem 34
#Solution : Brandon Greer
#Slow: about 2 minutes
import math
from primes_generator import primesfrom3to
import itertools

def rotate_one(input):
    part_one = input[0:1] 
    part_two = input[1 :] 
    return part_two+part_one

def is_circular(prime, primes_list, circular_primes):
    rotations_are_prime = True
    prime_string = str(prime)
    prime_rotation_list = list()
    prime_rotation_list.append(int(prime_string))
    for i in range(0,len(prime_string)-1):
        prime_string = rotate_one(prime_string)
        prime_rotation_list.append(int(prime_string))
        if int(prime_string) not in primes_list:
            rotations_are_prime = False
    if rotations_are_prime:
        circular_primes+=prime_rotation_list

primes_max = 1000000
primes_list = primesfrom3to(primes_max)
circular_primes = list()
circular_primes.append(2)

for num in primes_list:
    is_circular(num, primes_list, circular_primes)

circular_primes.sort()
print(len(set(circular_primes)))


