# Escaping the Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if not wall_on_right():
        turn_right()
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        move()
