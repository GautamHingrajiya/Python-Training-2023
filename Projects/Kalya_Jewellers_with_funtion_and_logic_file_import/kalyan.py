import logic_kalyan

status = True
while status:

    bill_amt=0
    discount = 0
    netbillvalue=0
    totalgoldrate=0
    purchase_amt=0
    currentgold_prise = 5752
    making_charge_per_gram = 845

    name = input("Enter Name : ").upper()
    gender = input("Enter Gender (M/F) : ").upper()
    age = int(input("enter your age : "))
    gram = int(input("enter gram you purchased : "))

    print("\n= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\n")

    a_purchase_amt = logic_kalyan.fn_pur_amt(currentgold_prise,gram )
    print("Total Purchase Amt : ",a_purchase_amt)

    a_total_making_charge = logic_kalyan.fn_making_charge(gram,making_charge_per_gram)
    print("Total Making Charges : ", a_total_making_charge )

    a_bill_amt = logic_kalyan.fn_bill_amt(a_purchase_amt , a_total_making_charge )
    print("ToTal Bill Amt ", a_bill_amt)
    input()
    
    print("\n= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\n")

    a_discount = logic_kalyan.fn_discount(gender,age,a_purchase_amt)
    print("Discount : ", a_discount,"%"," and discount amt :  ", a_discount*0.01* a_bill_amt)
    input()


    print("\n= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\n")
    print("Net Payable Amt : " , a_bill_amt-(a_discount*0.01* a_bill_amt))
    input()
    print("\n= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\n")
    
    print("Thank You for Visit ")

    check = input("Do you want to Continue(y/n) ?  :  ").upper()
    if check == 'Y' or check =="Yes":
        status= True
    elif check == "N" or check == "NO":
        status= False
    else:
        print("Enter Valid Input")