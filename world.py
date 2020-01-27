_world = {}
starting_position = (0, 0)


def load_tiles():
    """ Parses a file that describes the world space into the
        _world object """
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            if tile_name == 'X':
                _world[(x, y)] = None
            else:
                _world[(x, y)] = getattr(__import__('tiles'), tile_name)(x, y)


def tile_exists(x, y):
    return _world.get((x, y))
