from model.position import Position
from view.display import Display
from controller.map import Map
from model.player import Player
from model.guard import Guard
from model.items import Items

import pygame


class Game:
    WIDTH = 800
    HEIGHT = 800
    CASE_SIZE = 50
    TITLE = 'Help MacGyver Escape'
    IS_RUNNING = True
    PICKED_UP_ITEM = []

    def __init__(self):
        pygame.init()
        self.display = Display(self.TITLE, self.WIDTH, self.HEIGHT)
        self.clock = pygame.time.Clock()

        self.game_map = Map('level1')

        self.player = Player(self.game_map.player_startpos, self.game_map.player_image)
        self.guard = Guard(self.game_map.guard_startpos, self.game_map.guard_image)

        Items.create_items(self.game_map.items, self.game_map.guard_startpos, self.CASE_SIZE)
        self.ITEMS = Items.ITEMS

    def loop(self):

        for event in pygame.event.get():
            self.event_handler(event)

        if self.is_player_near_guard and len(self.PICKED_UP_ITEM) == len(self.ITEMS):
            self.guard.kill_guard()
            self.won_game(True)
        elif self.is_player_near_guard:
            self.won_game(False)

        for i in range(len(self.game_map.WALLS)):
            self.display.draw(self.game_map.WALLS[i])

        for i in range(len(self.game_map.TILES)):
            self.display.draw(self.game_map.TILES[i])

        for i in range(len(self.ITEMS)):
            item = self.ITEMS[i]
            if Position.difference_between_position(self.player.get_position, item.get_position) == 0 and\
                    not item.picked_up:

                print(item.pickup())
                self.PICKED_UP_ITEM.append(item.name)

            if not item.picked_up:
                self.display.draw(item)

        self.display.draw(self.guard)
        self.display.draw(self.player)
        self.display.update()

        self.clock.tick(60)

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.exit_game()

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_0:
                print('pressed k_0')
                Items.create_items(self.game_map.items, self.guard.get_position, self.CASE_SIZE)

            if event.key == pygame.K_RIGHT:
                next_position = self.player.move_right()

                if self.game_map.is_accessible(next_position):
                    self.player.change_pos(next_position)

            elif event.key == pygame.K_LEFT:
                next_position = self.player.move_left()

                if self.game_map.is_accessible(next_position):
                    self.player.change_pos(next_position)

            elif event.key == pygame.K_UP:
                next_position = self.player.move_up()

                if self.game_map.is_accessible(next_position):
                    self.player.change_pos(next_position)

            elif event.key == pygame.K_DOWN:
                next_position = self.player.move_down()

                if self.game_map.is_accessible(next_position):
                    self.player.change_pos(next_position)

    def won_game(self, won_or_lost):
        if won_or_lost:
            print('You WON!')
            self.exit_game()

        else:
            print('You LOST!')
            self.exit_game()

    @property
    def is_player_near_guard(self):
        if abs(self.player_guard_xdiff) + abs(self.player_guard_ydiff) == self.CASE_SIZE * 2:
            return True
        else:
            return False

    @property
    def player_guard_xdiff(self):
        return self.player.get_x - self.guard.get_x

    @property
    def player_guard_ydiff(self):
        return self.player.get_y - self.guard.get_y

    def exit_game(self):
        self.IS_RUNNING = False
