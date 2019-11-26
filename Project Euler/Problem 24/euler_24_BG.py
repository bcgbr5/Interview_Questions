#Project Euler Problem 24
#Solution : Brandon Greer
import itertools
numbers = list(('0','1','2','3','4','5','6','7','8','9'))

permu = list()
for p in itertools.permutations(numbers):
    permu.append(p)
permu.sort()
permu_str = ""
for num in permu[999999]:
    permu_str += num
print(permu_str)