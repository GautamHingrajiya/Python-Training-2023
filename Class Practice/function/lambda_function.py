"""

lambda function : function without any name is called lambda function

"""

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

ans = lambda num1,num2 : num1 * num2

print(ans(num1,num2))