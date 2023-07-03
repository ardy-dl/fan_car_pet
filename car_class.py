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
        return self.__speed
        
    # brake() subtract 5 to speed
    def brake(self):
        self.__speed -=5
        return self.__speed
    # get_speed() return current speed
    def get_speed(self):
        print(self.__year_model, "'s current speed is", self.__speed)
