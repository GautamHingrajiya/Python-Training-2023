"""
Encapsulation : Which is Behave like Capsule

Which is Contain Data Member and Member Function in single Entity

encapsulation which is represent data member in group

best Exapmle of Encapsulation is a class


"""

class Shop:

    def setProduct(self,productName):
        self.productname = productName

    def getProduct(self):
        return self.productname
    

obj = Shop()
obj.setProduct("Mobile")
print(obj.getProduct())