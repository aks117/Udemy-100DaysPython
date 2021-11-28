# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

countTrue = 0
combinedName = name1 + name2
combinedName = combinedName.lower()

countTrue += combinedName.count("t")
countTrue += combinedName.count("r")
countTrue += combinedName.count("u")
countTrue += combinedName.count("e")

# print(countTrue)

countLove = 0

countLove += combinedName.count("l")
countLove += combinedName.count("o")
countLove += combinedName.count("v")
countLove += combinedName.count("e")

# print(countLove)

score = int(str(countTrue) + str(countLove))
print(score)

if score < 10 or score > 90 :
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50 :
  print(f"Your score is {score}, you are alright together.")
else :
  print(f"Your score is {score}")
