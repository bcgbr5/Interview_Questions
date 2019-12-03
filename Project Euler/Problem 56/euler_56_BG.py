#Project Euler Problem 56
#Solution : Brandon Greer
import math

def get_digit_sum(num):
    return sum([int(x) for x in str(num)])
    
digit_sums = set()
for a in range(1,100):
    for b in range(1,100):
        digit_sums.add(get_digit_sum(a**b))
print(max(digit_sums))







