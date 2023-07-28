# Write a Python program to read a file line by line and store it into a list
list1 = []
fname = open("NewFile.txt","r")
for line in fname:
    
    list1.append(line)

print(list1)