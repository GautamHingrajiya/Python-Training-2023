# Write a Python program to check whether a list contains a sub list

main_list = []
sub_list = []

n= int(input("Enter How Many Items want to add in Main_List :"))
for i in range(0,n):
    main_list.append(input("Enter Item Name :"))

print(main_list)
sub_list.append(input("Enter Item Name want to find in main list : "))
sub_list1=list(sub_list)
main_list1=str(main_list)

for i in main_list:

    if i in sub_list :
        print(sub_list, "is in main_list")
        break
    else:
        continue


print(sub_list, "is not in main_list")
    
    

# if sub_list1 not in  main_list1:
#     print("yes")
# else:
#     print("no")