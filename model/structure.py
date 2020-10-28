#! /usr/bin/env python3
# coding: utf-8

"""
    Define Structure Class.
"""

from model.image import Image
from model.position import Position


class Structure(Position, Image):
    """
        Inherit from Position and Image.
        Class Methods:
            __init__(self, pos, img)
    """
    def __init__(self, pos, img):
        """
            param pos: [x, y]
            param img: str
            Initialize Position and Image.
        """
        Position.__init__(self, pos)
        Image.__init__(self, img)
