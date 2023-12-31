# create class named fan
class Fan:
    # initialization (all private)
    def __init__(self, name = "Default", speed = 1, radius = 5, color = "blue"):
        self.__name = name
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
        status = "Fan is ON." if self.__is_on == True else "Fan is OFF."
        print(self.__name, "-", self.__speed, "| radius:", self.__radius, "| color:", self.__color, "|", status)

    # integer speed
    def get_speed(self):
        print(self.__speed)
    
    def set_speed(self, speed):
        if speed == 1:
            print(self.__name, "'s speed is now SLOW")
        elif speed == 2:
            print(self.__name, "'s speed is now MEDIUM")
        elif speed == 3:
            print(self.__name, "'sspeed is now FAST")
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
        print(self.__name, "'s Radius:",self.__radius)

    def set_radius(self, radius):
        if isinstance(radius, float):
            self.__radius = radius
            print(self.__name, "'s radius is now set to", radius)
        else:
            raise ValueError("Invalid radius. Please input a float.")
    # string color
    def get_color(self):
        print(self.__name, "'s Color:", self.__color)
    
    def set_color(self, color):
        if isinstance(color, str):
            self.__color = color
            print(self.__name, "'s color is now set to", color)
        else:
            raise ValueError("Invalid fan color. Please input a string.")

