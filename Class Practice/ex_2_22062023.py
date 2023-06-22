#  accept 5 number from user and check positive and negative number


for i in range(1,6):

    num = int(input("enter number"))
        
    if num >= 0:
            print("you enter positive number")
    else:
            print("you enter negative number")