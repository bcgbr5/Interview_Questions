#Project Euler Problem 78
#Solution : Brandon Greer

max_num = 10**7

squared_digits = list([num**2 for num in range(0,10)])

class Chain:
    def sum_squared_digits(self,num):
        sum_digits = 0
        for digit in str(num):
            sum_digits+=squared_digits[int(digit)]
        return sum_digits
    def __init__(self,num,chains):
        self.num = num
        self.digits_squared = self.sum_squared_digits(num)
        chains[self.num]=self
        self.ends_in_eightynine = False
        if self.digits_squared == 1:
            self.ends_in_eightynine = False
        elif self.digits_squared == 89:
            self.ends_in_eightynine = True
        elif self.digits_squared in chains:
            self.ends_in_eightynine = chains[self.digits_squared].ends_in_eightynine
        else:
            self.ends_in_eightynine = Chain(self.digits_squared, chains).ends_in_eightynine

chains = dict()
for num in range(0,max_num):
    if num not in chains:
        chains[num]=Chain(num,chains)
    # print(num,chains[num].ends_in_eightynine,chains[num].digits_squared)
chains_that_end_in_eightynine = list()
for chain in chains.values():
    if chain.ends_in_eightynine:
        chains_that_end_in_eightynine.append(chain)
print(len(chains_that_end_in_eightynine))    
