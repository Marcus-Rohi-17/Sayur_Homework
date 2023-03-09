''' 
Write the function mostFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated the same), returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions.
'''
def mostFrequentLetters(s):
    s = s.lower();
    s.replace(" ","")
    s = "".join(sorted(s))
    s = "".join(sorted(s, key=lambda x: s.count(x), reverse=True))

    s_unique = ""
    for i in s:
        if i not in s_unique:
            s_unique += i
    return s_unique

#Read input
# s = input('Enter the String: ')
s = "We Attack at Dawn"

#convert into Output
most_freq_str = mostFrequentLetters(s)
#print output
print(most_freq_str.replace(" ",""))