import random
from replit import clear
from art import logo, vs
from game_data  import data

def getRandDict () :
  """"Returns a random Dictionary from data."""
  return random.choice(data)

def compare(a, b, choice) :
  """Compares the follower count of both the parties and returns a boolean depending on user choice."""
  aFollowers = a["follower_count"]
  bFollowers = b["follower_count"]

  if aFollowers > bFollowers :
    if choice == "a" :
      return True
    else :
      return False
  else :
    if choice == "b" :
      return True
    else :
      return False


def HLgame() :
  a = getRandDict()
  score = 0
  askAnother = True

  while askAnother :
    clear()
    print (logo)
    print (f"Your Current Score is : {score}\n\n")
    b = getRandDict()
    
    while a == b :
      b = getRandDict()

    print (f"A :\nName : {a['name']}\t\tDescription : {a['description']}\t\tCountry : {a['country']}")
    print(vs)
    print (f"B :\nName : {b['name']}\t\tDescription : {b['description']}\t\tCountry : {b['country']}\n")

    choice = input("Who do you think has more followers? : A or B\n").lower()

    askAnother = compare(a, b, choice)

    if askAnother == True :
      if choice == "b" :
        a = b
      score += 1

    else :
      print (f"You guessed wrong!\nYour final score is {score}")
      
      if input("Do you want to play again? (Y / N)\n").lower() == "y" :
        HLgame()
      else :
        clear()
        print ("Thank You for Playing!")
  

if __name__ == "__main__" :
  HLgame()
