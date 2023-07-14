def fn_pur_amt(currentgold_prise,gram ):
    
    purchase_amt = currentgold_prise * gram
    return purchase_amt

def fn_making_charge (grma , making_charge_per_gram):
    total_making_charge = grma * making_charge_per_gram
    return total_making_charge

def fn_bill_amt (a_purchase_amt , a_total_making_charge ):
    bill_amt = a_purchase_amt + a_total_making_charge
    return bill_amt
def fn_discount (gender,age,a_purchase_amt):
    
    global discount

    if gender == "M" or gender == "F":
        if gender == "M":
            if age >0 and age <65:
                if a_purchase_amt > 0 and a_purchase_amt <= 200000:
                    discount= 0
                elif a_purchase_amt > 200000 and a_purchase_amt <= 300000:
                    discount=10
                elif a_purchase_amt > 300000 and a_purchase_amt <= 500000:
                    discount=20
                else:
                    discount=25
            else:
                if a_purchase_amt > 0 and a_purchase_amt <= 200000:
                    discount= 0
                elif a_purchase_amt > 200000 and a_purchase_amt <= 300000:
                    discount=20
                elif a_purchase_amt > 300000 and a_purchase_amt <= 500000:
                    discount=30
                else:
                    discount=35
        else:
            if age >0 and age <65:
                if a_purchase_amt > 0 and a_purchase_amt <= 200000:
                    discount= 0
                elif a_purchase_amt > 200000 and a_purchase_amt <= 300000:
                    discount=15
                elif a_purchase_amt > 300000 and a_purchase_amt <= 500000:
                    discount=25
                else:
                    discount=30
            else:
                if a_purchase_amt > 0 and a_purchase_amt <= 200000:
                    discount= 0
                elif a_purchase_amt > 200000 and a_purchase_amt <= 300000:
                    discount=25
                elif a_purchase_amt > 300000 and a_purchase_amt <= 500000:
                    discount=35
                else:
                    discount=40
            
    else:
        print("enter valid gender")

    return discount