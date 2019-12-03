#Project Euler Problem 30
#Solution : Brandon Greer

sum_numbers = 0
for number in range(2,1000000):
    number_total = 0
    for digit in str(number):
        number_total += int(digit)**5
    if number == number_total:
        sum_numbers += number

print(sum_numbers)