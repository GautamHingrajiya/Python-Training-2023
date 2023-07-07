# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

string1= input("Enter String : ")
print("Enterd String : ",string1)

str2 = string1.replace("not poor","good")
print(str2)