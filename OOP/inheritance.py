# a class that can inherit a functionality from another class
# for instance admin user can share more with ordinary users, but has extra permissions

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def meow(self):
        print(f"{self.name} says meeeeoooowssss 🐈")



# in here Lion class has inherit from Cat class
# the important thing here is the class that will be inherit 
# from will be passed as an argument to the new class.
# Lion class also can access all the methods in the Cat class, 
# this means Lion can call MEOW method, but cat can not call ROAR method.
class Lion(Cat):
    def roar(self):
        print(f"{self.name} is roaring 🦁🦁")

# my_lion = Lion('libaax')

# my_lion.roar()


# ==== inherit with the super() key word =====


class Horse(Cat):
    def __init__(self, name, age,color, speed):
       super().__init__(name,age)  # This line will 
       self.color = color
       self.speed = speed
    def ride(self):
        return {
            "name" : self.name,
            "age" : self.age,
            "color" : self.color,
            "speed" : self.speed
        }

white_hore = Horse("faras",8,"white","50mph")

print(white_hore.ride())



