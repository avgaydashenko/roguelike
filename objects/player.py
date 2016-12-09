import utils
from objects.creature import Creature


class Player(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, x, y, utils.OBJ_PLAYER)
        self.health = 3
        self.armour = 0
        self.keys = 0
