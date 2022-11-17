def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    if wall_in_front():
        turn_left()
        if wall_in_front():
            turn_left()
            move()
        else:
            move()
    elif wall_on_right():
        turn_right()
        turn_left()
        if wall_in_front():
            turn_left()
            if wall_in_front():
                turn_left()
                move()
        else:
            move()
    elif right_is_clear():
        turn_right()
        move()
while at_goal() != True:
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
