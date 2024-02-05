# 1-31-2024 Alexander: Udemy Python / Time to complete project == 
# Overview: Debugging

# Tips for finding bugs in your code

######DEBUGGING######


# 1. Describe the problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# The for-loop is trying to loop through the range of numbers from 1 - 20 and when i is eqaul to 20, the funciton wants to print the string.
# However, it seems that the range in the code above will not include 20 due to syntax. You can make the range (1, 21)
# Solution would be to change 20 to 21 since the last number in the range is omitted and we want to include the number 20


# 2. Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# The bug happens when the dice num is randonly chosen to be 6. Becaue we are wokrig with a list, and they start to index at 0. So the list really has items 0 1 2 3 4 5.
# Solution would be to make the randit range 0 to 5 to work properly with the list.


# 3. Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# The bug is that if your year is one of the years that binds to the print statment parameters, nothing will happen.
# This is due to the improper use of operators, and the if/elif statement should be written to inlcude the cut-off years as input options.
# Solution would be to use >= in the elif parameter


# 4. Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# The first noticable bug is the lack of indentation for the if statement. There is another error beaucse the input should return the string as an int. And lastly, the print statement isnt including a f string syntax.
# Solution would be to indent the if statement, then make the input return as an int to perform the math operation, and also to turn the print statement into an f string.

# 5. Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# Using the print function can help you identify the issues.
# Print the two variables to see where the error is produced and you can find the error is in the words_per_page variable
# Solution is that the word_per_page variable should be one equal sign = rather than the two == in the bugged code 


# 6. Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
# Debuggers are programs that can help you identify bugs
# Some examples are browser based like pythontutor.com and built in application based like in the Thonny text editor
# The bug in the code above is that b_list produces a list with only 1 value which is equal to the last value of the new item.
# You can assign breakpoints in the code using pythontutor.com to assign where the problem occurs and for the program to stop running at that line of code.
# Solution is to indent the b_list.append(new_item) so that it is perfromed inside the loop.
  
