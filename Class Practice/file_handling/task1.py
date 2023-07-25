import datetime
import os

welcome_display = """
                    
                    Welcome to Vaccination Camp  


"""
print(welcome_display)
name = input("Enter Name : ").upper()
email = input("Enter Email : ").lower()
age= int(input("Enter Age : "))
gender= input("Enter Gender : ").upper()
vaccinename= input("Enter Vaccine Name : ").upper()
doze = int(input("Enter Doze (1/2) : "))

date = datetime.datetime.now()
today = str(datetime.date.today())
a= today.replace("-","")

f = open(str(a)+".txt", "a")
f.write("name : "+ name +"\n")
f.write("Email : "+ email +"\n")
f.write("Age : "+ str(age)+"\n")
f.write("Gender : "+ gender+"\n")
f.write("Vaccine Name : "+ vaccinename+"\n")
f.write("Doze : "+ str(doze)+"\n")
f.write("---------------------------------------------------------\n")
f.write(str(date))
f.close()