from vehicle import Vehicle, Car, Motorcycle

car = Car("Toyota", "Corolla", 5)
moto = Motorcycle("Yamaha", "MT-07", "689cc")

car.accelerate()
car.drive(150)
car.open_trunk()

moto.accelerate()
moto.brake()
moto.drive(80)

print(car)
print(moto)

print(car.__dict__)
print(moto.__dict__)

print("Has private kilometers:",
      hasattr(car, "_Vehicle__kilometers"))

print("Mileage:", car.get_mileage(), "km")
