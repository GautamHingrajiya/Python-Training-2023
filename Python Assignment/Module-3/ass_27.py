# Write a Python program to find the repeated items of a tuple.

tuple1 = (10,20,30,30,40,50,60,20,80,40,50,90,10,20,30)
list_repet = []
list_repet_item = 0


for item in tuple1:
        
    if item in tuple1:
        list_repet_item += 1
        
        if list_repet_item == 2:
            list_repet.append(item)
    
    else:
        list_repet_item = 1
print(list_repet)
    
