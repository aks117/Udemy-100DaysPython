#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to bill calculator!")

billAmount = input("What was the total bill? $")
# print(type(billAmount))
billAmount = float(billAmount)

tipPercentage = input("How much tip would you like yo give? 10, 12, or 15? ")
tipPercentage = int(tipPercentage)

numOfPeople = input("How many people to split the bill? ")
numOfPeople = int(numOfPeople)

amountToBePaid = (((billAmount * (tipPercentage / 100)) + billAmount) / numOfPeople)

amountToBePaid = round(amountToBePaid, 2)
amountToBePaid = "{:.2f}".format(amountToBePaid)

print(f"Each person should pay ${amountToBePaid}")
