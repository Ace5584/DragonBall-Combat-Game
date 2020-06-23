import pygame

clock = pygame.time.Clock()  # clock
bg = pygame.image.load('bg.jpg')  # Importing background image
font = pygame.font.SysFont('comicsans', 60)
shield_timer_font = pygame.font.SysFont('comicsans', 15)

def redraw_window(window, player1, player2, screen_x, time_seconds, pause=False, start_screen=False):
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
    pygame.draw.rect(window, (255, 255, 255), player1.bottom_shield_bar)
    pygame.draw.rect(window, (255, 255, 255), player2.bottom_shield_bar)
    pygame.draw.rect(window, (0, 0, 255), player1.shield_bar)
    pygame.draw.rect(window, (0, 0, 255), player2.shield_bar)
    if player1.shield_timer == 0:
        None
    else:
        text1 = shield_timer_font.render(str(player1.shield_timer), True, (255, 255, 255))
        window.blit(text1, player1.shield_timer_location)

    if player2.shield_timer == 0:
        None
    else:
        text2 = shield_timer_font.render(str(player2.shield_timer), True, (255, 255, 255))
        window.blit(text2, player2.shield_timer_location)

    if not pause:
        text = font.render(str(time_seconds), True, (255, 255, 255))
        window.blit(text, (screen_x / 2 - text.get_width() / 2, 0))
        player1.draw(window, 1)
        player2.draw(window, 2)
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
