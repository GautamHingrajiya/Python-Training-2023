purchaseamt = int(input("Enter Purchase Amt : "))
salesamt = int(input("Enter Sales Amt : "))


if purchaseamt > salesamt :
    print("you Got Loss Of Rs. :", purchaseamt-salesamt)
elif purchaseamt  < salesamt :
    print("you Got Profit Of Rs. :",salesamt - purchaseamt)
elif purchaseamt == salesamt:
    print("non Profit Sales")
else:
    print("Enter Valid Input")