import libtcodpy as libtcod
import utils
import random
import initialization


def print_stats():
    x, y = utils.STATS_HEALTH_COORDS
    for i in range(player.health):
        libtcod.console_put_char(0, x, y, '+', libtcod.BKGND_NONE)
        x += 2

    x, y = utils.STATS_ARMOUR_COORDS
    for i in range(player.armour):
        libtcod.console_put_char(0, x, y, '+', libtcod.BKGND_NONE)
        x += 2

    x, y = utils.STATS_SPEED_COORDS
    for i in range(player.speed):
        libtcod.console_put_char(0, x, y, '+', libtcod.BKGND_NONE)
        x += 2


def print_info():
    x, y = utils.MESSAGE_HEALTH_COORDS
    for char in utils.MESSAGE_HEALTH:
        libtcod.console_put_char(0, x, y, char, libtcod.BKGND_NONE)
        x += 1

    x, y = utils.MESSAGE_ARMOUR_COORDS
    for char in utils.MESSAGE_ARMOUR:
        libtcod.console_put_char(0, x, y, char, libtcod.BKGND_NONE)
        x += 1

    x, y = utils.MESSAGE_SPEED_COORDS
    for char in utils.MESSAGE_SPEED:
        libtcod.console_put_char(0, x, y, char, libtcod.BKGND_NONE)
        x += 1

    print_stats()


def handle_keys():
    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ESCAPE:
        return True

    dx, dy = (0, 0)
    if libtcod.console_is_key_pressed(libtcod.KEY_UP): dx, dy = (0, -1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN): dx, dy = (0, 1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT): dx, dy = (-1, 0)
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT): dx, dy = (1, 0)

    if (player.x + dx, player.y + dy) not in map:
        player.move(dx, dy)


libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT, 'roguelike')
libtcod.sys_set_fps(utils.LIMIT_FPS)

player, creatures, map = initialization.init_map()

for coords in map:
    map[coords].draw()

print_info()

while not libtcod.console_is_window_closed():

    print_stats()

    for creature in creatures:
        if creature.char == utils.OBJ_MOB:
            dx, dy = random.randrange(-1, 2), random.randrange(-1, 2)
            if (creature.x + dx, creature.y + dy) not in map:
                creature.move(dx, dy)
        creature.draw()

    libtcod.console_flush()

    for creature in creatures:
        creature.clear()

    exit = handle_keys()
    if exit:
        break