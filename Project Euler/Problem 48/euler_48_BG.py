#Project Euler Problem 48
#Solution : Brandon Greer

import math

nums = [n**n for n in range(1,1001)]
num_sum = str(sum(nums))

print(num_sum[-10:])
