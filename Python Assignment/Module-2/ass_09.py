# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1=int(input("Enter Number 1 :"))
num2=int(input("Enter Number 2 :"))
num3=int(input("Enter Number 3 :"))

if num1 == num2 or num1 == num3 or num2 == num3 :
    print("You Enter Two Same Number")
else:
    sum=num1+num2+num3

    print("Sum of given Three Integers : ", sum)