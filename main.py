import curses
import time

import roguelike.maps
import roguelike.enemies
import roguelike.players
import roguelike.walls

def main(screen):
    ### Config #############
    width  = 80
    height = 40
    fps    = 60
    sleep_time = 1.0/fps
    ########################

    screen.nodelay(1)

    grid         = roguelike.maps.Grid(width, height)
    player       = roguelike.players.Player(1, 1)
    game_objects = build_walls(width, height)
    game_objects.append(player)

    game_objects.append(roguelike.enemies.Enemy(5, 5)) # TBD monster maker

    for obj in game_objects:
        grid.place_obj(obj)

    while (True):
        start_time = time.time()
        capture_input(screen, grid, player);

        for obj in game_objects:
            obj.update(grid)

        grid.draw(screen)
        time.sleep(sleep_time - (time.time() - start_time))

def build_walls(width, height):
    return [ roguelike.walls.Wall(x, y)
            for x in range(width)
            for y in range(height)
            if x == 0 or x == (width-1)
            or y == 0 or y == (height-1) ]

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
