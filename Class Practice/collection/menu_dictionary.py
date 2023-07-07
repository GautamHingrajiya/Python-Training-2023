menu1 ="""
    mosambi juice       : 80
    orange juice        : 90
    watermelon juice    : 70
    pinapple juice      : 90
    apple juice         : 80
"""
menu = {
    "mosambi juice" : 80,
    "orange juice" : 90,
    "watermelon juice" : 70,
    "pinapple juice" : 90,
    "apple juice" : 80
}
print(menu1)
bill_amt = 0
total_bill=0
status = True
while status:
     
    item_name = input("Enter Item Want to Oreder : ").lower()
    item_qty =  int(input("Enter Item Want to Qty : "))

    if item_name in menu:
        bill_amt = item_qty * menu[item_name]
        print("bill_amt : ",bill_amt)
        total_bill +=bill_amt         
        order_more = input("Want to add More Item(y/n) : ").upper()
        if order_more == "Y" or order_more == "YES":
                continue
        else:
                status =False
                break  
    else:
        print("Enter Valid Name")    
print("TOTAL BILL AMT : ",total_bill)