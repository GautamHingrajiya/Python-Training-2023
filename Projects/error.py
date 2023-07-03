import random
list1 = ["u_list","c_list"]
m_list = []
u_list = []
c_list = []
i=1
while i<=12:
    num = random.randint(1,100)

    if num not in m_list:
        m_list.append(num)
        i+=1
print("main list",m_list)


for a in m_list:
    z=random.choice(list1)
    if z== "u_list":
        if len(u_list) ==6:
            c_list.append(a)    
        else:
            u_list.append(a)
    else:
        if len(c_list) ==6:
            u_list.append(a)   
        else:
            c_list.append(a)
print("user list",u_list)
print("computer list",c_list)
for i in range(1,12):
    lucky_number = random.choice(m_list)
    m_list.remove(lucky_number)
    
    print("Lucky Number : ",lucky_number)
    if lucky_number in u_list:
        if len(u_list) ==0:
            print("USER WON !!!!") 
        else:
            u_list.remove(lucky_number)
        
    else:
        if len(c_list) ==0:
            print("COMPUTER WON !!!!") 
        else:
            c_list.remove(lucky_number)
    
    print("user list",u_list)
    print("computer list",c_list)