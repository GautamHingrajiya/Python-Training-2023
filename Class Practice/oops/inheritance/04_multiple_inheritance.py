# multiple inheritance

class A:
    def DisplayA(self):
        print("Display Method Class A")

class B:
    def DisplayB(self):
        print("Display Method Class B")

class C(A,B):
    def DisplayC(self):
        print("Display Method Class C")


obj = C()
obj.DisplayA()
obj.DisplayB()
obj.DisplayC()