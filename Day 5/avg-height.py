# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
total_number = 0

for height in student_heights:
    total_height = total_height + height
    total_number = total_number + 1

avg_height = total_height / total_number
print(round(avg_height))

# student_total = len(student_heights)
# height_total = sum(student_heights)
# print(student_total)
# print(height_total)

