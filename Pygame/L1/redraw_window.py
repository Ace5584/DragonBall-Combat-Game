import pygame

clock = pygame.time.Clock()  # clock
bg = pygame.image.load('bg.jpg')  # Importing background image

count_down_time = 90

font = pygame.font.SysFont('comicsans', 60)

start_ticks = None


def redraw_window(window, player1, player2, screen_x, pause=False, start_screen=False):
    clock.tick(60)
    window.blit(bg, (0, 0))
    window.blit(player1.player_information, player1.text_location)
    window.blit(player2.player_information, player2.text_location)
    window.blit(player1.player_bullet_count, player1.bullet_count_text_location)
    window.blit(player2.player_bullet_count, player2.bullet_count_text_location)
    for z in player1.bullets:
        z.shoot_bullet(window, 'red')
    for z in player2.bullets:
        z.shoot_bullet(window, 'blue')
    pygame.draw.rect(window, (255, 255, 255), player1.bottom_health_bar_location)
    pygame.draw.rect(window, (255, 255, 255), player2.bottom_health_bar_location)
    pygame.draw.rect(window, (255, 0, 0), player1.health_bar_location)
    pygame.draw.rect(window, (255, 0, 0), player2.health_bar_location)
    if not pause:
        global start_ticks
        if start_ticks is None:
            start_ticks = pygame.time.get_ticks()
        else:
            None
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        seconds = int(seconds)
        text = font.render(f'Time: {count_down_time-seconds}', 1, (255, 255, 255))
        window.blit(text, (screen_x / 2 - text.get_width() / 2, 0))
        player1.draw(window, 1)
        player2.draw(window, 2)
        if count_down_time - seconds == 0:
            if player1.health < player2.health:
                player1.die = True
            else:
                player2.die = True

        pygame.display.update()
    else:
        if start_screen:
            player1.freeze(window, 1)
            player2.freeze(window, 2)
        else:
            if player1.is_dead():
                player1.freeze(window, 1)
            else:
                player2.freeze(window, 2)

# start_ticks = pygame.time.get_ticks()
#
# count_down_time = 90
#
# font = pygame.font.SysFont('comicsans', 60)
# seconds = (pygame.time.get_ticks() - start_ticks) / 1000
# text = font.render(f'Time: {seconds}', 1, (255, 255, 255))
# window.blit(text, (320, 320))
# print(seconds)