# 1-3-2024 Alexander: Udemy Python / Time to complete project == 30 mins
# Overview:Conditional Statements, Logical Operators, Code Blocks and Scope

# DAY 3 Project: Choose your own adventure game

#Checklist:
#1. Create a choice based mini game
#2. Use else elif or if statments
#3. Create greeting

print('''           _......._
       .-'.'.'.'.'.'.`-.
     .'.'.'.'.'.'.'.'.'.`.
    /.'.'               '..
    |.'    _.--...--._     |
    \    `._.-.....-._.'   /
    |     _..- .-. -.._   |
 .-.'    `.   ((@))  .'   '.-.
( ^ \      `--.   .-'     / ^ )
 \  /         .   .       \  /
 /          .'     '.  .-    .
( _.\    \ (_`-._.-'_)    /._\)
 `-' \   ' .--.          / `-'
     |  / /|_| `-._.'\   |
     |   |       |_| |   /-.._
 _..-\   `.--.______.'  |
      \       .....     |
       `.  .'      `.  /
         \           .'
          `-..___..-`          
''')
          
print("The Gauntlets of Boolean")
print("Will you survive and secure the Amulet of Truth?")

choice1 = (input("You have found yourself inside a dungeon with an awful smell. There are two hallways. Do you want to go left or right? Type 'left' or 'right'. "))
if choice1 == "left":
    print("Your steps lead you into the dark. A blast of fire from the stone walls melts your face. You are now a dead, and add to the wretched smell.")
if choice1 == "right": #continue onward
    choice2 = input("You find yourself walking into the dark, but you can see the dim glow of a torch down the hall. You get to the torch. Do you pick it up or continue deeper into the shadows? Type 'torch' or 'continue'. ")
    if choice2 == "continue":
        choice3 = input("You travel through the shadows and find yourself in a library. There are three oak doors. One small, one medium, and one large. Which door do you choose to open? Type 'small', 'medium', or 'large'. ")
        if choice3 == "small":
            print("You open the small door and find a glowing amulet. You put it on and you are now all-knowing. Nothing can stop you.")
        elif choice3 == "medium":
            print("You open the medium sized door and a pack of wolves lunge at you. You are now dead, and make the wolves happy.")
        elif choice3 == "large":
            print("You open the large door and Cyclopse Boolean is startled. He picks you up and eats you. *Nom *Nom *Nom, you are now dead.")
        else:
            print("Your choice is cowarldy, and you leave empty handed.")
    else:
        print("As you pull the torch, it releases a lever and you fall into an opening in the floor. You are dead, and will add to the horrible smell.")