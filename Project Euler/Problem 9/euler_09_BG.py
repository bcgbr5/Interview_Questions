#Project Euler Problem 9
#Solution : Brandon Greer

def find_triple_product():
    for i in range (1,1000):
        for j in range (1,1000):
            for k in range (1,1000):
                if i + j + k == 1000:
                    if i**2 + j**2 == k**2:
                        return i*j*k



print(find_triple_product())