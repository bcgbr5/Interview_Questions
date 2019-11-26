#Project Euler Problem 25
#Solution : Brandon Greer
import math 

#5x5 grid produces 25 numbers, 
#therefore a 1001 x 1001 grid produces
grid_size = 1001
grid = range(1,(grid_size**2)+1)
grid_sum = 0
index = 0
count = 0
step = 2
while index < len(grid):
    grid_sum += grid[index]
    if count != 4:
        index += step
        count+=1
    else:
        count = 1
        step += 2
        index+=step
    

print(grid_sum)
