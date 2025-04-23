"""Write a class called Converter. The user will pass a length and a unit when declaring an object
from the class—for example, c = Converter(9,'Inches'). The possible units are Inches, FEET,
YARDS, MILES, KILPMTERS, METERS, CENTIMETERS, and MILIMETER. For each of these units there
should be a method that returns the length converted into those units. For example, using the
Converter object created above, the user could call c.FEET() and should get 0.75 as the result."""


class Converter:

    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def METERS(self):
        if self.unit == 'Inches':
            return self.length * 0.0254
        elif self.unit == 'FEET':
            return self.length * 0.3048
        elif self.unit == 'YARDS':
            return self.length * 0.9144
        elif self.unit == 'MILES':
            return self.length * 1609.34
        elif self.unit == 'KILOMTERS':
            return self.length * 1000
        elif self.unit == 'METERS':
            return self.length
        elif self.unit == 'CENTIMETERS':
            return self.length * 0.01
        elif self.unit == 'MILIMETER':
            return self.length * 0.001

    def Inches(self):
        
        METERS = self.METERS()
        return METERS / 0.0254

    def FEET(self):
        
        METERS = self.METERS()
        return METERS / 0.3048

    def YARDS(self):
        
        METERS = self.METERS()
        return METERS / 0.9144

    def MILES(self):
        
        METERS = self.METERS()
        return METERS / 1609.34

    def KILPMTERS(self):
        
        METERS = self.METERS()
        return METERS / 1000

    def CENTIMETERS(self):
        
        METERS = self.METERS()
        return METERS / 0.01

    def MILIMETER(self):

        METERS = self.METERS()
        return METERS / 0.001



value = int(input("Enter the value: "))
c = Converter(value, 'Inches')
print("To METERS", c.METERS())     
print("To FEET", c.FEET())       
print("To CENTIMETERS", c.CENTIMETERS())  
print("To KILPMTERS", c.KILPMTERS())
print("To MILES", c.MILES())
print("To MILIMETER", c.MILIMETER())
print("To YARDS", c.YARDS())
