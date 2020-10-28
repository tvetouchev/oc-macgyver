#! /usr/bin/env python3
# coding: utf-8

"""
    Define Display Class.
"""

import pygame
import pygame.freetype
from game_variables import TITLE, WIDTH, HEIGHT


class Display:
    """
        Class Methods:
            __init__(self), __initialize_window(),
            update(), draw(self, model), draw_text(self, text, pos)
    """

    def __init__(self):
        """
            Initialize window and Pygame font system.
        """
        self.window = self.__initialize_window()
        pygame.font.init()
        self.font = pygame.freetype.SysFont('Arial', 30)

    @staticmethod
    def __initialize_window():
        """
            Initialize Window and set title.
        """
        game_window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        return game_window

    @staticmethod
    def update():
        """
            Update the display.
        """
        pygame.display.update()

    def draw(self, model):
        """
            param model: Class(Image)
            Draw a sprite on window.
        """
        self.window.blit(model.img, model.get_position)

    def draw_text(self, text, pos):
        """
            param text: str
            param pos: (x, y)
            Draw the given text at the given pos.
        """
        text_render, _ = self.font.render(text, (0, 96, 255))
        self.window.blit(text_render, pos)
