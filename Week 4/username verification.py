'''
Check if the username and password is correct. 
Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
name of the company mentioned in the username, followed by any 3 numbers.
eg username : myname@sayur.com. password - mnamesay123 
'''
#Get the user name & password from the user
username = 'Rohith@gmail.com'#input('Enter user name: ')
password = 'rohith'#input('Enter password: ')
#Initialize digits and counter variable
digits="0123456789"


#Validate the username 
if '@' not in username:
    print('please Enter valid username with "{@}" symbol')
    quit()
if not(username.endswith('.com')) and not(username.endswith('.edu')) and not(username.endswith('.tech'))  and not(username.endswith('.org')):
    print('please Enter valid username with "{.com}" or "{.edu}" or "{.tech}" or "{.org}" ')
    quit()
#Get the count of alphabets before @ char
length_of_username = username.find('@')
if(length_of_username < 6):
    print("The user name must be at least 6 chars")
length_of_companyname = username.find('.')
length_of_companyname = (length_of_companyname - length_of_username)-1
if(length_of_companyname < 4):
    print("The Company name must be at least 4 chars")

#Get the first letter of user name
first_letter_of_username = username[0]

#Get Thired letter of user name
thired_letter_of_username = username[2]

#Get last three letters of user name
last_three_letters_of_username = slice(length_of_username-3,length_of_username)

#Get first three letters of company name
first_three_letters_of_company = slice(length_of_username+1,length_of_username+4) 

#concatenate all the strings
new_string = first_letter_of_username+thired_letter_of_username+username[last_three_letters_of_username]+username[first_three_letters_of_company]
print(new_string)
#Get the length of the password
length_of_password = len(password)
#Get the length of the new string
length_of_new_string = len(new_string)

#Validate the password alphabets
count_of_alphabets=0
for i in range(length_of_new_string):
    if(new_string[i] == password[i]):
        count_of_alphabets+=1
    else:
        break
        #print("Invalid password")

#Get the digits count of the password
digits_count = length_of_password - length_of_new_string
#Store the digits in new string
digits_in_password = password[-digits_count:]
#Validate the password digits
count_of_digits = 0
for i in digits_in_password:
    if i in digits:
        count_of_digits+=1
    else:
        #print("Invalid password")
        break
# #Print the give user name is valid or invalid
# if(c == 2):
#     print('Entered user name is valid')
# else:
#     print('Entered user name is invalid')
#Print the give password is valid or invalid
if(length_of_password == (count_of_alphabets+count_of_digits)):
    print('Entered password is valid')
else:
    print('Entered password is invalid')
