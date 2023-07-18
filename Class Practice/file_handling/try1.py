f = open("myexcel.xls","a")

add = input("Enter Name : ")

f.write("\n"+add)
f.close()

f = open("myexcel.xls", "r")
print(f.read())

f.close()