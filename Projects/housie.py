import random
list1 = ["u_list","c_list"]
m_list = []
u_list = []
c_list = []
i=0
while i <=11:

    num = random.randint(1,100)
    
    if num not in m_list:
        m_list.append(num)
        i+=1
z=m_list
m_print = '    '.join(str(item) for item in m_list)
input("Press Enter For Start")
print("\n =================================================================================================\n")
print("RANDOM NUMBER :",m_print)

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
input()
print("\n =================================================================================================\n")
u_print = '    '.join(str(item) for item in u_list)
print("USER NUMBER : \t\t" ,u_print) 

input()
c_print = '    '.join(str(item) for item in c_list)
print("COMPUTER NUMBER : \t",c_print) 
print("\n =================================================================================================\n")

for i in range(1,12):
    magic_num =random.choice(m_list)
    print(magic_num)
    if magic_num in u_list:

        u_print.remove(magic_num)
        print(u_print)
        print(c_print)
    else :
        c_print.remove(magic_num)
        print(u_print)
        print(c_print)