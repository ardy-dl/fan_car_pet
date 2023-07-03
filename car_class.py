# Car class
class Car:
    # initialize
    def __init__(self, year_model, make, speed = 0):
        # Year model
        self.__year_model = year_model
        # make of the car
        self.__make = make
        # current speed (0)
        self.__speed = speed

    def show(self):
        print("Year Model:", self.__year_model, "| make:", self.__make, "| speed:", self.__speed)
    # methods
    # accelerate() Add 5 to speed each time it is called
    def accelerate(self):
        self.__speed +=5
        print(self.__speed)
    # brake() subtract 5 to speed
    # get_speed() return current speed

# Testing in a diff file
car_1 = Car("2021 Mazda3 Turbo", "Mazda", 130)
car_1.show()
car_1.accelerate()
# 2021 mazda3 by Mazda
# 1 car = acc 5x, after EACH call get speed, display. brake x5, after EACH call get speed and display.