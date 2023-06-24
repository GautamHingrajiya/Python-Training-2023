for i in range(1,6):
    name= input("enter your name : ")
    print(name)




# accept 5 subjects marks from user and calculate additon

sum = 0
for i in range(1,6):
    marks= int(input("enter marks : "))
    print( i,"entered ", marks)
    sum += marks
print("total : ", sum)


"""
sum=0                       # taking one variable for sum intialvalue = 0
for i in range(1,6):        #loop will execute between 1 to 5
    # int() : for casting convert input values into interger
    marks=int(input("enter marks : ")) #taking one variable marks and accept from user

        if marks>= 35:          #check pass ans fail condition
            sum+=marks    #store in to sum variable
        else:               #for fail condition
            print("you are fail")
print("total : ",sum)           #result 
"""

developers_list = ["Gautam", "Ravi", "Abhay","Harshal"]

for developer in developers_list:
    print("welcome", developer, "to tops technologies")

"""
dt:22-06-2023
1)  accept 5 number from user and check even odd numbe


for i in range(1,6):

    num = int(input("enter number"))
        
    if num % 2 == 0:
            print("you enter enven number")
    else:
            print("you enter odd number")
            

2)  accept 5 number from user and check positive and negative number


for i in range(1,6):

    num = int(input("enter number"))
        
    if num > 0:
            print("you enter positive number")
    else:
            print("you enter negative number")


3)  accep how many name user wants to add

    num1 = int(input("please enter how many name you want to enter"))

    for i in range(1,num1+1):
    input("enter name : ") 

"""