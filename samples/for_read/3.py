# Vehicle class
class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def drive(self):
        print(f"Driving at {self.max_speed} mph")


# Create car
car = Vehicle(220)

# Drive car
car.drive()
