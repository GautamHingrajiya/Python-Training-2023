Welcome_Display = """                           
                    WELCOME TO FRUIT MARKET

                        1) Manager
                        2) Customer

"""
Manager_Display = """
                    WELCOME MANAGER 

                    1) Add Fruit Stock
                    2) Viwe Fruit Stock
                    3) Update Fruit Stock
"""                                             # Manager Welcome and Role Selection Message

product = {}
shopping_product = {}
total_bill = 0

status = True                               
while status:
    print(Welcome_Display)                          # Printing Welcome Message 
    role = int(input("Select your Role (1/2) : "))          # Taking User Role 
    
    if role == 1 : # if select 1.manager role        
        
        print(Manager_Display)
        m_role = int(input("Select Operation Want to Perform : "))
        
        if m_role == 1:     # if select 1.Add Fruit Stock
            m_status = True
            while m_status:
                sub_dic = {}
                product_name = input("Enter product name : ")
                qty = int(input("Enter product qty : "))
                price = int(input("Enter product price : "))

                if product_name in product :
                    old_qty = product[product_name]['qty']
                    sub_dic['qty'] = qty + old_qty
                    sub_dic['price'] = price
                else:
                    sub_dic['qty'] = qty
                    sub_dic['price'] = price
                product[product_name]=sub_dic
                
                check = input("Do you want add more items ? (y/n) : ").upper()
                if check == "Y" or check == "YES":
                    m_status = True
                else:
                    m_status = False                   
                                
        elif m_role == 2:
                print("\n  ============  Current Stock  ============  \n")
                for k,v in product.items():
                    print(f"{k}   Qty= {v['qty']}  Rs. {v['price']} ")
        elif m_role == 3:
                
                u_status = True
                while u_status :
                    update_product_name = input("Enter Product Name")
                    update_product_qty = int(input("Enter update qty"))
                    update_product_price = int(input("Enter update price"))
                    
                    if product_name in product :
                        sub_dic['qty'] = update_product_qty
                        sub_dic['price'] = update_product_price
                    else:
                        print("Plese add First Item")

                    check = input("Do you want add more items ? (y/n) : ").upper()
                    if check == "Y" or check == "YES":
                        u_status = True
                    else:
                        u_status = False  
                    
    elif role ==2 :

        print("          Welcome Customer          ")
        c_status = True
        while c_status:

            print("  ============  MENU  ============  ")
            for k,v in product.items():
                print(f"{k}   Max Order Qty= {v['qty']}  Rs. {v['price']} ")
            
            
            product_name = input("Item Want to Oreder : ").lower()
            order_qty =  int(input("Enter Item Want to Qty : "))
            
            sub_shop={}
            shopping_product[product_name] = sub_shop

            if product_name in product:

                if order_qty <= product[product_name]['qty'] :
                    
                    bill_amt = order_qty * product[product_name]['price']
                    print("Item Total : ",bill_amt)
                    
                    total_bill += bill_amt
                    
                    product[product_name]['qty'] -= order_qty  
                    sub_shop['qty'] = order_qty
                    sub_shop['price'] = bill_amt
                    shopping_product[product_name]=sub_shop

                else :
                    print("You can't Order More then Max Order Qty")

            else:
                print("Enter Valid Item Name")
            
            check = input("Do you want add more items ? (y/n) : ").upper()
            if check == "Y" or check == "YES":
                c_status = True
            else:
                c_status = False  
                    
            print("\n  ============  Order Summery  ============  \n")
            for k,v in shopping_product.items():
                print(f"{k}   Qty= {v['qty']}  Rs. {v['price']} ")
            print("TOTAL BILL AMT : ",total_bill)
    else:
        print("Enter Valid Input")    
    
    check = input("Do you want to continue ? (y/n) : ").upper()
    if check == "Y" or check == "YES":
        status = True
    else:
        status =False