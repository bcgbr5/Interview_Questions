#Project Euler Problem 25
#Solution : Brandon Greer

fib1 = 1
fib2 = 1
fib_count = 2
while len(str(fib2)) < 1000:
    fib_count+=1
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3

print(fib_count)