# Write a Python program to count the occurrences of each word in a given sentence

name1= input("Enter any Sentence : ")
a=set(name1)
for i in a:
    print(i,":",name1.count(i))