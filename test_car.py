from car_class import Car
# Testing in a diff file
car_1 = Car("2021 Mazda3 Turbo", "Mazda", 130)
# 1 car = acc 5x, after EACH call get speed, display. brake x5, after EACH call get speed and display.
for i in range(5):
    car_1.accelerate()
    car_1.get_speed()
    car_1.brake()
    car_1.get_speed()


