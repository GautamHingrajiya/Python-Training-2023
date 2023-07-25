class checkodddata():
    pass

num = int(input("Enter Number : "))

try:
    if num % 2 == 0 :
        print("Even Number")
    else :
        raise checkodddata()
except : 
    print("Odd Number Entered ")
