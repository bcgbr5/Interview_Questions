#The top down algorithm was too slow. So we're 
#going to try a more iterative bottom up approach

#Project Euler Problem 67
#Solution : Brandon Greer

def loadTriangle(filename):
    lines = list()
    with open(filename) as fp:
        for cnt, line in enumerate(fp):
                line = (line.rstrip()).split()
                lines.append([int(x) for x in line])
    return(lines)

#Let's reowrk our node class into sub triangles

triangle = loadTriangle('triangle.txt')
triangle.reverse()
secondtriangle = list()
for row in range(0,len(triangle)): 
    if row == 0:
        secondtriangle.append(triangle[row])
    else:
        new_row = list()
        for node in range(0,len(triangle[row])):
            value = triangle[row][node] + max(secondtriangle[row-1][node], secondtriangle[row-1][node+1])
            new_row.append(value)
        secondtriangle.append(new_row)
print(secondtriangle[len(secondtriangle)-1][0])

    



    


 