#Project Euler Problem 16
#Solution : Brandon Greer

def loadTriangle(filename):
    lines = list()
    with open(filename) as fp:
        for cnt, line in enumerate(fp):
                line = (line.rstrip()).split()
                lines.append([int(x) for x in line])
    return(lines)

class node:
    def __init__(self, row, index, triangle):
        value = triangle[row][index]
        self.row = row       
        self.index = index
        self.total = 0
        if row == len(triangle)-1:
            self.total = value
        else:
            rightTotal = node(row+1, index+1, triangle).total + value
            leftTotal = node(row+1, index, triangle).total + value
            self.total =  max(leftTotal, rightTotal)

triangle = loadTriangle('triangle.txt')
print(node(0,0,triangle).total)


