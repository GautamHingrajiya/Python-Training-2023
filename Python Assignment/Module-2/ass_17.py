# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.


str1 = input("Enter String - 1 : ")
str2 = input("Enter String - 2 : ")

str3= str1+str2

print(str3.rfind("ing"))
print(str3.replace("ing","ly"))
