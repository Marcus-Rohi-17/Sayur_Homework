'''
Same as above, but the pattern can be multi line.
Eg 
Message - "I Love India".
Pattern - 
'This is 
          a 
             Test'
Output  -
'ILov eI 
          n
             diaI'
'''
#Input Message and pattern
message = "I Love India"
pattern = 'This is \n\t a\n\t    Test'
#Split the pattern into 3 part based on '\n'
splitedPattern = pattern.split('\n')
#Remove all the space from the given string
messageWithoutSpace = message.replace(' ','')
#Initialize Empty string to store the text in the form of pattern
string = ''
#Initialize Count variable
messageIndex = 0

#Get the length of the edited string
length_of_message = len(messageWithoutSpace)-1
#Get the Edited string in the form of pattern
for i in splitedPattern:
    for j in i:
        if(j.isalpha()):
            string = string + messageWithoutSpace[messageIndex]
            messageIndex+=1
            if(messageIndex > length_of_message):
                messageIndex = 0
        else:
            string += j
    string += '\n'
#print the Output
print(string)