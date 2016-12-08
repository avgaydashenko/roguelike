import libtcodpy as libtcod


class Object:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

    def draw(self):
        libtcod.console_put_char(0, self.x, self.y, self.char, libtcod.BKGND_NONE)
