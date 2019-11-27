#Project Euler Problem 34
#Solution : Brandon Greer
import math

def evaluate_multiples(num):
    i = 1
    product_string = ""
    while len(product_string) < 9:
        product_string += str(num*i)
        i+=1
    if(len(product_string) == 9 and all(elem in product_string for elem in ('1','2','3','4','5','6','7','8','9'))):
        return int(product_string)
    return 0

product_strings = list()
for num in range(2,10000):
    product_string = evaluate_multiples(num)
    if(product_string != 0):
        product_strings.append(product_string)
print(max(product_strings))
