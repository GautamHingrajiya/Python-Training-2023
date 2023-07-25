# self : sel is a keyword which is represent current class properties

class student:
    def input(self,fname,subject):
        self.fname = fname
        self.subject = subject

    def display(self):
        print("name :" , self.fname)
        print("Subject : ", self.subject)

obj = student()
obj.input("Gautam", "Python")
obj.display()