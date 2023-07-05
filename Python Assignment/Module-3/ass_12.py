# Write a Python program to convert a list of characters into a string.

list1=[]
str1=""
n= int(input("Enter How Many Items Want to add in List :"))

for i in range(0,n):
    list1.append(input("Enter Item Name :"))

print(list1) # print list which was creat by taking user input
print(type(list1))
print("\n ======================== \n")
for a in list1:
    str1=str1+a
print(str1, end="")
print(type(str1))
