class Vehicle:
    max_speed = 120

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.current_speed = 0
        self.__kilometers = 0

    def accelerate(self):
        self.current_speed += 10

    def brake(self):
        self.current_speed -= 10
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, km):
        self.__kilometers += km

    def get_mileage(self):
        if hasattr(self, "_Vehicle__kilometers"):
            return self._Vehicle__kilometers
        return 0

    def __str__(self):
        return f"{self.brand} {self.model} - Speed: {self.current_speed} km/h"


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def accelerate(self):
        self.current_speed += 15

    def open_trunk(self):
        print("The trunk is open.")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, displacement):
        super().__init__(brand, model)
        self.displacement = displacement

    def brake(self):
        self.current_speed -= 15
        if self.current_speed < 0:
            self.current_speed = 0
