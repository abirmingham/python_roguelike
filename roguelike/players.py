class Player():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def ascii(self):
        return 'A'

    def update(self, grid):
        if self.x_move or self.y_move:
            grid.move_obj(self, self.x_move, self.y_move)
