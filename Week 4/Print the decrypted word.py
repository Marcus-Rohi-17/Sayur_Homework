'''
Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special 
chars, all the chars between the number and special char are ignored.
 eg - ac2bd3 means acacbdbdbd. 
 ac2acc#cd3 acaccdcdcd
'''
#Get the encrypted text from the user
encrypted_text = input('Enter Your encrypted Text: ')
#Initialize the digits & special characters
digits="123456789"
special_characters = "!@#$%^&*()-+?_=,<>/"""
#Declare empty strings to store the alphabets
empty_string = ''
decrypted_string = ''
#Get decrypted text
for i in encrypted_text:
    if i in digits:
        digit = int(i)
        for i in range(digit):
            decrypted_string = decrypted_string + empty_string
        empty_string = ''
    elif(i in special_characters):
        empty_string=''
    elif(i.isalpha):
        empty_string+=i
    else:
        empty_string = ''
#print the decrypted text & it's length 
print('The length of the decrypted text is: ',len(decrypted_string))
print('The decrypted text is: ',decrypted_string)