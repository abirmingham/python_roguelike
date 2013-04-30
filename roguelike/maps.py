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

