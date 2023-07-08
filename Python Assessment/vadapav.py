# food billing system

# we create 2 role here, manager and cusomer

role =  """
                    MENU
            
            PRESS 1 FOR MANAGER
            PRESS 2 FOR CUSTOMER

        """
# create Dictionary

products = {} # creating Blanck Dictionary
shopping_cart = {} # creating shopping Blanck Dictionary
status = True
while status:
        print(role)
        choice = int(input("Enter Your Choice : "))

        if choice == 1:
                specific = {} # Creating blanck dictionary for specific product values
                product_name = input("Enter Product Name : ")
                qty = int(input("Enter Qty : "))
                price = int(input("Enter Price : "))
                
                if product_name in products:
                        old_qty = products[product_name]['qty']
                        specific['qty'] = qty + old_qty
                        specific['price'] = price
                        # print(specific)
                else :
                        specific['qty'] = qty + old_qty
                        specific['price'] = price
                        # print(specific)
                products[product_name] = specific

                # print(products)
                next_choice = input("Do You Want to Continue ? Press y for Yes and Press n for No : ") 
                if next_choice == "y" :
                    status = True
                else :
                    status = False
        else:
            print("                  Welcome to Customer Panel                            ")
            print("          Menu            ")
            for k,v in products.items():
                print(f"{k}  Qty={v['qty']} Rs. {v['price']}")
                
            name = input("Enter Product Name : ")
            if name in products.keys():
                print("Yes, product is Available")
                qty = int(input("Enter Qty : "))
                total_price = products[name]['price'] * qty 
                price("total proce = ", total_price)           
                                               
