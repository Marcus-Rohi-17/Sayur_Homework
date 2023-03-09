'''
Print the level of the password security and if the password is acceptable
Weak - only alphabets or only numbers or only special chars
Ok - at least one alphabet, one number and one special char
strong - at least three alphabets, two numbers and one special char
Very strong - same as strong, but at least 16 count

All passwords must be at least 8 chars long. You can use RegEx if you want.
'''
print('Password must be at least 8 chars long ')
#Get the input from the user
password = input('Enter your password: ')
#Initialize the variables to calculate the count of alphabets, numbers, special chars 
alphabet_count = 0
numbers_count = 0
special_chars_count = 0
alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
#get the count of alphabets, numbers & special chars 
for i in password:
    if(i in alphabets):
        alphabet_count = alphabet_count + 1
    if(i in digits):
        numbers_count = numbers_count + 1
    if(i == '@' or i=='$' or i=='_' or i=='#' or i=='&' or i=='!'):
        special_chars_count = special_chars_count + 1

#get the length of the password
length_of_the_password = alphabet_count+numbers_count+special_chars_count
#print('length',length_of_the_password)
#Check the complexity of the password
if(alphabet_count+numbers_count+special_chars_count < 8):
    print('All passwords must be at least 8 chars long, Please enter valid password, Your password length is: ',length_of_the_password)
elif(alphabet_count >= 3 and numbers_count >= 2 and special_chars_count >= 1 and length_of_the_password >= 16):
    print('Complexity of your password is very strong')
elif(alphabet_count >= 3 and numbers_count >= 2 and special_chars_count >= 1):
    print('Complexity of your password is Strong')
elif(alphabet_count >= 1 and numbers_count >= 1 and special_chars_count >= 1):
    print('Complexity of your password is ok')
else:
    print('Complexity of your password is weak')
