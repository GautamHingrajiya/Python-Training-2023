try : 
    num1 = int(input("Enter Num1 : "))
    num2 = int(input("Enter Num2 : "))
    ans = num1 / num2
    print(ans)
except ValueError:
    print("Int Value Required")
except ZeroDivisionError:
    print("can't be Divided by Zero")
