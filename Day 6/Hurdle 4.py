# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     if wall_in_front():
#         turn_left()
#         if wall_in_front():
#             turn_left()
#             move()
#         else:
#             move()
#     elif wall_on_right():
#         turn_right()
#         turn_left()
#         if wall_in_front():
#             turn_left()
#             if wall_in_front():
#                 turn_left()
#                 move()
#         else:
#             move()
#     elif right_is_clear():
#         turn_right()
#         move()
# while at_goal() != True:
#     jump()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
