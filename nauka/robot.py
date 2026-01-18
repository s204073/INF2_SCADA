
class Robot:
    def __init__(self, x, y, limit_x, limit_y):
        self.x = x
        self.y = y
        self.limit_x = limit_x
        self.limit_y = limit_y
    def ruch(self, dx, dy):
        nowe_x = self.x + dx
        nowe_y = self.y + dy

        if 0 <= nowe_x < self.limit_x:
            self.x = nowe_x

        if 0 <= nowe_y < self.limit_y:
            self.y = nowe_y



