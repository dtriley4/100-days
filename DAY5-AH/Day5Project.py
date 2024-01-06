# 1-5-2024 Alexander: Udemy Python / Time to complete project <= 45 mins
# Overview: Loops, Range, Code Blocks

'''lesson 16 auditorium
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum_height = 0
#find sum of height
for n in student_heights:
    sum_height += n
print(f"total height = {sum_height}")
#fid sum of list items
sum_students = len(student_heights)
print(f"number of students = {sum_students}")

average_height = round(sum_height / sum_students)
print(f"average height = {average_height}")
'''

'''
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
heighest_score = 0
for score in student_scores:
    if score > heighest_score:
      heighest_score = score
print(f"The highest score in the class is: {heighest_score}")'''


'''lesson 18 auditorium
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
#find even numbers in input
even_sum = 0

for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)
'''


'''*****lesson 19 - FIZZBUZZ - VERY COMMON JOB INTERVIEW QUESTION*****
1. program shoud print each number from 1 to 100 in turn and include number 100
2. if number is divisble by 3 it should print "Fizz"
3. if number is disible by 5 it should print "Buzz"
4. if number is divisble by both 3 and 5 then print "FizzBuzz"

# Write your code here 👇
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)
'''
# DAY 5 Project: Password Generator

#Checklist:
#1. Greeting
#2. Ask how many letters in pw?
#3. Ask how many symbols in pw?
#4. Ask how many numbers in pw?

#create lists and varaibles and define the variable that generates the password
import string
import random

def generate_password(num_letters, num_symbols, num_numbers):
    letters = list(string.ascii_lowercase)
    symbols = list("!@#$%^&*()-_+=[]{};:,.<>/?")
    numbers = list(range(10))

# empty list to store password
    password = []

#generate randoms
    password.extend(random.sample(letters, num_letters))
    password.extend(random.sample(numbers, num_numbers))
    password.extend(random.sample(symbols, num_symbols))

#combine and shuffle the three types of lists
    random.shuffle(password)
    
#convert to string to display to user.
#the map function applies the string to each element in the empty pw list
#the join method that concatenates the elements to a sigle, readable string
    password_string = ''.join(map(str, password))
    return password_string
    
    
#Input data and display user response
print("PyPassword Generator")
num_letters = int(input("How many letters would you like in your password? "))
print(num_letters)
num_symbols = int(input("How many symbols would you like in your passwrod? "))
print(num_symbols)
num_numbers = int(input("How many numbers would you like in your password? "))
print(num_numbers)

#generate pw from user data and print
password = generate_password(num_letters, num_symbols, num_numbers)
print("Your requested password is:", password)