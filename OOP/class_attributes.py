# Attributes are something all class instances share.
# Attributes are defined in the class itself.

class Car:
    num_cars = 0
    def __init__(self, make,model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        Car.num_cars += 1

print(f"Before creating any car we have this {Car.num_cars} number of cars")


almera = Car('nissan', 'Almera', 2004,'gray')
safira = Car('Voksol', 'Saffira', 2008,'blue')



print(f"We have this {Car.num_cars} number of cars")
        


