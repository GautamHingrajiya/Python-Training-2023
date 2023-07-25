class Vehical:
    def color(self):
        print("This Is Color Method")
    def speed(self):
        print("This Is Speed Method")
    def wheels(self):
        print("This Is Wheels Method")
    def brand(self):
        print("This Is Brand Method")

class car(Vehical):
    def colorcar(self):
        print("This Is Car Color Method")
    
class bike(Vehical):
    pass


# object Creation

objcar= car()
objbike = bike()
objcar.color()
objcar.colorcar()