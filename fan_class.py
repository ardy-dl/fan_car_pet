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
    def status(self):
        status = "Fan is ON." if self.__is_on == True else "Fan is OFF."
        print(status)
    def turn_on(self):
        self.__is_on = True
        print("The Fan is turned ON.")

    def turn_off(self):
        self.__is_on = False
        print("The Fan is turned OFF.")
    # float radius
    def get_radius(self):
        print("Fan's Radius:",self.__radius)

    def set_radius(self, radius):
        if isinstance(radius, float):
            self.__radius = radius
            print("Fan's radius is now set to", radius)
        else:
            raise ValueError("Invalid radius. Please input a float.")
    # string color
    def get_color(self):
        print("Fan's Color:", self.__color)
    
    def set_color(self, color):
        if isinstance(color, str):
            self.__color = color
            print("The Fan's color is now set to", color)
        else:
            raise ValueError("Invalid fan color. Please input a string.")


Hanabishi = Fan()
Hanabishi.get_speed()
Hanabishi.set_speed(3)
Hanabishi.status()
Hanabishi.turn_on()
Hanabishi.turn_off()
Hanabishi.get_radius()
Hanabishi.set_radius(6.7)
Hanabishi.get_radius()
Hanabishi.get_color()
Hanabishi.set_color(red)
Hanabishi.get_color()

# test programs on a diff file
# fan_1 = max speed, radius 10, yellow, on 
# fan_2 = medium speed, radius 5, color blue, off
# display properties 