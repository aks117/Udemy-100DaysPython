# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
sum = 0
for height in student_heights :
  sum += height
  # print(sum)
  count += 1
  # print(count)

averageHeight = round(sum / count)

print (averageHeight)