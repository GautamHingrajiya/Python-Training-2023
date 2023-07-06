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

for i in range(0,len(menu)):
    item_name = input("Eter Item Want to Oreder : ")
    item_qty =  int(input("Eter Item Want to Qty : "))
    if item_name in menu:
        bill_amt = item_qty * menu.get(item_name)
        print(bill_amt)
    else:
        print
    




# for i in range (1,len(quiz)+1):
#     print(f"Que. {i} {quiz[i]['Que']} ")
    
#     ans = input("Enter Your Ans : ").lower()
#     if quiz[i]['ans'] == ans:
#         score+=50
#         print("Right Answer")
#     else:
#         score-=20
#         print("wrong Answer")
# print(f"score = {score}")