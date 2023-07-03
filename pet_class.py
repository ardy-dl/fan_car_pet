# pet class
class Pet:
    # initialize
    def __init__(self, name, animal_type, age):
        # name of the pet
        self.__name = name
        # animal_type
        self.__animal_type = animal_type
        # age
        self.__age = age
    # methods
    def show(self):
        print(self.__name, self.__animal_type, self.__age)

pet_1 = Pet("callie", "dog", 2)
pet_1.show()
    # set name
    # set animal type
    # set age
    # get name
    # get animal type
    # get age 

# new file that creates an object but from user prompt and ask the attributes.
# use the accessors to retrieve the attributes and display.