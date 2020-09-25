import os
import pygame


class Image:

    @staticmethod
    def __load_and_scale_image(image):
        directory = os.path.dirname(os.path.dirname(__file__))
        image_path = os.path.join(directory, 'resources', image)

        final_image = pygame.image.load(image_path)
        final_image = pygame.transform.scale(final_image, (50, 50))  # scale to fit case size

        return final_image

    def __init__(self, img):
        self.img = self.__load_and_scale_image(img)

    def change_image(self, image):
        self.img = self.__load_and_scale_image(image)
