f = open("myfile_example2.txt", "a")

for i in range(1,3):
    name = input("Enter Name :")
    score = int(input("Enter Score : "))
    f.write("\n"+name)
    f.write("\t : \t"+str(score))


f.close()

f = open("myfile_example2.txt", "r")
print(f.read())

f.close()