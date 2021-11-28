print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice = input(
    "You're at the entrance of a cave with two ways inside - Left and Right. Which one do you go? (Left/Right)\n "
)
choice = choice.lower()

if (choice == "right"):
    print("There is a hungry tiger in there.")
    print("GAME OVER")

elif (choice == "left"):
    print("You walk till you reach a lake.\nYou need to cross the lake.")
    choice = input("Do you swim across the lake or do you wait for a boat? (Swim/Wait)\n")
    choice = choice.lower()

    if (choice == "swim") :
      print("There is a killer shark in the lake. You tried your best to survive but ...\nGAME OVER!")

    elif (choice == "wait") :
      print("You've safely crossed the lake.\nThere are three houses infront of you.")
      choice = input("Which house do you go to? (Red/Blue/Green)")
      choice = choice.lower()
      
      if (choice == "red") :
        print("There was supa hot fire in the house.\nHe killed you with his rap :)\nGAME OVER!")

      elif (choice == "blue") :
        print("You found a map to India.\nYAY! Team Blue\nYOU WIN!!! ")

      elif (choice =="green") :
        print("Green! Seriously!??\nWell, Welcome to Goblin's house.\nGAME OVER!")

      else :
        print("Invalid input.\nGAME OVER!")

    else :
      print("Invalid input.\nGAME OVER!")

else :
  print("Invaild input.\nGAME OVER!")