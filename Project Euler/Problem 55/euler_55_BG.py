#Project Euler Problem 54
#Solution : Brandon Greer
import math

def is_palindrome(num):
    num_str = str(num)
    for i in range(0,len(num_str)/2):
        if(num_str[i]!=num_str[len(num_str)-i-1]):
            return False
    return True

def reverse_and_add(num):
    return num + int(str(num)[::-1])#String slicing may be one of my favorite little features

def is_lychrel(num):
    for i in range(0,50):
        num = reverse_and_add(num)
        if(is_palindrome(num)):
            return False
    return True

lychrels = list()
for num in range(1,10000):
    if is_lychrel(num):
        lychrels.append(num)
print(lychrels)
print(len(lychrels))







