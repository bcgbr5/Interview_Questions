#Project Euler Problem 42
#Solution : Brandon Greer
import math

max_num = 100000
pentagonal_numbers = list()
for num in range(1,max_num):
    pentagonal_numbers.append(num*(3*num - 1) / 2)
pent_set = set(pentagonal_numbers)

def find_pair():
    for pent_1 in pentagonal_numbers:
        for pent_2 in pentagonal_numbers:
            if pent_1 != pent_2 and (pent_1 + pent_2) in pent_set and (pent_1 - pent_2) in pent_set:
                print(min(abs(pent_1 - pent_2), abs(pent_2-pent_1)))
                return(pent_1,pent_2)

print(find_pair())
