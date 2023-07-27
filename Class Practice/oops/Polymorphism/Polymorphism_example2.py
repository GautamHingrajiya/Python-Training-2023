"""

2) method overridding

two - parent and hild class both have same name methods with same numbers of arguments

"""

class Vehical:
    def speed(self):
        print("Max Speed Limit : 80 KMH")

class Car(Vehical):
    def speed(self):
        print("Max Speed Limit : 120 KMH")
        return super().speed()

obj = Car()

obj.speed()