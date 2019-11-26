#Project Euler Problem 21
#Solution : Brandon Greer
import math
def find_divisors(num):
        divsors = list()
        for candidate_divisor in range(1, int(math.sqrt(num))+1):
            if num % candidate_divisor == 0:
                divsors.append(candidate_divisor)
        return divsors

def find_divisors_sum(divisors):
    return sum(divisors)

def find_amicable_nums(numbers, this_num, amicables):
    print(this_num.number)
    for num in numbers:
        if num.divisor_sum == num.number and this_num.divisor_sum == num.number:
            amicables.append(this_num.number , num.number)
            print(amicables)

class divisor_sum:

    def __init__(self, number, numbers, amicables):
        self.number = number
        self.divisor_sum = find_divisors_sum(find_divisors(number))
        find_amicable_nums(numbers, self, amicables)


numbers = list()
amicables = list()
for i in range(1,300):
    divisor_sum(i, numbers, amicables)
print(sum(amicables))
    

        

