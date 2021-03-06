#it is a normal snake game in python 2.7
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN   #for controlling your snake 
from random import randint


curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT                                                    # Initializing the values
score = 0

snake = [[4,10], [4,9], [4,8]]                                     # the inisial co-ordinates of the snake
food = [10,20]                                                     # First food co-ordinates

win.addch(food[0], food[1], '*')                                   # shows the food

while key != 27:                                                   # the game will continue untill esc is pressed
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
    win.addstr(0, 27, ' SNAKE ')                                   # 'SNAKE' strings
    win.timeout(150 - (len(snake)/5 + len(snake)/10)%120)          # Increases the speed of Snake as its length increases
    
    prevKey = key                                                  # Previous key pressed
    event = win.getch()
    key = key if event == -1 else event 


    if key == ord(' '):                                            #it will pause if the space button is pressed
        key = -1                                                   # one (Pause/Resume)
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:    
        key = prevKey


    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # If snake crosses the boundaries, make it enter from the other side
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

    #if you want to game over when the snake crosses the border uncomment it
    #if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break

    # If snake runs over itself
    if snake[0] in snake[1:]: break

    
    if snake[0] == food:                                            
        food = []
        score += 1
        while food == []:
            food = [randint(1, 18), randint(1, 58)]                 
            if food in snake: food = []
        win.addch(food[0], food[1], '*')
    else:    
        last = snake.pop()                                        
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], 'AYAN')
    
curses.endwin()
