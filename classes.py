#! object oriented programming concept 
# creating a class : a class is the blue print for creating an object

class Point(): 
    def __init__ (self, input1, input2): # __init__ serves as a constructor for a class : it gets called automatically when an object of a class is created

        self.x = input1
        self.y = input2
p = Point(2,8)
print(p.x)
print(p.y)

#? writing a program for an airline needs to keep track of booking passengers on a flight and making sure that no flight overbooked we don't want more passengers more than capacity

class Flight() :
    def __init__(self, capacity): # every flight needs some sort of capacity to know how many people can fit
        self.capacity = capacity
        self.passengers = []

    def add_passenger (self, name):
        if not self.open_seats (): 
            return False    
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight (3)

people = ["harry", "Ron", "Prince" , "Ginny"]
for person in people :
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")




        