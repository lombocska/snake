# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for
# exiting

import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


def GameOver():
    win.addstr(22, 70, "GAME OVER")
    win.refresh()
    time.sleep(3)


def appears_wall_vertical(x):
    for i in range(1, 21):
        win.addstr(i, x, "|", curses.color_pair(4))
        win.refresh()


x = randint(60, 80)


def appears_wall_horizontal(y):
    for i in range(1, 21):
        win.addstr(y, i, "-", curses.color_pair(4))
        win.refresh()

y = randint(10, 20)

# Choose mode
mode = int(input(
    "\nPress button of F11! :]\n\nWhich mode do you want to play:"
    "\n1: If snake crosses the boundaries, make it enter from the other side"
    "\n2: Exit if snake crosses the boundaries\n"))
difficulty = int(input(
    "\nOn which diffuculty would you like to play?\n1:Easy\n2:Medium\n3:Hard\n4:Insane\n"))
if difficulty == 1:
    speed = 100
elif difficulty == 2:
    speed = 60
elif difficulty == 3:
    speed = 25
elif difficulty == 4:
    speed = 15

# default settings :)
curses.initscr()
curses.start_color()
box = curses.newwin(45, 150, 0, 0)
box.border(0)
win = curses.newwin(43, 146, 1, 2)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)

# window.border([ls[, rs[, ts[, bs[, tl[, tr[, bl[, br]]]]]]]])
win.nodelay(1)
box.nodelay(1)


# colors definte
# def color of snake
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
# def colours
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
# set color of bgs
win.bkgd(" ", curses.color_pair(2))
box.bkgd(" ", curses.color_pair(3))
box.refresh()
score = 0
# Initializing values
key = KEY_RIGHT
timer = 0
timer2 = 0
# stuff of game
# Initial snake co-ordinates
snake = [[4, 10], [4, 9], [4, 8]]
# First food co-ordinates
food1 = [15, 20]
food2 = [30, 50]
# print
# Prints the food1
win.addch(food1[0], food1[1], '*')
# Prints the food2
win.addch(food2[0], food2[1], '*')
# thegameprocess
while key != 27:
    box.border(0)                                                  # While Esc key is not pressed
    win.border(0)
    # Printing 'Score' and
    win.addstr(0, 10, 'Score : ' + str(score) + ' ')
    win.addstr(0, 40, 'Time : ' + str(timer2) + ' ')
    # 'SNAKE' strings
    win.addstr(0, 70, ' SNAKE ')
    # Increases the speed of Snake as its length increases
    win.timeout(speed)
    # Previous key pressed
    prevKey = key
    event = win.getch()
    if event == KEY_DOWN and prevKey == KEY_UP:
        key == prevKey
    elif event == KEY_UP and prevKey == KEY_DOWN:
        key == prevKey
    elif event == KEY_LEFT and prevKey == KEY_RIGHT:
        key == prevKey
    elif event == KEY_RIGHT and prevKey == KEY_LEFT:
        key == prevKey
    elif event == -1:
        key = key
    else:
        key = event
    # Pause
    # If SPACE BAR is pressed, wait for another
    if key == ord(' '):
        # one (Pause/Resume)
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue
    # if the user is stupid
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
        key = prevKey
    # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
    # This is taken care of later at [1].
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
                     snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])
    # If snake crosses the boundaries, make it enter from the other side
    if mode == 1:
        if snake[0][0] == 0:
            snake[0][0] = 41
        if snake[0][1] == 0:
            snake[0][1] = 144
        if snake[0][0] == 42:
            snake[0][0] = 1
        if snake[0][1] == 145:
            snake[0][1] = 1
    # Exit if snake crosses the boundaries
    if mode == 2:
        if snake[0][0] == 0 or snake[0][0] == 44 or snake[0][1] == 0 or snake[0][1] == 149:
            GameOver()
            break
    if score == 5:
        appears_wall_vertical(x)

    if score == 10:
        appears_wall_horizontal(y)

    # Events of gameover
    if snake[0] in snake[1:]:
        GameOver()
        break

    if (snake[0][1] == x and snake[0][0] <= 20 and score >= 5):
        GameOver()
        break

    if (snake[0][0] == y and snake[0][1] <= 20 and score >= 10):
        GameOver()
        break

    if snake[0] == food1:                                            # When snake eats the food
        food1 = []
        score += 1
        while food1 == []:
            # Calculating next food's coordinates
            food1 = [randint(2, 41), randint(2, 146)]
            if food1 in snake:
                food1 = []
            if food1[0] == y and food1[1] <= 20:
                food1 = []
            if food1[0] <= 40 and food1[1] == x:
                food1 = []
        win.addch(food1[0], food1[1], '*')
    # When snake eats the food
    elif snake[0] == food2:
        food2 = []
        score += 1
        while food2 == []:
            # Calculating next food's coordinates
            food2 = [randint(2, 41), randint(2, 146)]
            if food2[0] == y and food2[1] <= 20:
                food2 = []
            if food2[0] <= 40 and food2[1] == x:
                food2 = []
            if food2 in snake:
                food2 = []
        win.addch(food2[0], food2[1], '*')
    else:
        # [1] If it does not eat the food, length decreases
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], 'x', curses.color_pair(3))
    win.addch(snake[1][0], snake[1][1], ' ', curses.color_pair(1))
    timer += speed/1000
    timer2 = int(timer)

curses.endwin()
print("\nScore:" + str(score))
