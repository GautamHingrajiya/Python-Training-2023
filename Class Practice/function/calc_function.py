# Calculator

Operations = """
press 1 for addition
press 2 for multiplication
press 3 for substraction
press 4 for division

"""

def sum():
    num1 = int(input("Enter Number 1 :"))
    num2 = int(input("Enter Number 2 :"))
    ans = num1 + num2
    print(ans)


def mul():
    num1 = int(input("Enter Number 1 :"))
    num2 = int(input("Enter Number 2 :"))
    ans = num1 * num2
    print(ans)

def sub():
    num1 = int(input("Enter Number 1 :"))
    num2 = int(input("Enter Number 2 :"))
    ans = num1 - num2
    print(ans)

def div():
    num1 = int(input("Enter Number 1 :"))
    num2 = int(input("Enter Number 2 :"))
    ans = num1 / num2
    print(ans)

status = True
while status:
    print(Operations)
    choice = int(input("Enter Your Choice : "))

    if choice == 1 :
        sum()
    elif choice == 2:
        mul()
    elif choice == 3:
        sub()
    elif choice == 4:
        div()
    
    check = input("Perform More Operations (y/n) : ").upper()

    if check == "Y" :
        status = True
    else :
        status = False