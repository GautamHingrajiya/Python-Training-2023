# single level inheritance

class A:
    def DisplayA(self):
        print("Display Method Class A")

class B(A):
    def DisplayB(self):
        print("Display Method Class B")

obj = B()
obj.DisplayA()
obj.DisplayB()

