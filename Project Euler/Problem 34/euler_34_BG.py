#Project Euler Problem 34
#Solution : Brandon Greer
import math
max_num = math.factorial(9)*4#This is extremly arbitrary, but works

print(max_num)

def evaluate_digit_factorial(number):
    num_fact_total = 0
    for digit in str(number):
        num_fact_total += math.factorial(int(digit))
    if num_fact_total == number:
        return True

digit_factorials = list()
for num in range(3,max_num):
    if evaluate_digit_factorial(num):
        digit_factorials.append(num)
        print(num)
print(sum(digit_factorials))
