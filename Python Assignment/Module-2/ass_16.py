# Write a Python program to count the occurrences of each word in a given sentence

name1= input("Enter any Sentence : ")
list1= name1.split(" ")
a=set(list1)
for i in a:
    print("\nalphabate : ",i,", repeted :",name1.count(i),"times in Sentence")