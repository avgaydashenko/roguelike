import utils
from objects.player import Player
from objects.mob import Mob
from objects.wall import Wall

def init_map():
    map = {}
    creatures = []
    mapfile = open('map')

    y = 0
    for line in mapfile:
        x = 0
        for ch in line:
            if ch == utils.OBJ_WALL:
                map[x,y] = Wall(x, y)
            elif ch == utils.OBJ_PLAYER:
                player = Player(x, y)
                creatures.append(player)
            elif ch == utils.OBJ_MOB:
                creatures.append(Mob(x, y))

            x += 1
        y += 1

    return player, creatures, map
