# create class named fan
class Fan:
    # initialization (all private)
    def __init__(self, speed = 1, radius = 5, color = "blue"):
        # speed (df: slow)
        self.__speed = speed
        if speed == 1:
            self.__speed = "Speed: SLOW"
        elif speed == 2:
            self.__speed = "Speed: MEDIUM"
        elif speed == 3:
            self.__speed = "Speed: FAST"
        # radius (df: 5)
        self.__radius = radius
        # color (df: blue)
        self.__color = color
        # on (df: false)
        self.__is_on = False

    def show(self):
        print(self.__speed, self.__radius, self.__color, self.__is_on)

    # integer speed
    def get_speed(self):
        print(self.__speed)
    
    def set_speed(self, speed):
        if speed == 1:
            print("Fan's speed is now SLOW")
        elif speed == 2:
            print("Fan's speed is now MEDIUM")
        elif speed == 3:
            print("Fan's speed is now FAST")
        else:
            raise ValueError("Invalid Fan speed. Please choose between 1, 2, or 3.")
        
    
    # boolean on or off (df: false)
    # float radius
    # string color
    # get speed
    # set speed
    # get radius
    # set radius
    # get color
    # set color

Hanabishi = Fan()
Hanabishi.get_speed()
Hanabishi.set_speed(3)

# test programs on a diff file
# fan_1 = max speed, radius 10, yellow, on 
# fan_2 = medium speed, radius 5, color blue, off
# display properties 