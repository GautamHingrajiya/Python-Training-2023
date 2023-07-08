# Write a Python program to check whether a list contains a sub list

main_list = []
sub_list = []

n= int(input("Enter How Many Items want to add in Main_List :"))
for i in range(0,n):
    main_list.append(input("Enter Item Name :"))

print(main_list)
sub_list.append(input("Enter Item Name want to find in main list : "))


for i in sub_list:

    if i in main_list :
        print(sub_list, "is in main_list")
        break
    else:
        print(sub_list, "is not in main_list")


    