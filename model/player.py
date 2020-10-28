#! /usr/bin/env python3
# coding: utf-8

""""
    Define Player Class
"""

from model.image import Image
from model.position import Position

import game_variables


class Player(Position, Image):
    """
        Inherit from Position and Image
        Class Methods:
            __init__(self, pos, img), move_left(self), move_right(self),
            move_up(self), move_down(self)
    """

    def __init__(self, pos, img):
        """
            param pos: [x, y]
            param img: str
            Initialize Position and Image
        """
        Position.__init__(self, pos)
        Image.__init__(self, img)

    def move_left(self):
        """
            Calculate the action to move to the left.
        """
        return [self.get_x - game_variables.CASE_SIZE, self.get_y]

    def move_right(self):
        """
            Calculate the action to move to the right.
        """
        return [self.get_x + game_variables.CASE_SIZE, self.get_y]

    def move_up(self):
        """
            Calculate the action to move to the up.
        """
        return [self.get_x, self.get_y - game_variables.CASE_SIZE]

    def move_down(self):
        """
            Calculate the action to move to the down.
        """
        return [self.get_x, self.get_y + game_variables.CASE_SIZE]
