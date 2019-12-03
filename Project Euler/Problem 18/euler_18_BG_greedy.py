#I wanted to trty this as a greedy algorith to see 
#how far off it was
import os
import sys

def loadTriangle(filename):
    lines = list()
    with open(os.path.join(sys.path[0], filename)) as fp:
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

#On my machine that's about 1/3 the time, and I would
#imagine some of that's inevitable not bad for an
#under 1% loss (1074 vs 1064) 