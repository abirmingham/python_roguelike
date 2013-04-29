import random
import curses
import time

WIDTH  = 20
HEIGHT = 15
FPS    = 60
SLEEP_TIME = 1.0/FPS

class Grid():
    def __init__(self, width, height):
        self.EMPTY = -1
        self.data = [ [self.EMPTY for j in range(width)] for i in range(height) ]

    def is_coord_empty(self, x, y):
        return self.data[y][x] == self.EMPTY

    def fetch_obj(self, x, y):
        return self.data[y][x]

    def place_obj(self, obj):
        self.data[obj.y][obj.x] = obj

    def move_obj(self, obj, moveX, moveY):
        newX, newY = obj.x + moveX, obj.y + moveY

        if self.is_coord_empty(newX, newY):
            self.data[obj.y][obj.x] = self.EMPTY
            obj.x, obj.y = newX, newY
            self.place_obj(obj)

    def as_list(self):
        return self.data

    def draw(self, screen):
        y = 0
        for horizontal in self.data:
            screen.addstr(y, 0, ''.join([ ' ' if obj == self.EMPTY else obj.ascii() for obj in horizontal ]))
            screen.refresh()
            y += 1

class Enemy():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.idle_counter = 1
        self.asciiChar = 'T'

    def ascii(self):
        return self.asciiChar

    def update(self, grid):
        self.idle_counter += 1;

        if self.idle_counter % 120 == 0:
            self.idle_counter = 1
            movex, movey = 0, 0

            for x in random.sample([-1, 0, 1], 3):
                for y in random.sample([-1, 0, 1], 3):
                    if x == 0 and y == 0:
                        continue
                    else:
                        if isinstance(grid.fetch_obj(self.x + x, self.y + y), Player):
                            # attack
                            self.asciiChar = '!'
                            break
                        elif grid.is_coord_empty(self.x + x, self.y + y):
                            movex, movey = x, y

            grid.move_obj(self, movex, movey)

class Player():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def ascii(self):
        return 'A'

    def update(self, grid):
        if self.x_move or self.y_move:
            grid.move_obj(self, self.x_move, self.y_move)

class Wall():
    def __init__(self, x, y):
        self.x, self.y = x, y
    def ascii(self):
        return '#'
    def update(self, grid):
        grid.place_obj(self)

def main(screen):
    screen.nodelay(1)

    grid         = Grid(WIDTH, HEIGHT)
    player       = Player(1, 1)
    game_objects = build_walls()
    game_objects.append(player)

    game_objects.append(Enemy(5, 5)) # temp

    for obj in game_objects:
        grid.place_obj(obj)

    while (True):
        start_time = time.time()
        capture_input(screen, grid, player);

        for obj in game_objects:
            obj.update(grid)

        grid.draw(screen)
        time.sleep(SLEEP_TIME - (time.time() - start_time))

def build_walls():
    return [ Wall(x, y)
            for x in range(WIDTH)
            for y in range(HEIGHT)
            if x == 0 or x == (WIDTH-1)
            or y == 0 or y == (HEIGHT-1) ]

def capture_input(screen, grid, player):
    key = screen.getch()
    player.x_move = 0
    player.y_move = 0

    if key == curses.KEY_LEFT:
        player.x_move = -1
    elif key == curses.KEY_RIGHT:
        player.x_move = 1
    elif key == curses.KEY_UP:
        player.y_move = -1
    elif key == curses.KEY_DOWN:
        player.y_move = 1

curses.wrapper(main)
