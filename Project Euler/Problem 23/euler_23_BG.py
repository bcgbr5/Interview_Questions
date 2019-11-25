#Project Euler Problem 23
#Solution : Brandon Greer

#This is a bit slow (a little over 3 minutes on my machine)
#but overall I'm actually pretty happy with it.
import itertools

def is_adbundant(input_num):
    sum = 0
    for i in range (1, input_num/2 +1):
        if input_num % i == 0 :
            sum +=  i
    if sum > input_num:
        return True
    else:
        return False


def find_adbundant_sums(abundant_num_list):
    N = 2
    abundant_sums = set()
    for s in itertools.product(abundant_num_list[::-1], repeat=N):
        abundant_sum = sum(s)
        if abundant_sum<28124:#since this is a set instead of a list,  we don't have to worry about duplicates
            abundant_sums.add(abundant_sum)
            print(abundant_sum)
    return abundant_sums

upper_limit = 28112 #We know 12 is the smallest abundant number and that 
abundant_num_list = list()

for num in range (0,upper_limit):
    if is_adbundant(num):
        abundant_num_list.append(num)
abundant_sums=find_adbundant_sums(abundant_num_list)
real_nums = range(1,28124)
print (sum(list(set(real_nums) - set(abundant_sums))))

        