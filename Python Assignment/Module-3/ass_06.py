# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
str1 = input("Enter String : ")
if len(str1) >= 2 and  str1[0] == str1[-1] :
    print ("Length of String : ",len(str1))