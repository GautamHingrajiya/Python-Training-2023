from message_display import *
from items_module import *
import datetime

total_pasta_qty = 0
total_piza_qty = 0
pizza_total_amt = 0
pasta_total_amt = 0
daytotalbillamt = 0
softDrinks = 0
bruschetta = 0
chocco_brownies_ice_cream = 0
orderno = 0
ordersdetails = {}
details = {}
order = {}

print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     Welcome to Amazing Pizza and Pasta Pizzeria      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")   
Name = input("\nEnter Your Name : ").upper()
print("\n\t\t\t\t\t\t\t\tHello", Name)
print(current_offer)

status = True
while status:
    orderno += 1
    print(WelcomeDisplay)
    role = int(input("Select Your Roll : "))

    match role:

        case 1 :
            print(pizza_menu)
            pizza_size = int(input("Select Pizza Size by Number (1,2,3) : "))
            pizza_order_qty = int(input("Enter No. of Pizza Want to Order : ")) 

            if pizza_size == 1:
                size_value  = 10.99
                pizza_total_amt += fn_pizza(size_value,pizza_order_qty)
                total_piza_qty += pizza_order_qty
                item_size = "Small"
            elif pizza_size == 2: 
                size_value  = 20.99
                pizza_total_amt += fn_pizza(size_value,pizza_order_qty)
                total_piza_qty += pizza_order_qty
                item_size = "Medium"
            elif pizza_size == 3:
                size_value  = 29.99
                pizza_total_amt += fn_pizza(size_value,pizza_order_qty)
                total_piza_qty += pizza_order_qty
                item_size = "Large"
                    
            if total_piza_qty >=4 :
                print(get_pizza)
                softDrinks += 1

            input()  
            print("Pizza Qty : ",total_piza_qty)
            print("Pizza Amt : ",pizza_total_amt) 
            item_name = "pizza" 

            print(pasta_menu)
            pasta_size = int(input("Select Pasta Size by Number (1,2,3) : "))
            pasta_qty = int(input("Enter No. of Pasta Want to Order : ")) 

            if pasta_size == 1:
                pasta_size_value  = 9.5
                pasta_total_amt += fn_pasta(pasta_size_value,pasta_qty)
                total_pasta_qty += pasta_qty
                item_size = "Small" 
            elif pasta_size == 2: 
                pasta_size_value  = 17.00
                pasta_total_amt += fn_pasta(pasta_size_value,pasta_qty)
                total_pasta_qty += pasta_qty
                item_size = "Medium"
            elif pasta_size == 3:
                pasta_size_value  = 27.50
                pasta_total_amt += fn_pasta(pasta_size_value,pasta_qty)
                total_pasta_qty += pasta_qty
                item_size = "Large"

            if total_pasta_qty >= 4 :
                print(get_pasta)
                bruschetta +=2

            input()
            print("Pasta Qty : ",total_pasta_qty)
            print("Pasta Amt : ",pasta_total_amt) 
            item_name = "pasta" 

            input()
            BillAmt = pizza_total_amt + pasta_total_amt
            print("\t\t\t\t===============================  Your Bill Amt : ", BillAmt,"  ===============================")
            if total_piza_qty >=4 and total_pasta_qty >= 4:
                print(get_amaz)
                chocco_brownies_ice_cream += 2
            daytotalbillamt += BillAmt

        case 2:
            print("payment received from pizza :",pizza_total_amt)
            print("payment received from pasta :",pasta_total_amt)
            print("payment received today :",daytotalbillamt)
            print("Number of pizza and pasta sold :", total_piza_qty + total_pasta_qty)
            print("softDrinks : ",softDrinks)
            print("bruschetta : ",bruschetta)
            print("chocco brownies ice cream : ",chocco_brownies_ice_cream)

        case _:
            print("Enter Valid Input")

    status = fn_check()

date = datetime.datetime.now()
today = str(datetime.date.today())
a= today.replace("-","")
f = open(str(a)+".txt", "a")
f.write("Order No. : "+ str(orderno) +"\n")
f.write("Name : "+ Name  +"\n")
f.write("Pizza Qty : "+ str(total_piza_qty)+"\n")
f.write("Pizza Price : "+ str(pizza_total_amt) +"\n")
f.write("Pasta Qty : "+ str(total_pasta_qty) +"\n")
f.write("Pasta Price : "+ str(pasta_total_amt) +"\n")
f.write("Total Bill Value : "+ str(BillAmt) +"\n")

f.write("---------------------------------------------------------\n")
f.write(str(date))
f.close()

print("==x==x==x==x==x==x==x==x==x==  Bye Bye  ==x==x==x==x==x==x==x==x==x==")