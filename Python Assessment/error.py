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
def fn_counsellor():

    
    
    

    c_status = True
    while c_status:
        student_main = {}
        student_details = {}
        student_subject = {}
        
        rollno = int(input("Enter Roll No. : "))

        if rollno in student_main:
            print("Roll No. Already Exist")
        else:
            print("\nEntered Roll No. Available for Registration\n")
            fname = input("Enter First Name : ").upper()
            lname = input("Enter Last Name : ").upper()
            contactno = int(input("Enter Contact No. : "))
            facultyname = input("Enter Faculty Name : ").upper()

            student_details['fname'] = fname
            student_details['lname'] = lname
            student_details['contact'] = contactno
            student_details['faculty'] = facultyname
            student_main[rollno]=student_details
            
            c_sub = True
            while c_sub:
                
                student_marks = {}

                subject = input("Enter Subject Name : ").upper()
                marks = int(input("Enter Marks : "))
                fees = int(input("Enter Fees : "))

                student_marks['marks'] = marks
                student_marks ['fees'] = fees
                
                



                check = input("Want More subject (y/n) : ").upper()
                if check == "N" :
                    c_sub = False
                elif check == "Y" :
                    c_sub = True
                else:
                    print("Enter Valid Input")

            student_details['subject'] = student_subject
            student_subject[subject]=student_marks

            print("\n")
            print(student_main)





        check = input("Want More Operation (y/n) : ").upper()
        if check == "N" :
            status = False
        elif check == "Y" :
            status = True
        else:
            print("Enter Valid Input")
            input()
    

def fn_faculty():
    pass

def fn_student():
    pass

status = True
while status:
    
    print(welcome)
    
    role = int(input("Select Roll : "))

    match role:

        case 1 :
            print(counsellor_display)
            c_role = int(input("Select Operation : "))
            fn_counsellor()


        case 2 :
            print(faculty_display)
            f_role = int(input("Select Operation : "))
            fn_faculty()

        case 3 :
            print(student_display)
            fn_student()


        case _ :
            print("Enter Valid Input")



    check = input("Want to Exit (y/n) : ").upper()
    if check == "N" :
        status = True
    elif check == "Y" :
        status = False
    else:
        print("Enter Valid Input")
        input()