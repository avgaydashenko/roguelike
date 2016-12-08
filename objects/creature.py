import libtcodpy as libtcod
from object import Object


class Creature(Object):
    def __init__(self, x, y, char):
        Object.__init__(self, x, y, char)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def clear(self):
        libtcod.console_put_char(0, self.x, self.y, ' ', libtcod.BKGND_NONE)
