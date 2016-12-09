import utils
from objects.player import Player
from objects.object import Object
from objects.creature import Creature


def init_map():

    map = {}
    artifacts = {}
    creatures = []
    mapfile = open('map')

    y = 0
    for line in mapfile:
        x = 0
        for ch in line:
            if ch == utils.OBJ_WALL or ch == utils.OBJ_DOOR:
                map[x,y] = Object(x, y, ch)
            elif ch == utils.OBJ_PLAYER:
                player = Player(x, y)
                creatures.append(player)
            elif ch == utils.OBJ_MOB:
                creatures.append(Creature(x, y, utils.OBJ_MOB))
            elif ch != ' ':
                artifacts[x,y] = Object(x, y, ch)

            x += 1
        y += 1

    return player, creatures, artifacts, map
