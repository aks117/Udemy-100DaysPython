def turnRight() :
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal() :
    if front_is_clear() :
        move()
    elif wall_in_front() :
        turn_left()
        while not right_is_clear() :
            move()
        turnRight()
        move()
        turnRight()
        while not wall_in_front():
            move()
        turn_left()
        