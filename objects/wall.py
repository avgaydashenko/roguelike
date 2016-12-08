import utils
from objects.object import Object


class Wall(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, utils.OBJ_WALL)