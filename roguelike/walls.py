class Wall(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def ascii(self):
        return '#'
    def update(self, grid):
        grid.place_obj(self)
