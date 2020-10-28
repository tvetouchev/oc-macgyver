#! /usr/bin/env python3
# coding: utf-8

"""
    Declare Items Class
"""

import random
import os

from model.image import Image
from model.position import Position
from model.map import Map

import game_variables


class Items(Position, Image):
    """
        Inherit from Position and Image
        Class Methods:
            __init__(self, pos, img), get_name_without_extension(item),
            pickup(self), create_items(cls, items, guard_pos)

    """

    ITEMS = []

    def __init__(self, pos, img):
        """
            param pos: [x, y]
            param img: str
            Initialize Position and Image,
            sets map name without extension and
            set picked_up to False
        """
        Position.__init__(self, pos)
        Image.__init__(self, img)
        self.name = self.get_name_without_extension(img)
        self.picked_up = False

    @staticmethod
    def get_name_without_extension(item):
        """
        param item: str
            return item name without extension
        """
        return os.path.splitext(item)[0]

    def pickup(self):
        """
            Set picked_up of an item Instance to true
            and return a str with the item name
        """
        self.picked_up = True
        return 'You picked up {}'.format(self.name)

    @classmethod
    def create_items(cls, items, guard_pos):
        """
            param items: list
            param guard_pos: [x, y]

            Create every item of items and verifying they
            are not too close to guard_pos ( case.size * 3 )
        """

        for item in items:
            generate_random_position = True
            item_pos = Position([0, 0])

            while generate_random_position:
                x_axis = random.randint(0, 15)
                y_axis = random.randint(0, 15)
                item_pos.change_pos([x_axis * 50, y_axis * 50])

                if Map.is_accessible(item_pos.get_position):
                    if Position.difference_between_position(
                            item_pos.get_position,
                            guard_pos) >= game_variables.CASE_SIZE * 3:
                        generate_random_position = False

            new_item = Items(item_pos.get_position, item)
            cls.ITEMS.append(new_item)
