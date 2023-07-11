welcome = """
                                                WELCOME TO STUDENT MANAGEMENT SYSTEM

                                                1) COUNSELLOR

                                                2) FACULTY

                                                3) STUDENT



"""

counsellor_display = """

                                                WELCOME COUNSELLOR

                                                1) ADD STUDENT

                                                2) REMOVE STUDENT

                                                3) VIWE ALL STUDENT

                                                4) VIWE SPECIFIC STUDEN


"""

faculty_display = """

                                                WELCOME FACULTY

                                                1) ADD MARKS TO STUDENT

                                                2) VIWE ALL STUDENT

"""

student_display = """

                                                WELCOME STUDENT

"""

def consellor ():
    global sub_student
    global main_student
    global sub_student_sub

    c_role = int(input("Select Your Role by Entering Number : "))

    if c_role == 1:
        a_status = True
        while a_status:
                
            student_roll_no = int(input("Enter Roll No : "))
            Student_firstname = input("Enter First Name : ").upper()
            Student_lastname = input("Enter Last Name : ").upper()
            Student_contact_no = int(input("Enter Contact No : "))
            Student_subject = input("Enter Subject Name : ").upper()
            Student_marks = int(input("Enter Marks : "))
            Student_fees = int(input("Enter Fees : "))


            sub_student_sub ['marks'] = Student_marks
            sub_student_sub ['fees'] = Student_fees
            sub_student['firstname'] = Student_firstname
            sub_student['lastname'] = Student_lastname
            sub_student['contactno'] = Student_contact_no
            
            sub_student[Student_subject] = sub_student_sub
            main_student[student_roll_no]=sub_student

            check = input("Add More (y/n) : ").upper()
            if check == "Y":
                a_status = True
            elif check == "N":
                a_status = False
            else:
                print("Enter Valid Input ") 

        print(main_student)
    
    elif c_role == 2:
        d_status = True
        while d_status:
            student_roll_no = int(input("Enter Roll No : "))
            
            if student_roll_no in main_student:

                main_student.pop(student_roll_no)

            else: 
                print(" Enter Valid Roll No. ")    
            check = input("Delete More (y/n) : ").upper()
            if check == "Y":
                d_status = True
            elif check == "N":
                d_status = False
            else:
                print("Enter Valid Input ")
        print(main_student)


    elif c_role == 3:
        pass
    elif c_role == 4:
        pass






    

def faculty ():
    f_role = int(input("Select Your Role by Entering Number : "))
    rollnm = int(input("Enter Roll Number : "))
    if f_role == 1:
        if rollnm in main_student:
            Student_subject = input("Enter Subject Name :").upper()
            if Student_subject in sub_student:
                Student_marks = int(input("Enter Marks : "))
                sub_student_sub ['marks'] = Student_marks
                sub_student[Student_subject] = sub_student_sub
            else:
                print("Subject Not Available Press Enter to Add Subject")
                Student_subject = input("Enter Subject Name : ").upper()
                Student_marks = int(input("Enter Marks : "))
                sub_student_sub ['marks'] = Student_marks
                sub_student[Student_subject] = sub_student_sub
            print(main_student)
            
                
        else: 
            print("Enter Roll no in not Available")
        
    elif f_role ==2:
        pass
    else:
        print("Enter Valid Input ")
def student ():
    for f,l in main_student:
        print(f"Roll No. {f} \tFirst Namme : {l['firstname']} \tlast Name : {l['lastname']} ")





main_student = {}
sub_student = {}
sub_student_sub = {}
status = True
while status:

    print(welcome)

    role = int(input("Select Your Role by Entering Number : "))
    if role == 1:
        print(counsellor_display)
        
        consellor()
        

    elif role == 2:
        print(faculty_display)
        
        faculty ()

    
    elif role == 3:
        print(student_display)

        student ()

    else:
        print("Enter Valid Input : ")


    check = input("Want to Exit (y/n) : ").upper()
    if check == "Y":
        status = False
    elif check == "N":
        status = True
    else:
        print("Enter Valid Input ")
