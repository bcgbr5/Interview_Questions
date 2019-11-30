#Project Euler Problem 49
#Solution : Brandon Greer

import math
from primes_generator import primesfrom3to
primes_max = 10000


def is_permu(sequence):
    first_num_string = list(str(sequence[0]))
    second_num_string = list(str(sequence[1]))
    third_num_string = list(str(sequence[2]))
    for char in second_num_string:
        if char in first_num_string:
            first_num_string.remove(char)
        else:
            return False
    
    first_num_string = list(str(sequence[0]))
    for char in third_num_string:
        if char in first_num_string:
            first_num_string.remove(char)
        else:
            return False
    return True

primes = set(primesfrom3to(primes_max))
for num in range(1,1488):
    primes.discard(num)

sequences = list()
for prime in primes:
    step_max = (10000 - prime)/2
    for step in range(1000,step_max):
        if prime+step in primes and prime+2*step in primes:
            sequences.append((prime, prime+step, prime+2*step))

permutations = list()
for sequence in sequences:
    if is_permu(sequence):
        permutations.append(sequence)

for permutation in permutations:
    print(str(permutation[0])+str(permutation[1])+str(permutation[2]))
