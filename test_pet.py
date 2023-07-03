# import the pet class
from pet_class import Pet
# create instance of an object
pet = Pet("", "", 0)
# prompt the user from attributes and use the accessors to retrieve the attributes 
pet_name = str(input("Enter the name of your pet: "))
pet.set_name(pet_name)

# display
pet.get_name()
