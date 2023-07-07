#  Write a Python program to get the Fibonacci series of given range.

num = int(input("Enter Number You Wnat to Find Fibonacci Series Term : "))

num0=0
num1=1

if num <= 0:
    print("series is not available for negative numbers or zeroth position")
elif num <=1:
    print(num0)
else:   
    print(num0)
    print(num1)
    for i in range(2,num):
        num2=num0 + num1
        print(num2)
        num0 , num1 = num1, num2