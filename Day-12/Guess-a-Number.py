import random
from art import logo

def returnRandomNumber() :
  """This function returns a random number between 1 and 100 (Both included)."""
  return random.randint(1, 100)

def guessingGame () :
  print (logo)
  
  number = returnRandomNumber()
  selectDifficulty = input("Select Difficulty : (Easy / Hard)\n").lower()

  if selectDifficulty == "hard" :
    chances = 5
    print (f"You chose HARD difficulty.\nYou have {chances} chances to guess the number.")
  else :
    chances = 10
    print (f"You chose EASY difficulty.\nYou have {chances} chances to guess the number.")

  while chances != 0 :
    guess = int(input("Guess a number : \n"))

    if (number == guess) :
      print(f"The number is {number}\nCorrect Guess.\nYou WIN!")
      break
    elif (number > guess) :
      print ("Guess is too Low.")
    else :
      print ("Guess is too High.")

    chances -= 1

    if (chances == 0) :
      print (f"You have {chances} remaining.\nThe number was {number}\nYou Lose.")
    else :
      print (f"You have {chances} remaining.\nGuess another number.")  


if __name__ == "__main__" :
  guessingGame()