"""

1) single level inheritance

single class derived properties of another class

"""

class parant:
    def bike(self):
        print("I have Bike")

class child(parant):
    def cycle(self):
        print("I have My Own Cycle")

# object Creation

obj = child()

obj.bike()
obj.cycle()

