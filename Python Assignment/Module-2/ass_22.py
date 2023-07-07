# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

mainStr = input("Enter String : ")
if len(mainStr) <2 :
    print(mainStr)
else : 
    subStr = mainStr[0] + mainStr[1] + mainStr[-2] + mainStr[-1]
    print(subStr)