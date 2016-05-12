# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting

import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

def GameOver():
    win.addstr(22, 70, "GAME OVER")
    win.refresh()
    time.sleep(3)

# Choose mode
mode = int(input(" \n" "Press button of F11! :]  \n" " \n" "Which mode do you want to play: \n" "1: If snake crosses the boundaries, make it enter from the other side \n" "2: Exit if snake crosses the boundaries \n" ))
difficulty = int(input("\nOn which diffuculty would you like to play?\n1:Easy\n2:Medium\n3:Hard\n4:Insane\n"))
if difficulty == 1:
    speed = 100
elif difficulty == 2:
    speed = 60
elif difficulty == 3:
    speed = 25
elif difficulty == 4:
    speed = 15

#default settings :)
curses.initscr()
curses.start_color()
win = curses.newwin(45, 150, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(1)
win.nodelay(1)


#colors definte
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)         #def color of snake
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)         #def color of background
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
win.bkgd(" ", curses.color_pair(2))                                 # set color of bg

for i in range (0,21):
    win.addstr(i,80,"|", curses.color_pair(4))
    win.refresh()

for i in range (0,21):
    win.addstr(10,i,"-", curses.color_pair(4))
    win.refresh()

key = KEY_RIGHT                                                    # Initializing values
score = 0

#stuff of game
snake = [[4,10], [4,9], [4,8]]                                     # Initial snake co-ordinates
food1 = [15,20]                                                     # First food co-ordinates
food2 = [30,50]

#print
win.addch(food1[0], food1[1], '*')                                   # Prints the food1
win.addch(food2[0], food2[1], '*')                                   # Prints the food2

#thegameprocess
while key != 27:                                                   # While Esc key is not pressed
    win.border(0)
    win.addstr(0, 10, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
    win.addstr(0, 70, ' SNAKE ')                                   # 'SNAKE' strings
    win.timeout(speed)                                               # Increases the speed of Snake as its length increases

    prevKey = key                                                  # Previous key pressed
    event = win.getch()
    if event == KEY_DOWN and prevKey == KEY_UP:
        key ==prevKey
    elif event == KEY_UP and prevKey == KEY_DOWN:
        key ==prevKey
    elif event == KEY_LEFT and prevKey == KEY_RIGHT:
        key ==prevKey
    elif event == KEY_RIGHT and prevKey == KEY_LEFT:
        key ==prevKey
    elif event == -1:
        key = key
    else: key = event

    #Pause
    if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
        key = -1                                                   # one (Pause/Resume)
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    #if the user is stupid
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
        key = prevKey




    # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
    # This is taken care of later at [1].
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # If snake crosses the boundaries, make it enter from the other side
    if mode == 1:
        if snake[0][0] == 0: snake[0][0] = 43
        if snake[0][1] == 0: snake[0][1] = 148
        if snake[0][0] == 44: snake[0][0] = 1
        if snake[0][1] == 149: snake[0][1] = 1

    # Exit if snake crosses the boundaries
    if mode == 2:
        if snake[0][0] == 0 or snake[0][0] == 44  or snake[0][1] == 0 or snake[0][1] == 149:
            GameOver()
            break

    # Events of gameover
    if snake[0] in snake[1:]:
        GameOver()
        break

    if (snake [0][1] == 80 and snake[0][0] <= 20):
        GameOver()
        break

    if (snake[0][0] == 10 and snake[0][1] <= 20):
        GameOver()
        break


    if snake[0] == food1:                                            # When snake eats the food
        food1 = []
        score += 1
        while food1 == []:
            food1 = [randint(1, 43), randint(1, 148)]                 # Calculating next food's coordinates
            if food1 in snake: food1 = []
            if food1[0] == 10 and food1[1] <= 20: food1 = []
            if food1[0] <= 40 and food1[1] == 20: food1 = []
        win.addch(food1[0], food1[1], '*')
    elif snake[0] == food2:                                            # When snake eats the food
        food2 = []
        score += 1
        while food2 == []:
            food2 = [randint(1, 43), randint(1, 148)]                 # Calculating next food's coordinates
            if food2 == 10 and food2 <= 20: food1 = []
            if food2 in snake: food2 = []
        win.addch(food2[0], food2[1], '*')
    else:
        last = snake.pop()                                          # [1] If it does not eat the food, length decreases
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], 'x', curses.color_pair(3))
    win.addch(snake[1][0], snake[1][1], ' ', curses.color_pair(1))

curses.endwin()
print("\nScore:" + str(score))
