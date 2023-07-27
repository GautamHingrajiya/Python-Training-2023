"""
Abstraction : which is represent only few information, not allocated background information

Abstraction which is provide only front information

Abstraction concept hide implementation from outside the world

in python using ABC (Abstract Base Class) we can use this concept
 

"""

from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    
    def roi(self):
        pass

class SBI(RBI):

    def roi(self):
        print("ROI is 8.5%")

class HDFC(RBI):
    
    def Display(self):
        print("Welcome to HDFC")

    def roi(self):                  # comment to check 
        print("ROI is 7.5%")        # comment to check 


sbi = SBI()
sbi.roi()

hdfc = HDFC()
hdfc.Display()
hdfc.roi()