#Problem 67 Greedy Method
# Brandon Greer
#I wanted to try this as a greedy algorith to see 
#how far off it was

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
            if triangle[row+1][index+1] > triangle[row+1][index]:
                self.total = node(row+1, index+1, triangle).total + value
            else:
                self.total = node(row+1, index, triangle).total + value
            


triangle = loadTriangle('triangle.txt')
print(node(0,0,triangle).total)

#This is where this algorithm really shines.
#it finishes in .237 Seconds vs the other ones
#