#! /usr/bin/env python3
# coding: utf-8

""""
    Define Map Class.
"""

import os

from model.structure import Structure
import game_variables


class Map:
    """
        Class Methods:
            __init__(self, map_name), __load_map(self), create_tile(self, position),
            create_wall(self, position), is_accessible(cls, position).
    """

    WALLS = []
    TILES = []

    def __init__(self, map_name):
        """
            param map_name: str
            Declare the map_name, load and initialize the map.
        """

        self.name = map_name
        self.__load_map()

    def __load_map(self):
        """
            Open the map file according to the map_name,
            read line by line and char by char to calculate
            the x, y axis and create the matching Structure
            for each char and declare the player_startpos and
            guard_startpos.
        """
        directory = os.path.dirname(os.path.dirname(__file__))
        level_path = os.path.join(directory, 'map', '{}.txt'.format(self.name))

        with open(level_path) as file:
            lines = file.readlines()

            line_count = 0
            for line in lines:
                line_str = line.strip()

                char_count = 0
                for char in line_str:
                    current_position = [char_count * 50, line_count * 50]

                    if char == 'w':
                        self.create_wall(current_position)
                    elif char == 't':
                        self.create_tile(current_position)
                    elif char == 'm':
                        self.create_tile(current_position)

                        self.player_startpos = current_position
                    elif char == 'g':
                        self.create_tile(current_position)

                        self.guard_startpos = [char_count * 50, line_count * 50]

                    char_count += 1

                line_count += 1

    def create_tile(self, position):
        """
            param position: [x, y]
            Create a Structure for a tile.
        """

        tile = Structure(position, game_variables.TILES_IMAGE)

        self.TILES.append(tile)

    def create_wall(self, position):
        """
            param position: [x, y]
            Create a Structure for a wall.
        """

        wall = Structure(position, game_variables.WALLS_IMAGE)

        self.WALLS.append(wall)

    @classmethod
    def is_accessible(cls, position):
        """
            param position: [x, y]
            Loop through walls Structure to check if
            the passed position matches a wall position
            return true or false.
        """

        for i in range(len(cls.WALLS)):
            if position == cls.WALLS[i].get_position:
                return False

        return True
