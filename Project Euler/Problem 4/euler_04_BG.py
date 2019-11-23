#Project Euler Problem 3
#Solution : Brandon Greer

def get_palindrome():
    candidates = list()
    for i in range (500,999):
        #
        for j in range(500,999):
            #print(j)
            if check_palindrome(i*j):
                candidates.append(i*j)
    return  max(candidates)

def check_palindrome(number):
    pal_candidate = str(number)
    if(pal_candidate[0]==pal_candidate[-1] and pal_candidate[1]==pal_candidate[-2] and pal_candidate[2]==pal_candidate[-3]):
        return True
    else:
        return False
    
print(get_palindrome())