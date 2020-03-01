# Project Euler Problem 17
# Solution : Brandon Greer

import inflect


inf = inflect.engine()
def num_of_letters(num:int):
    return len([char for char in inf.number_to_words(num) if char not in [',','-',' ']])

def sum_of_english_numbers(low:int, high:int):
    return sum([num_of_letters(num) for num in range(low, high+1)])

print(sum_of_english_numbers(1,1000))
