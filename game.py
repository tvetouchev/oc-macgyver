import pygame
from model.position import Position
from model.player import Player

pygame.init()

display_width = 800
display_height = 800
display = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

pygame.display.set_caption('Help MacGyver Escape')

guard = pygame.image.load('resources/Guard.png')
guard = pygame.transform.scale(guard, (50, 50))


def main():
    game_is_running = True

    player_position = Position([300, 300])
    player = Player(player_position, 'MacGyver.png')

    guard_position = [500, 750]

    while game_is_running:
        display.fill((0, 0, 0))
        for i in range(15):
            pygame.draw.line(display, (66, 66, 66), (0, (i + 1) * 50), (display_width, (i + 1) * 50))
            pygame.draw.line(display, (66, 66, 66), ((i + 1) * 50, 0), ((i + 1) * 50, display_height))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.move_right()

                elif event.key == pygame.K_LEFT:
                    player.move_left()

                elif event.key == pygame.K_UP:
                    player.move_up()

                elif event.key == pygame.K_DOWN:
                    player.move_down()

        if abs(player.position.get_x - guard_position[0]) + abs(player.position.get_y - guard_position[1]) == 50:
            print('You WON!')
            game_is_running = False

        player.draw(display)
        display.blit(guard, guard_position)
        pygame.display.update()

        clock.tick(60)
        # pygame.time.delay(1000)


if __name__ == "__main__":
    main()
