# 1-1-2024 Alexander: Udemy Python / Time to complete project <= 30 mins
# Overview: data types, numbers, operations, type conversion, f-strings

# DAY 2 Project: Tip Calculator

#Checklist:
#1. Greeting
#2. Round answers to 2 decimal places
#3. Ask bill total
#4. ASk tip percentage
#5. Ask number of people splitting bill
#6. Return what each person should pay

print("Easy Tip Calculator")
#input data
bill = float(input("What is the bill total? $"))
tip = int(input("What percentage tip would you like to give? %"))
people = int(input("How many people are splitting the bill? "))

#math time
total_bill = tip / 100 * bill + bill
individual_bill = total_bill / people
comfy_bill = round(individual_bill, 2)
comfy_bill = "{:.2f}".format(comfy_bill) #used to format and reveal results that end in a 0 

print(f"Each person owes: ${comfy_bill} towards the bill!")
