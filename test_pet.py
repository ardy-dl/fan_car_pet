# import the pet class
from pet_class import Pet
# if the user has pet greater than 1
num_pets = int(input("Enter the number of pets you want to add: "))
pets = []

for i in range(num_pets):
    print(f"Pet {i+1}: ")
    # create instance of an object
    pet = Pet("", "", 0)
    # prompt the user for attributes and use the accessors to retrieve the attributes 
    pet_name = str(input("Enter the name of your pet: "))
    pet.set_name(pet_name)

    pet_type = str(input("What type of an animal is the said pet? "))
    pet.set_animal_type(pet_type)

    pet_age = int(input("Enter the age of your pet (in years): "))
    pet.set_age(pet_age)

    pets.append(pet)

# display
print("Pet Details:")
for i, pet in enumerate(pets):
    print(f"Pet {i+1}:")
    print("Name:", pet.get_name())
    print("Animal Type:", pet.get_animal_type())
    print("Age:", pet.get_age())
