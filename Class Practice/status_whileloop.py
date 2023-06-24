status=True
while status:
    num = int(input("Enter Number"))
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")
    
    check = input("Do you want to Continue ? Press Y for yes or N of no : ")
    if check == 'y' or check =="yes":
        status= True
    else:
        status= False