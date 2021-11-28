############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
numberOfCards = len(cards)

def blackjack():
  clear()
  print (logo)

  playerCards = []
  dealerCards = []

  for i in range (2):
    playerCards.append(random.choice(cards))
    dealerCards.append(random.choice(cards))

  print (f"Your cards are : {playerCards} - Current Score : {sum(playerCards)}\n ")
  print (f"Dealer's first card : [{dealerCards[1]}] \n")

  if (sum(dealerCards) == 21) :
    print (f"The Dealer's cards are {dealerCards} - Dealer's Score : {sum(dealerCards)}\nThe Dealer has a Blackjack.\nYouLose.")
  
  elif (sum(playerCards) > 21) :
    print (f"You got a Blackjack. : Your Score : {sum(playerCards)}\nYou Win!")
  
  else :

    if (input("Do you want to draw another card? (Y / N )\n").lower() == "y") :
      drawAnother = True
    else :
      drawAnother = False

    while drawAnother :
      playerCards.append(random.choice(cards))

      if playerCards[-1] == 11 and sum(playerCards) >21 :
        playerCards[-1] = 1

      print (f"Your cards are : {playerCards} - Current Score : {sum(playerCards)}\n ")
      print (f"Dealer's first card : [{dealerCards[1]}] \n")

      if (sum(playerCards) >= 21) :
        drawAnother = False
      
      elif input("Do you want to draw another card? (Y / N )\n").lower() == "y" :
        drawAnother == True

      else :
        drawAnother = False
     
    if (sum(dealerCards) < 16) :
      while (sum(dealerCards) < 16) :
        dealerCards.append(random.choice(cards))

        if dealerCards[-1] == 11 and sum(dealerCards) > 21 :
          dealerCards[-1] = 1
        
    if (sum(playerCards) > 21) :
      print (f"Your score is : {sum(playerCards)}\nIt's a BUST!\nYou Lose.")

    elif (sum(dealerCards) == 21) :
      print (f"Your cards are : {playerCards} - Your Score : {sum(playerCards)}\n ")
      print (f"Dealer's cards are : {dealerCards} - Dealer's Score : {sum(dealerCards)} \n")
      print ("Dealer has a Blackjack!\nYou Lose.")

    elif (sum(playerCards) == 21) :
      print (f"Your cards are : {playerCards} - Your Score : {sum(playerCards)}\n ")
      print (f"Dealer's cards are : {dealerCards} - Dealer's Score : {sum(dealerCards)} \n")
      print ("You have a Blackjack!\nYou Win!")
    
    elif (sum(dealerCards) > 21) or (sum(playerCards) > sum(dealerCards)) :
      print (f"Your cards are : {playerCards} - Your Score : {sum(playerCards)}\n ")
      print (f"Dealer's cards are : {dealerCards} - Dealer's Score : {sum(dealerCards)} \n")
      print ("You Win!")

    elif (sum(playerCards) == sum(dealerCards)) :
      print (f"Your cards are : {playerCards} - Your Score : {sum(playerCards)}\n ")
      print (f"Dealer's cards are : {dealerCards} - Dealer's Score : {sum(dealerCards)} \n")
      print ("It's a Draw.")

    else :
      print (f"Your cards are : {playerCards} - Your Score : {sum(playerCards)}\n ")
      print (f"Dealer's cards are : {dealerCards} - Dealer's Score : {sum(dealerCards)} \n")
      print ("You Lose.")  

  if input("Do you want to play another round? (Y / N)\n").lower() == "y" :
    blackjack()
      

if __name__ == "__main__" :
  if input("Do you wan to play Blackjack ? (Y / N)\n").lower() == "y" :
    blackjack()
  clear()
  print("Thank You for Playing!")