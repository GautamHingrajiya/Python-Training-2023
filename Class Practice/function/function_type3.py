# function with parameter and function with return type

def checkEvenOdd(num):

    if num % 2 ==0 :
        return "Even Number"
    else : 
        return "Odd Number"


num = int(input("Enter Number : "))
print(checkEvenOdd(num))

# 2nd example

def sum(num1 , num2) :
    return num1 + num2

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
print("sum = ",sum(num1 , num2))