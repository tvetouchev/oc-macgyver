from controller.game import Game


def main():
    game = Game()

    while game.IS_RUNNING:
        game.loop()


if __name__ == "__main__":
    main()
