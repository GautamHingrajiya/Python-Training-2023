"""

OPPS : Object Oriented Programing system or structure.

        Class : Class is a Collection of Data Member and Member Function

        Classs Which is Contain Data Member and Member Function in Single Entity

        Classs Which is Behave like Group Of Elements

        we can Store Similar and dis-similar data Elements in Class  

        Class Syntax:

            class < Class Name >:
                data Member
                Membeer Funcction     

Object : Object is an Instance or Variable of Class 

         using of Object we Can Access All the Properties of Class 

         Syntax:

         odjname : classname()
"""


class Student():
    id = 1              # Data Members
    name = "Gautam"
    subject = "Python"


# Object Creation

obj = Student()
print(obj.id)
print(obj.name)
print(obj.subject)