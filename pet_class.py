# pet class
class Pet:
    # initialize
    def __init__(self, name, animal_type, age):
        # name of the pet
        self.__name = name
        # animal_type like dog, cat, rabbit etc.
        self.__animal_type = animal_type
        # age
        self.__age = age
    # methods
    def show(self):
        print(self.__name, self.__animal_type, self.__age)
    # get name
    def get_name(self):
        print("The name of the Pet is", self.__name)
    # get animal type
    def get_animal_type(self):
        print("The animal type is", self.__animal_type)
    # get age 
    def get_age(self):
        print("The age of the pet is", self.__age)
    # set name
    # set animal type
    # set age
    
pet_1 = Pet("callie", "dog", 2)
pet_1.show()
pet_1.get_name()
pet_1.get_animal_type()
pet_1.get_age()
# new file that creates an object but from user prompt and ask the attributes.
# use the accessors to retrieve the attributes and display.