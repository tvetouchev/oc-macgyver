from model.structure import Structure
import json
import os


class Map:
    WALLS = []
    TILES = []

    def __init__(self, map_name):
        self.name = map_name
        self.__load_map(map_name)

    def __load_map(self, map_name):
        json_data = self.__read_json(map_name)

        self.player_startpos = json_data['player_startpos']
        self.player_image = json_data['player_image']

        self.guard_startpos = json_data['guard_startpos']
        self.guard_image = json_data['guard_image']

        self.items = json_data['items']
        self.item_to_craft = json_data['item_to_craft']

        self.__generate_structures(json_data['walls'], json_data['walls_image'],
                                   json_data['tiles'], json_data['tiles_image'])

    @staticmethod
    def __read_json(map_name):
        directory = os.path.dirname(os.path.dirname(__file__))
        level_path = os.path.join(directory, 'map', '{}.json'.format(map_name))

        with open(level_path) as file:
            data = json.load(file)

        return data

    @classmethod
    def is_accessible(self, position):
        for i in range(len(self.WALLS)):
            if position == self.WALLS[i].get_position:
                return False

        return True

    def __generate_structures(self, walls, walls_img, tiles, tiles_img):
        # WALLS
        for i in range(len(walls)):
            wall_pos = walls[i]

            wall = Structure(wall_pos, walls_img)
            self.WALLS.append(wall)

        # TILES
        for i in range(len(tiles)):
            tile_pos = tiles[i]

            tile = Structure(tile_pos, tiles_img)
            self.TILES.append(tile)

