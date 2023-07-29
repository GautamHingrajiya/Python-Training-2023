# check triangle is equilateral isoscele and scalene

side1 = int(input("Enter Side 1 :"))
side2 = int(input("Enter Side 2 :"))
side3 = int(input("Enter Side 3 :"))

if side1 == side2 == side3 :
    print("equilateral ")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("isoscele")
else:
    print("scalene")