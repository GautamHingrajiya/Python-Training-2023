# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead 
# if the string length of the given string is less than 3, leave it unchanged.

str1 = input("Enter any String : ")

if len(str1) >= 3:                          # string length greatter then 3 then block is execute
        if str1.endswith("ing"):            # string end with ing than block is execute
            str1=str1.replace("ing","ly")   # replacing 'ly' instead of "ing" in string
        else:                               # string not end with ing and execute
            str1+= 'ing'                    # add ing in string

print(str1)