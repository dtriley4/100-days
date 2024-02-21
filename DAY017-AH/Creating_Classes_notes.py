# 2-19-2024 Alexander: Udemy Python / Time to complete project == 1 hr
# Overview: Creating Classes

# Syntax
# class NameX: 
# all code is indented under the class

# name of class is always PascalCase, where each 1st letter in nomenclature is upper case

# Constructor is a part of the blueprint (class) what tells what should happen when the object is being constructed.

# Can use a special function with syntax: "__init__(self, X):" to initialize the attributes. See main.py for code examples.

# This function will be called every time you create a new  object from the class

# Attributes are essentially varibales associated with the final object

# You can add as many paramets as you wish to pass through objects though class. Once datat is received, you can use it to set the objects attributes.
# Example:

# class Car:
#     def __init__(self, seats):
#         self.seats = seats

# normal convetion to have the parameter name = the attribute name 
        
### Adding Methods to Class ###
        
# Attributes are what the object has and the methods are what the object does
# Example:
        
# Class = Car. An attribute is seats = 5. And one method could be a race_mode function for the car.
# When a function is attached to an object it is called a method
# Syntax for this example:
        
# class Car:
#     def enter_race_mode():
#         self.seats = 2

# my_car.enter_race_mode() # calls the

# Methods always need a "self" parameter as the inital parameter

# Codeing example for a social media account to represent user id and username and followrs and following count

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 #provides a default value instead of creating a parameter
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Alexander")
user_2 = User("002", "Rachel")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
