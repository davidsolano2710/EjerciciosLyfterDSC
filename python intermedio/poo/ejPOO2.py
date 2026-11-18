import random


class Person():
	def __init__(self, name):
		self.name = name
		self.age = 0

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.current_passengers = 0
        self.passengers = []


    def add_passenger(self, person):
        if self.current_passengers < self.max_passengers:
            self.current_passengers += 1
            self.passengers.append(person)
            print(f"Passenger {person.name} got on the bus.")
        else: 
            print("Bus is full!")


    def drop_off_passenger(self):             #drops a random passenger from the bus
        if self.current_passengers > 0:
            r_number = random.randint(0, self.current_passengers - 1)
            dropped_passenger = self.passengers.pop(r_number)
            print(f"Passenger {dropped_passenger.name} got off the bus.")
            self.current_passengers -= 1
        else:
            print("No passengers to drop off.")
            return
            
        
bus1 = Bus(3)

person1 = Person("Alicia")
person2 = Person("Luis")
person3 = Person("Charlie")
person4 = Person("David")
person5 = Person("Sofia")

bus1.add_passenger(person1)
bus1.add_passenger(person2)
bus1.add_passenger(person3)
bus1.drop_off_passenger()
bus1.add_passenger(person4) 
bus1.add_passenger(person5)


    