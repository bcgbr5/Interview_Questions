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

class sub_triangle:
    def __init__(self, row, index, left_child, right_child, triangle):
        value = triangle[row][index]
        self.row = row       
        self.index = index
        self.total = 0
        if(row%10 == 0 and row != 90):
            print(row)
        self.total = value + max(left_child.total + right_child.total)
    def __init__(self, row, index, triangle):
        self.row = row
        self.index =  index
        self.total = triangle[row][index]


triangle = loadTriangle('triangle.txt')
triangle_values = list()
for node in triangle[len(triangle) -2]:
    triangle_values.append(sub_triangle((len(triangle) -2),node,sub_triangle(len(triangle-1),node+1, triangle),sub_triangle(len(triangle-1),node, triangle), triangle))
#for i in len(triangle):

 