#Project Euler Problem 5
#Solution : Brandon Greer

factors = list((18,17,16,15,14,13,12,11))
#10,5,4,and 2 are free Because of 20
#9, 6, 3 are in 18
#8 is in 16 and 7 is in 14

#Our value has to be a multiple of 20 and 19 since they
#share no factors, which also allows us to leave them 
#out of our list

def check_smalles_multiple(candidate):
    is_multiple = True
    for factor in factors:
        if candidate % factor != 0:
            is_multiple = False
    return is_multiple

multiple = 20 * 19
candidate_multiple = multiple
while not check_smalles_multiple(candidate_multiple):
    candidate_multiple += multiple
print(candidate_multiple)


