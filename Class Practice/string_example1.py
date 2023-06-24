email = "gautam@gmail.com"
password = "123456"

u_email = input("Enter Email : ")
u_password = input("Enter Password : ")

if u_email != email or u_password != password:
    if u_email != email and u_password != password:
        print("Invalid Email and Password")
    elif u_email != email:
        print("Invalid Email")
    elif u_password!= password:
        print("Invalid Password")    
else:
    print("Valid Email and Password")