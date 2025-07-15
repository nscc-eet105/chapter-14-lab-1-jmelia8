#Joe Melia EET-107

class Vehicle:

    def __init__(self, speed):
        self.speed = 0
    def accelerate(self):
        self.speed += 1
    def decelerate(self):
        self.speed -= 1
    def display_speed(self):
        return self.speed

def main():
    vehicle = Vehicle(0)
    for start in range(2):
        print("Accelerating...")
        vehicle.accelerate()
        print("Current speed: ", vehicle.display_speed())
    print("")
    for stop in range(2):
        print("Decelerating...")
        vehicle.decelerate()
        print("Current speed: ", vehicle.display_speed())
main()
        
