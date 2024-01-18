# 1-18-2024 Alexander: Udemy Python / Time to complete project == 1.5 hours
#Overview: Dictionaries and Nesting

'''
#dictionaries Syntax:
key_dictionary = {
    "Key1": "Value1",
    "Key2": "Value2",
}


#retrieve value from dictionary syntax:
key_dictionary["Key1"]


#add new value to dicionary syntax:
key_dictionary["Key3"] = "Value3"


#start an empty dictionary syntax:
empty_dictionary = {}


#wipe an existing dictionary by making an empty dictionary farther down in the code:
key_dictionary = {}


#edit item in dictionary syntax:
key_dictionary["Key1"] = "NewValue1"


#loop through a dictionary syntax using for loop:
for key in key_dictionary:
    print(key) #prints out only the key(s) in key_dictionary and not the "value(s)"

    print(key_dictionary[key]) #prints out both the key(s) and the value(s) in key_dictionary

    
    

# TODO Example problem and code solution:
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  score = student_scores[student]
  if score >= 91:
    student_grades[student] = "Outstanding"
  elif score >= 81:
    student_grades[student] = "Exceeds Expectations"
  elif score >= 71:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)




#nesting inside dictionary sytnax example:
{
Key1: [List],
Key2: {Dict},
}


#sample dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


#nesting list in dictionary:
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],  
}


#nesting a list in a list:
["A", "B", ["C", "D"]]


#nesting a dictionary with a list inside a dictionary:
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visit": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visit": 12},  
}


#nesting a dictionary inside a list syntax example:
[{
    Key: [List],
    Key2: {Dict},
},
{
    Key: Value,
    Key2: Value,
}]


#nesting a dictionary inside list example with a list that contains two items that are each a dictionary that has 3 key-value pairs containing three datas types (string, list, integer):
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visit": 12,
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visit": 12,  
    }
]




# TODO Example problem and code solution:
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name, times_vistited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_vistited
  new_country["cities"]  = cities_visited
  travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
'''



#DAY 9 Project: Silent and Secret Auction
#TODO
#1. Greeting
#2. ask and input for name
#3. ask and input for buid amount
#4. ask and input for if there are multiply bidders
#5 if yes, clear console, and repeat the above steps until new bidders is false
#6. after all bids entered, print who the has the higgest bidder


'''#import and define a clear function to clear console screen bewteen bidders
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#creating a few auction items that are randomly chosen for the greeting
import random
auction_items = ["a large pet snake", "a gently used 2001 Honda Civic", "a dishwasher", "a pair of tube socks", "a painting of your mother", "a gold bar", "a brand new helicopter"]
random_auction_item = random.choice(auction_items)

#greeting and input variables
print(f"Welcome to the Secret Auction. Today we are auctioning off {random_auction_item}!")
name = input("What is your name? ") #get name
bid = int(input("What is your bid amount? $")) #get bid
#empty list to store input names and bids
bidders_dictionary = []

#define add bidder function
def add_bidder (new_name, new_bid):
  new_bidder = {}
  new_bidder["name"] = new_name
  new_bidder["bid"] = new_bid
  bidders_dictionary.append(new_bidder)

def add_new_bidder():
  add_new_bidder = input("Are they any other bidder? Type Y/N" ).upper()
  if add_new_bidder() == "Y":
    clear_screen()
    add_bidder()

add_bidder(name, bid)
add_new_bidder()
print(bidders_dictionar'''

#fresh start take 2 
import os
import random

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Creating a few auction items that are randomly chosen for the greeting
auction_items = ["a large pet snake", "a gently used 2001 Honda Civic", "a dishwasher", "a pair of tube socks", "a painting of your mother", "a gold bar", "a brand new helicopter"]
random_auction_item = random.choice(auction_items)

# Greeting and input variables
print(f"Welcome to the Secret Auction. Today we are auctioning off {random_auction_item}!")
name = input("What is your name? ").upper() # Get name
bid = int(input("What is your bid amount? $"))  # Get bid

# Empty list to store input names and bids
bidders_list = []

# Define add_bidder function
def add_bidder(new_name, new_bid):
    new_bidder = {"name": new_name, "bid": new_bid}
    bidders_list.append(new_bidder)

# Define add_new_bidder function
def add_new_bidder():
    add_new_bidder_input = input("Are there any other bidders? Type Y/N ").upper()
    return add_new_bidder_input == "Y"

# Initial bidder entry
add_bidder(name, bid)

# Check if there are more bidders
while add_new_bidder():
    clear_screen()
    name = input("What is your name? ").upper()
    bid = int(input("What is your bid amount? $"))
    add_bidder(name, bid)

# Find the highest bidder
highest_bidder = max(bidders_list, key=lambda x: x['bid'])

# Print the highest bidder
print(f"\nThe highest bidder is {highest_bidder['name']} with a bid of ${highest_bidder['bid']} and wins {random_auction_item}.")

# Print the list of bidders
print("\nList of Bidders:")
for bidder in bidders_list:
    print(f"Name: {bidder['name']}, Bid: ${bidder['bid']}")
