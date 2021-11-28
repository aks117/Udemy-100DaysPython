#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# print("Simple Password")

# password = ""

# for number in range (1, nr_letters + 1) :
#   randomAlphabet = random.randint(0, 51)
#   password = password + letters[randomAlphabet]

# for number in range (1, nr_symbols + 1) :
#   randomSymbol = random.randint(0, 8)
#   password = password + symbols[randomSymbol]

# for number in range (1, nr_numbers +1) :
#   randomNumber = random.randint(0, 9)
#   password = password + numbers[randomNumber]

# print("\n\n" + password + "\n\n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# print("Complex Password")

listOfLists = [letters, numbers, symbols]
passwordList = []

# for number in range (1, nr_letters + 1) :
#   randomListChooser = random.randint(0,2)

#   if (randomListChooser == 2) and (nr_symbols > 0) :
#     randomSymbol = random.randint(0, 8)
#     passwordComplex == passwordComplex + listOfLists[2][randomSymbol]
#     nr_symbols -= 1

#   elif (randomListChooser == 1) and (nr_numbers > 0) :
#     randomNumber = random.randint(0, 9)
#     passwordComplex = passwordComplex + listOfLists[1][randomNumber]
#     nr_numbers -= 1

#   else :
#     randomAlphabet = random.randint(0,25)
#     passwordComplex = passwordComplex + listOfLists[0][randomAlphabet]

for char in range (1, nr_letters + 1) :
  passwordList += random.choice(letters)

for char in range (1, nr_symbols + 1) :
  passwordList += random.choice(symbols)

for char in range (1, nr_numbers + 1) :
  passwordList += random.choice(numbers)

# print (passwordList)
random.shuffle(passwordList)
# print(passwordList)

password = ""

for char in passwordList :
  password += char

print(f"Your Password is {password}")
