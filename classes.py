#! object oriented programming concept 
# creating a class : a class is the blue print for creating an object

class Point(): 
    def __init__ (self, input1, input2): # __init__ serves as a constructor for a class : it gets called automatically when an object of a class is created

        self.x = input1
        self.y = input2
p = Point(2,8)

        