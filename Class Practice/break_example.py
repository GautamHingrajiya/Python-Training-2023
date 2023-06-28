"""
break : break is a statement which is used to execute at looping time

using of break we can break the statement

syntax : 

    for i in range(1,10)
        if condition:
            break

"""

for i in range(1,6):
    marks = int(input("Enter Marks : "))
    if marks >= 35 :
        print("Pass")
    else:
        break
print("Fail")