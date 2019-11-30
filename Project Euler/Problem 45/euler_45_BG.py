#Project Euler Problem 42
#Solution : Brandon Greer


triangle_num_count = 100000

triangle_nums = [n*(n+1)/2 for n in range(1, triangle_num_count)]

pentagonal_nums = [n*(3*n - 1)/2 for n in range(1,triangle_num_count)]
pentagonal_nums = set(pentagonal_nums)
hexagonal_nums = [n*(2*n -1) for n in range(1,triangle_num_count)]
hexagonal_nums = set(hexagonal_nums)

triple_nums = list()

for num in triangle_nums:
    if num in pentagonal_nums and num in hexagonal_nums:
        triple_nums.append(num)

print(max(triple_nums))

