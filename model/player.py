import os
import pygame


class Player:
    PLUS_CASE = 50
    MINUS_CASE = -50

    def __init__(self, position, image):
        self.position = position
        self.image = self.__load_and_scale_image(image)

    @staticmethod
    def __load_and_scale_image(image):
        directory = os.path.dirname(os.path.dirname(__file__))
        image_path = os.path.join(directory, 'resources', image)

        player_image = pygame.image.load(image_path)
        player_image = pygame.transform.scale(player_image, (50, 50))  # scale to fit case size

        return player_image

    def draw(self, display):
        display.blit(self.image, self.position.get_position)

    def move_left(self):
        self.position.change_x(self.MINUS_CASE)

    def move_right(self):
        self.position.change_x(self.PLUS_CASE)

    def move_up(self):
        self.position.change_y(self.MINUS_CASE)

    def move_down(self):
        self.position.change_y(self.PLUS_CASE)
