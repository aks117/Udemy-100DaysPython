# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

namesCount = len(names)
randomNameIndex = random.randint(0, namesCount-1)

print(f"{names[randomNameIndex]} is going to buy the meal today!")