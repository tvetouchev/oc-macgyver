import pygame


class Display:

    def __init__(self, title, width, height):
        self.window = self.__initialize_window(title, width, height)

    @staticmethod
    def __initialize_window(title, width, height):
        game_window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        return game_window

    @staticmethod
    def update():
        pygame.display.update()

    def draw(self, model):
        self.window.blit(model.img, model.get_position)
