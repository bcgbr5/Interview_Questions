#Project Euler Problem 12
#Solution : Brandon Greer
import math
def get_number_of_factors(number):
    factors = 0
    for i in range(1, int(math.sqrt(number))):
        if number % i == 0:
            factors += 2
    return factors

def get_triangular_number_with_n_factors(n):
    triangular_num = 1
    i = 2
    while get_number_of_factors(triangular_num) < n:
        triangular_num += i
        i+=1
    return triangular_num

print(get_triangular_number_with_n_factors(500))

