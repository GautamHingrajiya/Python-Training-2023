# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.


str1 = input("Enter String - 1 : ")                                         # getting str1 input
str2 = input("Enter String - 2 : ")                                         # getting str2 input

str3= str1 +" " + str2                                                      # getting single string from str1 and str2 sepereted by space
print(str3)                                                                 # printing single string from str1 and str2 sepereted by space

list1 = list(str1)                                                          # convert str1 into list1
list2 = list(str2)                                                                  # convert str2 into list2
list1[0], list1[1], list2[0], list2[1] = list2[0], list2[1], list1[0], list1[1]     # interchange 1st 2 charachter of both list
str3 = str(''.join(list1)) +" "+ str(''.join(list2))                                # joint and convert into string from list 
print(str3)                                                                         # print interchanged string