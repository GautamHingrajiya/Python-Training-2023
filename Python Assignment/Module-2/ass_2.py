# Write a Python program to get the Factorial number of given number.

num = int(input("Enter Number You Wnat to Find Factorial"))

factorial = 1

if num > 0:

    for i in range ( 1, num + 1):
        
        factorial = factorial * i
    
    print(factorial)

elif num < 0:

    print("factorial does not for negative numbers")

else:

    print("The factorial of 0 is 1")