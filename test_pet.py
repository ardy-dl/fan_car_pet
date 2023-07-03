# import the pet class
from pet_class import Pet
# create instance of an object
pet = Pet("", "", 0)
# prompt the user for attributes and use the accessors to retrieve the attributes 
pet_name = str(input("Enter the name of your pet: "))
pet.set_name(pet_name)

pet_type = str(input("What type of an animal is the said pet? "))
pet.set_animal_type(pet_type)

pet_age = int(input("Enter the age of your pet (in years): "))
pet.set_age(pet_age)

# display
pet.get_name()
pet.get_animal_type()
pet.get_age()
