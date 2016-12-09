import libtcodpy as libtcod
import utils
import random
import initialization


def print_stats():
    x = utils.X_STATS
    for i in range(1, 4):
        if i <= player.health:
            libtcod.console_put_char(0, x, utils.Y_HEALTH, '+', libtcod.BKGND_NONE)
        else:
            libtcod.console_put_char(0, x, utils.Y_HEALTH, ' ', libtcod.BKGND_NONE)

        if i <= player.armour:
            libtcod.console_put_char(0, x, utils.Y_ARMOUR, '+', libtcod.BKGND_NONE)
        else:
            libtcod.console_put_char(0, x, utils.Y_ARMOUR, ' ', libtcod.BKGND_NONE)

        if i <= player.keys:
            libtcod.console_put_char(0, x, utils.Y_KEYS, '+', libtcod.BKGND_NONE)
        else:
            libtcod.console_put_char(0, x, utils.Y_KEYS, ' ', libtcod.BKGND_NONE)
        x += 2


def print_info():
    x = utils.X_MESSAGE
    for char in utils.MESSAGE_HEALTH:
        libtcod.console_put_char(0, x, utils.Y_HEALTH, char, libtcod.BKGND_NONE)
        x += 1

    x = utils.X_MESSAGE
    for char in utils.MESSAGE_ARMOUR:
        libtcod.console_put_char(0, x, utils.Y_ARMOUR, char, libtcod.BKGND_NONE)
        x += 1

    x = utils.X_MESSAGE
    for char in utils.MESSAGE_KEYS:
        libtcod.console_put_char(0, x, utils.Y_KEYS, char, libtcod.BKGND_NONE)
        x += 1

    print_stats()


def handle_keys():
    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ESCAPE:
        return True

    dx, dy = (0, 0)
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        dx, dy = (0, -1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        dx, dy = (0, 1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        dx, dy = (-1, 0)
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        dx, dy = (1, 0)

    if (player.x + dx, player.y + dy) not in map:
        player.move(dx, dy)
    elif map[player.x + dx, player.y + dy].char == utils.OBJ_DOOR and player.keys > 0:
        player.move(dx, dy)
        player.keys -= 1


libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT, 'roguelike')
libtcod.sys_set_fps(utils.LIMIT_FPS)

player, creatures, artifacts, map = initialization.init_map()

for coords in map:
    map[coords].draw()

for coords in artifacts:
    artifacts[coords].draw()

print_info()

while not libtcod.console_is_window_closed():

    print_stats()
    exit = handle_keys()

    for creature in creatures:
        if creature.char == utils.OBJ_MOB:
            dx, dy = random.randrange(-1, 2), random.randrange(-1, 2)
            if (creature.x + dx, creature.y + dy) not in map:
                creature.move(dx, dy)
                if abs(creature.x-player.x) < 2 and abs(creature.y-player.y) < 2:
                    if player.armour > 0:
                        player.armour -= 1
                    else:
                        player.health -= 1
        creature.draw()

    if (player.x, player.y) in artifacts:
        artifact = artifacts[(player.x, player.y)].char
        del artifacts[(player.x, player.y)]
        if artifact == utils.OBJ_ARMOR:
            player.armour = 2
        elif artifact == utils.OBJ_KEY:
            player.keys += 1
        elif artifact == utils.OBJ_GRAIL:
            exit = True

    if player.health == 0:
        exit = True

    libtcod.console_flush()

    for creature in creatures:
        creature.clear()

    if exit:
        break
