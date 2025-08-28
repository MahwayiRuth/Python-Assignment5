# ================= Base Class: Vehicle =================
class Vehicle:
    def __init__(self, name):
        self.name = name

    # Generic move method (can be overridden)
    def move(self):
        print(f"{self.name} is moving.")


# ================= Subclass: Car =================
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road 🚗.")


# ================= Subclass: Plane =================
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky ✈️.")


# ================= Subclass: Boat =================
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the water ⛵.")


# ================= Create Objects =================
my_car = Car("Honda Civic")
my_plane = Plane("Boeing 747")
my_boat = Boat("Sailor 3000")

# ================= Demonstrate Polymorphism =================
vehicles = [my_car, my_plane, my_boat]

for vehicle in vehicles:
    vehicle.move()  # each move() behaves differently depending on class
