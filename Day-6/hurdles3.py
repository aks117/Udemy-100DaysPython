def turnRight() :
    turn_left()
    turn_left()
    turn_left()
       
def oneHurdle() :
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
    
while not at_goal() :
    if front_is_clear() :
        move()
    elif wall_in_front() :
        oneHurdle()
    