sub1 = int(input("Enter Sub1 Marks : "))
sub2 = int(input("Enter Sub2 Marks : "))
sub3 = int(input("Enter Sub3 Marks : "))
sub4 = int(input("Enter Sub4 Marks : "))
sub5 = int(input("Enter Sub5 Marks : "))

TotalMarks = sub1+sub2+sub3+sub4+sub5
per= (100*TotalMarks)/ 500
print ("Total Marks : ", TotalMarks)
print ("Percentage : ", per)

if per >= 70:
    print("Distinction")
elif per >=60 and per <70:
    print("First Class")
elif per >=50 and per <60:
    print("Second Class")
elif per >=40 and per <50:
    print("Pass Class")
else :
    print("You are Faild ")