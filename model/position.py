#! /usr/bin/env python3
# coding: utf-8

"""
    Declare Position Class.
"""


class Position:
    """
        Class Methods:
            __init__(self, start_pos), change_x(self, num),
            change_y(self, num), change_pos(self, position),
            __clamp_axis(axis), difference_between_position(pos1, pos2)

        Class Property:
            get_position, get_x, get_y
    """

    def __init__(self, start_pos):
        """
            param start_pos: [x, y]
            Set position to start_pos.
        """
        self.position = start_pos

    def change_x(self, num):
        """
            param num: int
            Calculate the x axis + num,
            clamp it and change x axis.
        """
        x_axis = self.__clamp_axis(self.get_x + num)

        self.position[0] = x_axis

    def change_y(self, num):
        """
            param num: int
            Calculate the y axis + num,
            clamp it and change y axis.
        """
        y_axis = self.__clamp_axis(self.get_y + num)

        self.position[1] = y_axis

    def change_pos(self, position):
        """
            param position: [x, y]
            Set position x, y axis to position[0]
            and position [1], clamp [0] and [1] to
            ensure not having problems.
        """

        x_axis = self.__clamp_axis(position[0])
        y_axis = self.__clamp_axis(position[1])

        self.position = [x_axis, y_axis]

    @staticmethod
    def __clamp_axis(axis):
        """
            param axis: int
            Check if the axis value is correct
            if not clamp it.
        """
        if axis > 750:
            return 750
        if axis < 0:
            return 0

        return axis

    @classmethod
    def difference_between_position(cls, pos1, pos2):
        """
            param pos1: [x, y]
            param pos2: [x, y]
            Calculate the absolute difference between
            two position.
        """
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    @property
    def get_position(self):
        """
            Get the position of the instance.
        """
        return self.position

    @property
    def get_x(self):
        """
            Get the x axis of the instance
        """
        return self.position[0]

    @property
    def get_y(self):
        """
            Get the y axis of the instance
        """
        return self.position[1]
