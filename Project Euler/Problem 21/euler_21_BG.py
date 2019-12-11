#Project Euler Problem 21
#Solution : Brandon Greer
import math
max_num = 10**4

def find_proper_divisors(num):
    proper_divisors = list([1])
    sqrt = math.sqrt(num)
    if sqrt.is_integer():
        proper_divisors.append(int(sqrt))
    for candidate in range(2,int(math.floor(sqrt)+1)):
        if num%candidate == 0:
            proper_divisors.append(candidate)
            proper_divisors.append(num/candidate)
    return(proper_divisors)

def d(n):
    return sum(find_proper_divisors(n))

amicable_nums = set()
for num in range(5,max_num):
    if d(num) < max_num and d(d(num))==num and num != d(num):
        amicable_nums.add(num)
        amicable_nums.add(d(num))

print(sum(amicable_nums))
