class A:
    num1 = 10
    num2 = 20
    
    def displayA(self):
        print(self.num1)
        print(self.num2)

class B:
    num3 = 30
    num4 = 40
    
    def displayB(self):
        print(self.num3)
        print(self.num4)

class C(A,B):
    def addition(self):
        self.ans = A.num1 + A.num2
        return self.ans        
    def multiplication(self):
        self.ans = B.num3 * B.num4
        return self.ans
    
"""
A           B
|-----------|
|-----------|
      |
      V
      C

"""

obj = C()
obj.displayA()
obj.displayB()
print(obj.addition())
print(obj.multiplication())