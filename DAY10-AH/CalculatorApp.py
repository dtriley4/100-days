# 1-19-2024 Alexander: Udemy Python / Time to complete project == 30 min
#Overview: Functions with Outputs


'''
functions with outputs syntax:

def my_function():
    result = 3 * 2
    return result

output = my_fuction() *gets replaced with "result" or the returned variable and can save to new variable
output would equal 6 in this function case


#functions with outputs example:
def format_name(f_name, l_name):   #changes name inputs into title case
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
formated_string = format_name("AleXANDeR", "NICHOLAS")
print(formated_string)
    

#multiple return values
def format_name(f_name, l_name):   #changes name inputs into title case
    if f_name == "" or l_name == "":
        return "You need to provide both first and last name." #adding an empty return for errors to exit function if someone user left an input blank
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))


#days in month auditorium exercise solution:
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days [month - 1]

#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)


#adding Docstrings: Must go after first line of "def" line using three quotioans """:
example:

def format_name(f_name, l_name):
    """Take a first and last name and format to return title case of name"""
    if f_name == "" or l_name == "":
        return "You need to provide both name inputs."
    formated_l_name = l_name.title()
    formated_f_name = f_name.title()
'''


#Project: Calculator App

#1. Ask and ask user for first integer
#2 Show and ask user to pick an operator
#3 Perform and show operation


#define operator funnctions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
    
def calculator():
    print("Python Calculator")
    print("Please select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input")
calculator()