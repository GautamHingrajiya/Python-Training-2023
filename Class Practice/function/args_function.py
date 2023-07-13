"""
args : arguments - function with arguments

tuple as parameter

"""


def myfun (*args) : 
    sum = 0
    for i in args:
        sum += i
    return sum

print(myfun(1,2,3,4,5,6,7))
print(sum)