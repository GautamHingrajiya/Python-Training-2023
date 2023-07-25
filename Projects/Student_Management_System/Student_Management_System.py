from packages import counsellor_logic,faculty_logic,student_logic


welcome = """
                                                WELCOME TO STUDENT MANAGEMENT SYSTEM

                                                1) COUNSELLOR

                                                2) FACULTY

                                                3) STUDENT
"""

status = True
while status :
    
    print(welcome)
    role = int(input("Select Role By Entering Role : "))
    
    match role:

        case 1:         
            # print(counsellor_logic.counsellor_display)
            counsellor_logic.fn_counselloer()

        case 2:
            # print(faculty_logic.counsellor_display)
            faculty_logic.fn_faculty()

        case 3 :            
            # print(student_logic.counsellor_display)
            student_logic.fn_student         
        case _:
            print("Enter Valid Input")


    check = input("Want to Exit (y/n) : ").upper()
    if check == "Y":
        status = False
    elif check == "N":
        status = True
    else:
        print("Enter Valid Input")