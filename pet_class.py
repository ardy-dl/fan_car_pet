import tkinter as tk

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
    def show(self, text_widget):
        text_widget.insert(tk.END, f"Name: {self.__name} | Animal Type: {self.__animal_type} | Age: {self.__age}\n")
    # get name
    def get_name(self, text_widget):
        text_widget.insert(tk.END, f"Name: {self.__name}\n")
    # get animal type
    def get_animal_type(self, text_widget):
        text_widget.insert(tk.END, f"Animal Type: {self.__animal_type}\n")
    # get age 
    def get_age(self, text_widget):
        text_widget.insert(tk.END, f"Age: {self.__age}\n")
    # set name
    def set_name(self, name):
        self.__name = name
    # set animal type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    # set age
    def set_age(self, age):
        self.__age = age
    