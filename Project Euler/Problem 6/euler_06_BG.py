#Project Euler Problem 6
#Solution : Brandon Greer
import math
squared_sum = pow(sum(range(1,101)),2)
sum_of_squares = sum(map(lambda x: x ** 2, range(1,101)))
print (squared_sum - sum_of_squares)

