# 2-6-2024 Alexander: Udemy Python / Time to complete project == 1 hr
# Overview: OOP (Object Oriented Programming)

# So far we have done Procedural programmming: which is programming where procedures or functions are in place to execute particular things.
# Increasing these prodecures and complexity of the code can begin to become hard to follow and confusing.

# Creating seperate modules for larger scale and complex code can help simplify these larger types of programs.
# This way of building out modules means they can be used for other programs as well where there is a crossover in the desired program.

# Object Oriented Programming is a style of coding that splits larger tasks into these smaller, modular pieces, where each module can have it's own designated team.
# OOP is aimed to model real life objects, each with their own attributes and functions

# How to use OOP
    # 1. Identify each component needed for the project
    # 2. For each module, identify:
        # a. what is has. (attributes) (often variable)
        # b. what it does (methods) (often functions)


# Example
    # A resturant
    # Modules to model:
        # a. Chef
        # b. Cleaner
        # c. Waiter
        # d. Host
        # etc.

# We could choose one, such as the waiter, and build a model with attributes and methods attached to that particular object (waiter).
# Once we can identify what a waiter is and does, we can they itterate various versions of the same object (waiter)
# This is called a class in OOP. So these class blueprints (waiter) would be the class, and the iterations (waiter Joe, waiter Bob, etc) are called objects.

# Syntax for creating classes and objects:
    # car = CarBlueprint() , where car is the Object, and CarBlueprint() is the Class. 
    # The Class is PascalCase, which is where each words first letter is capital. Done to differntiate it from all function and variables names with _ between each word of function or variable.

# To pratice, we can use Turtle Graphics, a preloaded python package.

from turtle import Turtle, Screen #importing the module

timmy = Turtle() #constructing our object Timmy, from the class Turtle
print(timmy)

# Accessing object attributes (variables) syntax:
    # ex. car.speed where car is the object, and speed is the attribute we are calling

my_screen = Screen() #creating an object (my_screen) from the class module (Screen)
my_screen.canvheight #calling the attriubte for the screen, or canvas height
print(my_screen.canvheight) 

# Acessing object methods (functions) syntax:
    # ex. car.stop() where car is the object, and stop is the function we are calling

my_screen.exitonclick() # allows the program to run the screen until there is a click.

timmy.shape("turtle") #calling method to change shape of timmy
timmy.color("green") #calling methods to change color of timmy
timmy.forward(100) #calling methods to move position of timmy

# Python Packages can be used to install and import other code that devs have already written.
# Pypi.org is a good resource for finding packages.

# For installing package libraries in VS code for specific projects:
    # Open terminal and enter:
    # python -m venv (insert project path like C:\Users\...\venv)
    # then install downloaded package by entering in terminal:
    # pip install (library)

