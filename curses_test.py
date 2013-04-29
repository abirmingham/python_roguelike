import curses
import time

WIDTH  = 20
HEIGHT = 15
FPS    = 60
SLEEP_TIME = 1.0/FPS

grid = []
player = { 'x': 2, 'y': 2 }

def main(screen):
    screen.nodelay(1)

    while (True):
        start_time = time.time()

        getInput(screen);
        updateGrid();
        draw(screen);

        time.sleep(SLEEP_TIME - (time.time() - start_time))

def getInput(screen):
    global player
    key = screen.getch()

    oldy = player['y']
    oldx = player['x']

    if key == curses.KEY_LEFT:
        player['x'] = player['x'] - 1
    elif key == curses.KEY_RIGHT:
        player['x'] = player['x'] + 1
    elif key == curses.KEY_UP:
        player['y'] = player['y'] - 1
    elif key == curses.KEY_DOWN:
        player['y'] = player['y'] + 1

    # Clamp
    if (len(grid) and grid[player['y']][player['x']] == '#'):
        player['y'] = oldy
        player['x'] = oldx

def updateGrid():
    global grid
    grid = ['#' * WIDTH]

    for i in range(HEIGHT-2):
        grid.append('#' + (' ' * (WIDTH-2)) + '#')

    grid.append('#' * WIDTH)

def draw(screen):
    for y in range(len(grid)):
        # Grid
        screen.addstr(y, 0, grid[y])

        # Player
        screen.addstr(player['y'], player['x'], 'A')

        screen.refresh()

curses.wrapper(main)
