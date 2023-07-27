"""
to Hide or Prevent Data from Outside the Class

we can use some access specifiers or visibilities modes


=> public
=> privete
=> protected


by Deafult all the members are public 

if  we declare any variable as private we need to use __ in prefix

protected : we need to use _in prefix

private : which is only modify by current class

protected : which is modify by own class and child class

"""

class Products:
    def __init__(self) -> None:
        self.mobile = 5000
        self.__laptop = 26000  # private 

    def Display(self):
        print("Mobile :",self.mobile)
        print("Laptop : ", self.__laptop)

    def changePrice(self,laptopNewPric):
        self.__laptop = laptopNewPric

obj = Products()
obj.Display()

obj.mobile = 12000
obj.__laptop = 35000
obj.Display()

obj.changePrice(45000)
obj.Display()
