# Setup: Our system uses 4 and 5 number account numbers internally,
# however our older 'mainframe' system expects and will only function
# with 9 character strings. Create a function that can pad the account
# numbers correctly with leading 0s

def pad_acct_num(acct_num:str):#This was my initial attempt
    while len(acct_num) < 9:
        acct_num = '0'+acct_num
        print(acct_num)
    return acct_num

print(pad_acct_num("1234"))
#Interviewer Follow up 1 : What would your code do if it didn't recieve
#a stinrg or recieved a string of the wrong length?(I gather that some of
#these were generic and not specific to my code)
#Response : The length wouldn't matter, if it didn't recieve a string
#it would throw an exception. I would be more concerned about it recieveing
#a string with letters in it than something else.
#Followup 2 : Why would you want it to throw an exception and not just
#log the error to a file or something similar?
#Response : We want to make sure that someone is aware that there is a
#problem, I would much rather have the user see an unhandled error than
#have them think everything is fine when it's not. In other words
#we would rather it "fail loud" than "fail silently".
#Followup 3 : what if we wanted to return strings of another length
#or use a seperate padding character
def generalized_pad_acct_num(acct_num:str, padding_char = '0', expected_length=9):
    while len(acct_num) < expected_length:
        acct_num = padding_char+acct_num
        print(acct_num)
    return acct_num

print(generalized_pad_acct_num("4321",padding_char='_',expected_length=15))

#Interviewer Followup 4 : Can you do it in one line?

#The rest of these were essentially my answers in the interview, This
#one actualy stumped me so I came home and worked on it for a while.

def one_line_pad_acct_num(acct_num:str, padding_char = '0', expected_length=9):
    return (padding_char * (expected_length - len(acct_num)) + acct_num)
print(one_line_pad_acct_num("5678"))
