s1= {"java", "python", "andriod", "php","node.js","andriod","java"}
print(s1)

# imp : remove duplicate values from list or find unique value from list

l1 = [10,20,30,40,20,50,30,60]
s= set(l1)  # convert in to set
print(s)

# imp : remove duplicate values from list or find unique value from list without using set

unique_list = []
l1 = [10,20,30,40,20,50,30,60]
for i in l1:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

