#! /usr/bin/env python3
# coding: utf-8

"""
    Define main() and Initialize.
"""

from controller.game import Game


def main():
    """"
        Create an insane of Game and loop through
        Game.loop() while Game.IS_RUNNING return true.
    """

    game = Game()

    while game.is_running:
        game.loop()


if __name__ == "__main__":
    main()
