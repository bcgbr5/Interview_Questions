#Project Euler Problem 42
#Solution : Brandon Greer
import itertools

perms = [''.join(p) for p in itertools.permutations('0123456789')]

sub_divisible_perms = list()

def assess_subdivisibility(num):
    if int(num[1:4])%2 != 0:
        return False
    elif int(num[2:5])%3 != 0:
        return False
    elif int(num[3:6])%5 != 0:
        return False
    elif int(num[4:7])%7 != 0:
        return False
    elif int(num[5:8])%11 != 0:
        return False
    elif int(num[6:9])%13 != 0:
        return False
    elif int(num[7:10])%17 != 0:
        return False
    return True

for perm in perms:
    if assess_subdivisibility(perm):
        sub_divisible_perms.append(perm)

sub_divisible_perms_sum = 0
for perm in sub_divisible_perms:
    sub_divisible_perms_sum+=int(perm)
print(sub_divisible_perms_sum)






