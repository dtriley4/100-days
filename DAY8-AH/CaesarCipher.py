# 1-13-2024 Alexander: Udemy Python / Time to complete project == 
#Overview: Functions with inputs & Caesar Cipher


'''
#day 8 function review:
#checlkist:
#1. create a function called greet()
#2. write 3 print statements inside function
#3. call the function and run code

#my code:
#simple function
def greet():
    print("Hello.")
    print("How are you?"
    print("You're neat.")
    
greet()

#doing more with functions
#can add inside variable to be executed in function
#ex:


#function with input syntax
def my_function(something):
    #do this with something
    #then do this
    #finally do this

my_function(123)

#example
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")

greet_with_name("Alexander")


#functions with > 1 inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?) 

greet_with("Alexander", "Earth")


#functions with keyword arguments for above example
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?) 

greet_with(name="Alexander", location="Earth") #creates less errors due to postional argument errors

#Prime number checker exercise on Auditorium
#soultion 
# Write your code below this line 👇
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

'''

#DAY 8 Project: Create a Caesar cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar_cipher(text, shift, mode, alphabet):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Find the index of the character in the alphabet
            char_index = alphabet.index(char.lower())
            
            # Apply the Caesar cipher shift based on the mode (encode or decode)
            if mode == 'encode':
                shifted_index = (char_index + shift) % 26
            elif mode == 'decode':
                shifted_index = (char_index - shift) % 26
            else:
                raise ValueError("Invalid mode. Use 'encode' or 'decode'.")
            
            shifted_char = alphabet[shifted_index]
            
            # Convert back to uppercase if the original character was uppercase
            if is_upper:
                shifted_char = shifted_char.upper()
            
            # Append the shifted character to the result
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

# Perform the Caesar cipher using the provided variables
cipher_text = caesar_cipher(text, shift, direction, alphabet)

# Print the result
print(f"Original text: {text}")
print(f"Result text: {cipher_text}")
