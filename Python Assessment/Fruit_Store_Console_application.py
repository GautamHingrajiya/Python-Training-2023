WelcomeDisplay = """
                                WELCOME TO FRUIT MARKET

                                1)  MANAGER
                                
                                2)  CUSTOMER
"""
ManagerDisplay = """
                                WELCOME TO FRUIT MARKET

                                1)  Add Fruirt Stock
                                
                                2)  Viwe Stock

                                3)  Update Stock

"""

products = {}
status = True
while status :
    print(WelcomeDisplay)
    role = int(input("Select Your Role (1/2) :"))
    if role == 1:
        print(ManagerDisplay)
        m_role = int(input("Select Your Role (1/2) :"))
        if m_role == 1:
            pass
        elif m_role == 2:
            pass
        elif m_role == 3:
            pass
    elif role == 2:
        pass










    check = input("Do You Want to Continue(y/n) : ").upper()
    if check == "Y":
        status = True
    else : 
        status = False