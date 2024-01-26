# 1-7-2024 Alexander: Udemy Python / Time to complete project == 30 mins
# Overview: Functions, Code Blocks, While Loops

'''
functions typically use ()
ex: 
num_char = len("Hello") # gets character length of string
print(num_char) #executes function inside ()

defining our own functions with def function
ex:
def my_function()"
    XXXX
    XXXX
my_function() - #used to call or execute function

#For loops vs while loops
#for loops 
    for item in list_of_items:
        #do something to each item

for number in rangs(a, b):
    print(number)
    
#while loops
    while something_is_true:
        #do something repeatedly

ex for while loop: hurdle game (Reeborg)

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()   #already defined variable using "def" function
    number_of_hurdles -= 1    #counts down number of hurdles from first variable




hurdle game: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
####hurdle exercise 2: evenly spaced hurdles and random goal finish line###
#my code to solution:
def turn_right():   #defines variable for a right turn
    turn_left()
    turn_left()
    turn_left()    
def jump():         #defines variable for hurdlejump
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while at_goal() != True:  #runs the jump() function until the condition becomes true
    jump()
    
#similarly
while not at_goal():
    jump()
    
    
    
    
###hurdle example 3: random placed hurdles to goal finish line###
#my code to solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()    
def jump():             #have to elimate the move() function from the begingin of the jump() function so the while / if function bellow can determine if there is a hurdle in front of the moving object or not
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
   
        
###hurdle 4 exercise: random hurdle heights
#my code to solution:
def turn_right():
    turn_left()
    turn_left()
    turn_left()    
def jump():
    while wall_on_right():
       if not is_facing_north():
        turn_left()
       else:
        move()
    while not wall_on_right():
        if right_is_clear():
            turn_right()
            move()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()




#final project for day6: Escape the maze on" https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#my code to solution:
def turn_right():
    turn_left()
    turn_left()
    turn_left()    
def jump():
    while wall_on_right():
       if not is_facing_north():
        turn_left()
       elif not front_is_clear():
            turn_left()
       else:
        move()
    while not wall_on_right():
        if right_is_clear():
            turn_right()
            if at_goal():
                done()
            move()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
'''
