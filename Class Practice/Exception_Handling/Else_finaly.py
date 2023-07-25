try : 
    num1 = int(input("Enter Num1 : "))
    num2 = int(input("Enter Num2 : "))
    ans = num1 / num2

except Exception as e :
    print(e)

else: 
    print(ans)
    
finally :
    print("THANK YOU FOR USING THIS APPLICATION")