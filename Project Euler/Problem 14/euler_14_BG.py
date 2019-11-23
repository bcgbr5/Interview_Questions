#Project Euler Problem 14
#Solution : Brandon Greer
import sys
sys.setrecursionlimit(2000)
class Collatz:
    def __init__(self, identity, chains):
        self.identity = identity
        self.length = 0
        if identity == 1:
            self.length = 1
        elif identity % 2 == 0:
            next_identity = identity / 2
            if next_identity in chains:
                self.length = chains.get(next_identity).length + 1
            else:
                chains[next_identity] = Collatz(next_identity,chains)
                self.length = chains.get(next_identity).length + 1
        else:
            next_identity = (identity * 3) +1
            if next_identity in chains:
                self.length = chains.get(next_identity).length + 1
            else:
                chains[next_identity] = Collatz(next_identity,chains)
                self.length = chains.get(next_identity).length + 1


max_len = 0
max_num = 0
chains = {}
for i in range(1,1000000):
    if i not in chains:
        chains[i] = Collatz(i, chains)

    if  chains[i].length > max_len:
        max_len = chains[i].length
        max_num = chains[i].identity
print(max_num)

