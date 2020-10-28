#! /usr/bin/env python3
# coding: utf-8

"""
    Declare Image Class
"""

import os
import pygame

from game_variables import CASE_SIZE


class Image:
    """
        Class Methods:
            __init(self), __load_and_scale_image(image),
            change_image(self, image)
    """

    def __init__(self, img):
        """
            param img: str
            declare img by executing load and scale image
        """
        img_path = self.get_image_path(img)
        self.img = self.scale_image(img_path)

    @staticmethod
    def get_image_path(image):
        """
            param image: str
            Load Image
        """
        directory = os.path.dirname(os.path.dirname(__file__))
        image_path = os.path.join(directory, 'resources', image)

        return image_path

    @staticmethod
    def scale_image(image_path):
        """
            param image_path: Path
            Scale image to fit case size.
        """

        final_image = pygame.image.load(image_path)
        final_image = pygame.transform.scale(final_image,
                                             (CASE_SIZE, CASE_SIZE))  # scale to fit case size

        return final_image

    def change_image(self, image):
        """
            param image: str
            change the current img to another one
        """
        img_path = self.get_image_path(image)
        self.img = self.scale_image(img_path)
