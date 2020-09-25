from model.image import Image
from model.position import Position
from controller.map import Map

import random
import os


class Items(Position, Image):
    ITEMS = []

    def __init__(self, pos, img, name):
        Position.__init__(self, pos)
        Image.__init__(self, img)
        self.name = name
        self.picked_up = False

    @staticmethod
    def get_name_without_extension(item):
        return os.path.splitext(item)[0]

    def pickup(self):
        self.picked_up = True
        return 'You picked up {}'.format(self.name)

    @classmethod
    def create_items(cls, items, guard_pos, case_size):
        for item in items:
            generate_random_position = True
            position = []

            while generate_random_position:
                x_axis = random.randint(0, 15)
                y_axis = random.randint(0, 15)
                end_pos = [x_axis * 50, y_axis * 50]

                if Map.is_accessible(end_pos):

                    if Position.difference_between_position(end_pos, guard_pos) >= case_size * 3:
                        generate_random_position = False
                        position = end_pos

            item_name = cls.get_name_without_extension(item)
            new_item = Items(position, item, item_name)
            cls.ITEMS.append(new_item)
