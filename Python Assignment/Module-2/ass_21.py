# Write a Python function to reverses a string if its length is a multiple of 4.

def revstr(str1):
    if len(str1) % 4 == 0:
        
        rstr = str1 [-1::-1]
        return rstr
    else :
        
        return str1
    

str1= input("Enter String : ")
print(revstr(str1))