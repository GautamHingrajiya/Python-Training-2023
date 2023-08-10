import pymysql
import connection

mydb = pymysql.connect(host="localhost",user="root",password="",database="15JUN_CRUD")
mycursor=mydb.cursor()

menu = """
                                  MENU

                            1) ADD STUDENT

                            2) VIWE STUDENTS

                            3) UPDATE DETAILS

                            4) VIWE SPECIFIC DETAILS

                            5) DELETE DETAILS


"""

print(menu)
choice = int (input("Select : "))
if choice == 1:
    # add data
    name = input("Enter Name : ")
    subject = input("Enter Subject : ")
    city = input("Enter City : ")

    values = (name,subject,city)

    str = "insert into STUDENT (name,subject,city) values ('%s','%s','%s')"
    mycursor.execute(str % values)
    mydb.commit()
    print("Successfully Data Inserted !!!")

elif choice == 2:
    # viwe student
    query = "select * from STUDENT"
    mycursor.execute(query)

    data = mycursor.fetchall()
    print(data)

elif choice == 3:
    # UPDATE DETAILS
    name = input("Enter Name: ")
    updatedname = input("Enter updated Name: ")
    subject = input("Enter Subject: ")
    city = input("Enter City: ")

    query = "UPDATE STUDENT SET name=%s, subject=%s, city=%s WHERE name=%s"
    values = (updatedname, subject, city, name)

    mycursor.execute(query , values)
    mydb.commit()


elif choice == 4 :
    # fetch specific data from the table
    name = input("Enter Name : ")
    query = "select * from STUDENT where name = '%s' "
    values = (name)
    mycursor.execute(query % values)
    data = mycursor.fetchone()

    print("Name :", data[1])
    print("Subject :", data[2])
    print("City :", data[3])

elif choice == 5 :
    id = int(input("Enter Id Want to Delete : "))
    query = "DELETE FROM STUDENT WHERE id =%s"
    values = (id)
    mycursor.execute(query , values)
    mydb.commit()
    print("Successfully Data Deleted !!!")
