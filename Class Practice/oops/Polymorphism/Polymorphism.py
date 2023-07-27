"""
Polymorphism : 

    poly means many and moriphism means form

    Polymorphism is a greek word which is derived same name method with diffrent differnt forms

    there are mainly 2 types of Polymorphism

    1) method overloading
    2) method overridding

        1) method overloading : one class have morre than 2 method with same name and same parameters

            note : python does not support method overloading.

        2) method overriding :two class have same name method with same arguments its called method overriding

"""


class Student:
    
    def display(self):
        print("this is student class display")

    def display(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print(self.num1)
        print(self.num2)


obj = Student()
obj.display(10,20)
obj.display()