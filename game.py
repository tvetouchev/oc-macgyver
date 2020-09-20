import pygame

pygame.init()

display_width = 800
display_height = 800
display = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

pygame.display.set_caption('Help MacGyver Escape')

player = pygame.image.load("resources/MacGyver.png")
player = pygame.transform.scale(player, (50, 50))

guard = pygame.image.load("resources/Gardien.png")
guard = pygame.transform.scale(guard, (50, 50))


def main():
    game_is_running = True

    player_position = [300, 300]
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
                x_axis = player_position[0]
                y_axis = player_position[1]

                if event.key == pygame.K_RIGHT:
                    if x_axis + 50 <= 750:
                        print('Right KeyUp')
                        x_axis += 50

                elif event.key == pygame.K_LEFT:
                    if x_axis - 50 >= 0:
                        print('Left KeyUp')
                        x_axis -= 50

                elif event.key == pygame.K_UP:
                    if y_axis - 50 >= 0:
                        print('Up KeyUp')
                        y_axis -= 50

                elif event.key == pygame.K_DOWN:
                    if y_axis + 50 <= 750:
                        print('Down KeyUp')
                        y_axis += 50

                player_position = [x_axis, y_axis]

        # if abs(player_position[0] - guard_position[0]) == 50 or abs(player_position[1] - guard_position[1]):
        #     print('near enough!')

        # print('x_axis: {}'.format(abs(player_position[0] - guard_position[0])))
        # print('y_axis: {}'.format(abs(player_position[1] - guard_position[1])))
        if abs(player_position[0] - guard_position[0]) == 50 and abs(player_position[1] - guard_position[1]) == 0:
            print('You WON!')
            game_is_running = False
        elif abs(player_position[0] - guard_position[0]) == 0 and abs(player_position[1] - guard_position[1]) == 50:
            print('You WON!')
            game_is_running = False

        display.blit(player, player_position)
        display.blit(guard, guard_position)
        pygame.display.update()

        clock.tick(60)
        # pygame.time.delay(1000)


if __name__ == "__main__":
    main()
