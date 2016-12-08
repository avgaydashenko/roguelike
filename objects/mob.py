import utils
from objects.creature import Creature


class Mob(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, x, y, utils.OBJ_MOB)