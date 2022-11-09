# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"


###my solution
# reversed_position = position[::-1]
# print(len(reversed_position))

# print(position[1] + position[0])
# row 1
# if position[1] == "1":
#     if position[0] == "1":
#         row1[0] = 'X'
#     elif position[0] == "2":
#         row1[1] = 'X'
#     elif position[0] == "3":
#         row1[2] = 'X'

# # row 2
# if position[1] == "2":
#     if position[0] == "1":
#         row2[0] = 'X'
#     elif position[0] == "2":
#         row2[1] = 'X'
#     elif position[0] == "3":
#         row2[2] = 'X'

# # row 3
# if position[1] == "3":
#     if position[0] == "1":
#         row3[0] = 'X'
#     elif position[0] == "2":
#         row3[1] = 'X'
#     elif position[0] == "3":
#         row3[2] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

