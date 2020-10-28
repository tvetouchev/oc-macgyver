#! /usr/bin/env python3
# coding: utf-8

"""
    Define Game Class.
"""
import pygame

from view.display import Display
from model.map import Map
from model.position import Position
from model.player import Player
from model.guard import Guard
from model.items import Items

import game_variables


class Game:
    """"
        Class Methods:
            __init__(self), loop(self), event_handler(self, event),
            won_game(self, boolean), exit_game().

        Class Property:
            PICKED_UP_ITEM[], (boolean)is_running, (boolean)is_player_near_guard,
            (int)player_guard_xdiff, (int)player_guard_ydiff.
    """
    PICKED_UP_ITEM = []

    def __init__(self):
        """
            Initialize Pygame and create instance for Display,
            Map, Player, Guard, Items and pygame.time.Clock.
        """

        self.is_running = True

        pygame.init()

        self.display = Display()
        self.clock = pygame.time.Clock()

        self.game_map = Map('level1')

        self.player = Player(self.game_map.player_startpos, game_variables.PLAYER_IMAGE)
        self.guard = Guard(self.game_map.guard_startpos, game_variables.GUARD_IMAGE)

        Items.create_items(game_variables.ITEMS, self.game_map.guard_startpos)

        self.items_list = Items.ITEMS

    def loop(self):
        """"
            Manage the main operations for the game in order to work.
            Manage event, if the player is near the guard, items,
            structures like walls and tiles, drawing of sprites,
            and winning or loosing the game.
        """
        picked_up_item_count = len(self.PICKED_UP_ITEM)
        items_count = len(self.items_list)

        for event in pygame.event.get():
            self.event_handler(event)

        if self.is_player_near_guard:
            if picked_up_item_count == items_count:
                self.guard.kill_guard()
                self.won_game(True)
            else:
                self.won_game(False)

        for i in range(len(self.game_map.WALLS)):
            self.display.draw(self.game_map.WALLS[i])

        for i in range(len(self.game_map.TILES)):
            self.display.draw(self.game_map.TILES[i])

        for i in range(len(self.items_list)):
            item = self.items_list[i]
            if Position.difference_between_position(
                    self.player.get_position, item.get_position) == 0 and not item.picked_up:

                print(item.pickup())
                self.PICKED_UP_ITEM.append(item.name)
                if len(self.PICKED_UP_ITEM) == len(self.items_list):
                    print('You crafted a {}'.format(game_variables.ITEM_TO_CRAFT))

            if not item.picked_up:
                self.display.draw(item)

        object_str_template = 'Object collected: {}/{}'.format(
            len(self.PICKED_UP_ITEM), len(self.items_list))

        self.display.draw_text(object_str_template, (0, 0))
        self.display.draw(self.guard)
        self.display.draw(self.player)
        self.display.update()

        self.clock.tick(60)

    def event_handler(self, event):
        """
            param event: pygame event
            Handle pygame events.
        """
        if event.type == pygame.QUIT:
            self.exit_game()

        elif event.type == pygame.KEYUP:
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
        """
            param won_or_lost: Boolean
            Print the according message and then close the game.
        """
        if won_or_lost:
            print('You WON!')
            self.exit_game()

        else:
            print('You LOST!')
            self.exit_game()

    def exit_game(self):
        """
            exit main loop by setting is_running to false.
        """
        self.is_running = False

    @property
    def is_player_near_guard(self):
        """"
            Add the player guard x and y axis difference,
            if it equals 2 * game_property.CASE_SIZE return true,
            otherwise return false.
        """
        x_diff = self.player_guard_xdiff
        y_diff = self.player_guard_ydiff

        return abs(x_diff) + abs(y_diff) == game_variables.CASE_SIZE * 2

    @property
    def player_guard_xdiff(self):
        """
            Return the player guard x diff.
        """
        return self.player.get_x - self.guard.get_x

    @property
    def player_guard_ydiff(self):
        """
            Return the player guard y diff.
        """
        return self.player.get_y - self.guard.get_y
