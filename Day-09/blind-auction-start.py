from replit import clear
#HINT: You can call clear() to clear the output in the console.

auctionDictionary = {}

from art import logo

auction = True
highestBid = 0

while auction :
  print (logo)

  name = input("What's your name?\t")
  bid = int(input("What's your bid?\t$"))

  auctionDictionary[name] = bid

  if (highestBid < bid) :
    highestBid = bid
    highestBidder = name

  again = input("Any more bidders? (Yes/No)\t").lower()

  if again == "no" :
    auction = False

  clear()

print(f"The highest bid is ${highestBid} by {highestBidder}.")

