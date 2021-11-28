rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

options = [rock, paper, scissors]
optionNames = ["ROCK", "PAPER", "SCISSORS"]

choice = int(input("What do you choose? (Type 0 for rock, 1 for paper or 2 for scissiors)\n"))

programChoice = random.randint(0,2)

if (choice == 0):
  print("You : \n-----------------------------\n" + optionNames[choice])
  print (options[0] + "\n")
  print("-----------------------------\nOpponent : \n-----------------------------\n" + optionNames[programChoice] )

  if (programChoice == 0):
    print (options[0] + "\n")
    print("-----------------------------\n")
    print("It's a draw.")

  elif (programChoice == 1):
    print (options[1] + "\n")
    print("-----------------------------\n")
    print("You Lose.")

  else :
    print (options[2] + "\n")
    print("-----------------------------\n")
    print("You Win!")

elif (choice == 1) :
  print("You : \n-----------------------------\n" + optionNames[choice])
  print (options[1] + "\n")
  print("-----------------------------\nOpponent : \n-----------------------------\n" + optionNames[programChoice] )

  if (programChoice == 0):
    print (options[0] + "\n")
    print("-----------------------------\n")
    print("You Win!")

  elif (programChoice == 1):
    print (options[1] + "\n")
    print("-----------------------------\n")
    print("It's a draw.")

  else :
    print (options[2] + "\n")
    print("-----------------------------\n")
    print("You Lose.")

elif ( choice == 2) :
  print("You : \n-----------------------------\n" + optionNames[choice])
  print (options[2] + "\n")
  print("-----------------------------\nOpponent : \n-----------------------------\n" + optionNames[programChoice] )

  if (programChoice == 0):
    print (options[0] + "\n")
    print("-----------------------------\n")
    print("You Lose.")

  elif (programChoice == 1):
    print (options[1] + "\n")
    print("-----------------------------\n")
    print("You Win!.")

  else :
    print (options[2] + "\n")
    print("-----------------------------\n")
    print("It's a draw.")

else :
  print("Invalid input.")
