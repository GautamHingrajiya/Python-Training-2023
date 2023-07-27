
num = int( input( "Enter Number till you want sum : "))
sum = 0
if num > 0 : 
    for i in range(1,num+1):
        sum = sum+i

else:
    print("Please Enter Positive Numbers")
    
print("sum of  1 to", num ,"Number is :", sum )