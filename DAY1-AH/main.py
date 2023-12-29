# 12-29-2023 Alexander: Udemy Python / Time to complete= 12:30pm - 
# Overview: printing, comments, debug, string manipulation, variables 
# Joined Auditorium interactive courses

# print("Hello " + input("What is your name?"))

#adding variables

# name = input("What is your name?")
# print(name)

#using stored data

name = input("What is your name?")
length = len(name)
print(length)

# Using temp or extra variables to swap data
# There are two variables, a and b 
a = input()
b = input()
# Create a third variable to help switch the values
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# variable naming
# Use single words or underscores for multi-words, numbers go after words

# DAY 1 Project: Band Name Generator
#Executables:

#1. Create a greeting
#2. Ask user for city their from
#3. Ask user for pet name
#4. Combine city name and pet name
#5. Curser starts on new line

print("Welcome to Band Name Generator!") #Greeting/Header
city_name = input("What city are you from? \n")
pet_name = input("What is a pet name you like? \n")
print("Your band name is " +city_name+" "+pet_name)
