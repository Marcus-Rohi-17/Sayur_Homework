'''
Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
of the pattern. 
Eg -  Message - "I Love India".
      Pattern - "*** **** ** **********     *****"
      Output  - "ILo veIn di aILoveIndi     aILov"

     Note how you replace each * in the pattern with the letter in the message, the space in the message doesn't
     matter, but the space(s) in the pattern matters.
'''


#Input Message and pattern
Message = "I Love India"
Pattern = "*** **** ** **********     *****"
#Remove all the space from the given string
edited_string = Message.replace(" ", "")
#Get length of the pattern
length_of_pattern = len(Pattern)
#Get the length of the edited string
length_of_message = len(edited_string)
#Initialize Count variable
count=0
#Initialize Empty string to store the text in the form of pattern
string = ''
#Get the Edited string in the form of pattern
for i in range(length_of_pattern):
    if(Pattern[i]=='*'):
        string = string + edited_string[count]
        count+=1
    if(Pattern[i] == ' '):
        string = string + ' '
    if(count == length_of_message):
        count = 0
#print the Output
print(string)
