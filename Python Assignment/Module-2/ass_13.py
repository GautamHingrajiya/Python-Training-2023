# Write a Python program to count the number of characters (character frequency) in a string

count = 0
name1= input("Enter any name : ")
a=set(name1)
for i in a:
    print(i,":",name1.count(i))
    count+=1
print("\nGiven Name lenght is",len(name1),"Character and Has",count,"Different Characters")