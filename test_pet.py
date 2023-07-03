# import the pet class
from pet_class import Pet
import tkinter as tk

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

# design
root = tk.Tk()
root.title("My Pets")
root.config(bd=10)
text = tk.Text(root, width = 40, height =40)
text.pack() 
# display
for i, pet in enumerate(pets):
    text.insert(tk.END, f"Pet {i+1}:\n")
    pet.get_name(text)
    pet.get_animal_type(text)
    pet.get_age(text)

root.mainloop()