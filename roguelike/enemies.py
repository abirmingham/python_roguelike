import random

class Enemy(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.idle_counter = 1
        self.asciiChar = 'T'

    def ascii(self):
        return self.asciiChar

    def alignment(self):
        return 'evil'

    def is_hostile(self, target):
        return target.alignment() != 'evil'

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
                        if grid.is_coord_empty(self.x + x, self.y + y):
                            movex, movey = x, y
                        elif self.is_hostile(grid.fetch_obj(self.x + x, self.y + y)):
                            # attack
                            self.asciiChar = '!'
                            break

            grid.move_obj(self, movex, movey)

