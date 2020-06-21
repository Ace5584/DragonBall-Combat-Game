import pygame

clock = pygame.time.Clock()  # clock
bg = pygame.image.load('bg.jpg')  # Importing background image



def redraw_window(window, player1, player2, screen_x,pause=False):

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
        player1.draw(window, 1)
        player2.draw(window, 2)
        pygame.display.update()
    else:
        if player1.is_dead():
            player1.freeze(window, 1)
        else:
            player2.freeze(window, 2)
