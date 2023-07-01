# create class named fan
class Fan:
    # initialization (all private)
    def __init__(self, speed="slow", radius=5, color="blue"):
        # speed (df: slow)
        self.__speed = speed
        # radius (df: 5)
        self.__radius = radius
        # color (df: blue)
        self.__color = color
        # on (df: false)
        self.__is_on = False

Hanabishi = Fan()
print(Hanabishi)

    # integer speed
    # boolean on or off (df: false)
    # float radius
    # string color
    # get speed
    # set speed
    # get radius
    # set radius
    # get color
    # set color

# test programs on a diff file
# fan_1 = max speed, radius 10, yellow, on 
# fan_2 = medium speed, radius 5, color blue, off
# display properties 