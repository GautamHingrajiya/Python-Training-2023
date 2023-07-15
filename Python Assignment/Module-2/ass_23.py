# Write a Python function to insert a string in the middle of a string.


def middleadd (str1,str2):
    global middlepoint
    global str3
    middlepoint =  len(str1) / 2
    str3 = str1[:int(middlepoint)] + str2 + str1[int(middlepoint):]
    return str3

middlepoint = 0
str3 = 0

str1 = input("Enter String : ")
str2 = input("Enter Middel String : ")
print(middleadd(str1,str2))