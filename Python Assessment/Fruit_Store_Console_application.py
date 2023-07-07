Welcome_Display = """                           
                    WELCOME TO FRUIT MARKET

                        1) Manager
                        2) Customer

"""
print(Welcome_Display)                          # Printing Welcome Message 
Manager_Display = """
            WELCOME MANAGER 

            1) Add Fruit Stock
            2) Viwe Fruit Stock
            3) Update Fruit Stock
"""                                             # Manager Welcome and Role Selection Message

user_list= {                                    # Created User Collection
    1 : "Manager",
    2 : "Customer"
}
fruit={

}
                                           
role = int(input("Select your Role (1/2) : "))  # Taking User Role 
# print(f"\nYou are : {user_list.get(role)}\n")      # Printing User Selection  
if role == 1 :
    print(Manager_Display)
    m_role = int(input("Select Operation Want to Perform : "))
    if m_role == 1:
        status = True
        while status:
            fruit_name = input("Enter Fruit Name : ")
            fruit_name = {}
            fruit_qty = int(input("Enter Fruit Qty : ")) 
            fruit[fruit_name]["Qty"] = fruit_qty
            fruit_price = int(input("Enter Fruit Price : "))
            fruit[fruit_name]["price"] = fruit_price
                      
            
            
            
            # fruit_name[fruit_qty] = fruit_qty
            # fruit_name[fruit_price] = fruit_price 


                                
            add_more = input("Want to Add More Items (y/n) : ").upper()
            if add_more == "Y" or add_more == "YES":
                    continue
            else:
                    status =False
                    break    
        print(fruit)
       
    elif m_role == 2:
          print(fruit)
          
    elif m_role == 3:
          pass