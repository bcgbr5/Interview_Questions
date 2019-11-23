#Project Euler Problem 2
#Solution : Brandon Greer
first_num = 1
second_num = 2

even_fibs = list()
even_fibs.append(2)

while(first_num + second_num < 4000000):
    new_fib = first_num + second_num
    if(new_fib % 2 == 0):
        even_fibs.append(new_fib)
    first_num = second_num
    second_num =new_fib
print(sum(even_fibs))