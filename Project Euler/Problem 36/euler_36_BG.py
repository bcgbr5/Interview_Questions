#Project Euler Problem 34
#Solution : Brandon Greer
import math


def is_palindrome(num):
    num_str = str(num)
    for i in range(0,len(num_str)/2):
        if(num_str[i]!=num_str[len(num_str)-i-1]):
            return False
    return True


def is_bin_palidrome(num):
    num_str = str(num)
    num_str = num_str[2:]
    for i in range(0,len(num_str)/2):
        if(num_str[i]!=num_str[len(num_str)-i-1]):
            return False
    return True

double_base_palindromes = list()
double_base_palindromes.append(1)
for num in range(2,1000000):
    if is_palindrome(num) and is_bin_palidrome(bin(num)):
        double_base_palindromes.append(num)
print(sum(double_base_palindromes))
