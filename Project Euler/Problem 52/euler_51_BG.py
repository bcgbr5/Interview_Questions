#Project Euler Problem 51
#Solution : Brandon Greer


def convert_to_list(num):
    as_list = list(str(num))
    as_list.sort()
    return as_list

    
def find_lowest_int(num):
    num_as_list = convert_to_list(num)
    
    if num_as_list == convert_to_list(num*2):
        if num_as_list == convert_to_list(num*3):
            if num_as_list == convert_to_list(num*4):
                if num_as_list == convert_to_list(num*5):
                    if num_as_list == convert_to_list(num*6):
                        return True
    return False

for num in range(0,1300000):
    if find_lowest_int(num):
        print(num)





