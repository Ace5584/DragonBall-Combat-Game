import pygame
import AAfilledRoundedRect

clock = pygame.time.Clock()  # clock
bg = pygame.image.load('background/city_4.png')  # Importing background image
font = pygame.font.Font('ImminentLine.ttf', 60)
shield_timer_font = pygame.font.Font('ImminentLine.ttf', 15)

shield_timer = [pygame.image.load('timer/timer_1.png'), pygame.image.load('timer/timer_2.png'),
                pygame.image.load('timer/timer_3.png'), pygame.image.load('timer/timer_4.png')]
teleport_label = pygame.image.load('goku/vanish_times.png')

player1_die_left = [pygame.image.load('goku/die.png'), pygame.image.load('goku/die1.png'),
                    pygame.image.load('goku/die2.png'), pygame.image.load('goku/die3.png'),
                    pygame.image.load('goku/die4.png')]
player1_die_right = [pygame.image.load('goku/R_die.png'), pygame.image.load('goku/R_die1.png'),
                     pygame.image.load('goku/R_die2.png'), pygame.image.load('goku/R_die3.png'),
                     pygame.image.load('goku/R_die4.png')]
player2_die_left = [pygame.image.load('Vegeta/die.png'), pygame.image.load('Vegeta/die1.png'),
                    pygame.image.load('Vegeta/die2.png'), pygame.image.load('Vegeta/die3.png')]
player2_die_right = [pygame.image.load('Vegeta/R_die.png'), pygame.image.load('Vegeta/R_die1.png'),
                     pygame.image.load('Vegeta/R_die2.png'), pygame.image.load('Vegeta/R_die3.png')]

goku_explode = [pygame.image.load('goku/explode_1.png'), pygame.image.load('goku/explode_2.png'),
                pygame.image.load('goku/explode_3.png'), pygame.image.load('goku/explode_4.png'), ]

character_circle_L = pygame.image.load('background/character_circle_L.png')
character_circle_R = pygame.image.load('background/character_circle_R.png')
character1_display_R = pygame.image.load('goku/goku_character_R.png')
character1_display_L = pygame.image.load('goku/goku_character_L.png')
character1_display_dead_R = pygame.image.load('goku/character_dead_R.png')
character1_display_dead_L = pygame.image.load('goku/character_dead_L.png')

character2_display_R = pygame.image.load('Vegeta/character_R.png')
character2_display_L = pygame.image.load('Vegeta/character_L.png')
character2_display_dead_R = pygame.image.load('Vegeta/character_dead_R.png')
character2_display_dead_L = pygame.image.load('Vegeta/character_dead_L.png')

c1_move_count = 0
c2_move_count = 0

die_count = 0
die_count_2 = 0
ex_count = 0
ex_count_2 = 0
flying = pygame.mixer.Sound('sound/flying.wav')
#flying.set_volume(0.5)

def redraw_window(window, player1, player2, screen_x, time_seconds, bullet_seconds, pause=False, start_screen=False):
    if player1.is_dead() or player2.is_dead():
        player1.walking = False
        player2.walking = False
    if player1.walking or player2.walking and not player1.is_dead() and not player2.is_dead():
        pygame.mixer.Channel(1).play(flying)
    elif player1.is_dead() or player2.is_dead() or not player1.walking or not player2.walking:
        flying.stop()

    global c1_move_count
    global c2_move_count
    global die_count
    global die_count_2
    global ex_count
    global ex_count_2
    clock.tick(60)
    window.blit(bg, (0, 0))
    window.blit(character_circle_L, (0, 0))
    window.blit(character_circle_R, (screen_x-380, 0))
    if not player2.is_dead():
        if 0 <= c1_move_count < 1:
            window.blit(character1_display_R, (30, 30))
            c1_move_count += 0.05
        if 1 <= c1_move_count <= 2:
            window.blit(character1_display_R, (30, 25))
            c1_move_count += 0.05
        if c1_move_count > 2:
            c1_move_count = 0
    else:
        window.blit(character1_display_dead_L, (30, 30))

    if not player1.is_dead():
        if 0 <= c2_move_count < 1:
            window.blit(character2_display_L, (1168, 30))
            c2_move_count += 0.05
        if 1 <= c2_move_count <= 2:
            window.blit(character2_display_L, (1168, 25))
            c2_move_count += 0.05
        if c2_move_count > 2:
            c2_move_count = 0
    else:
        window.blit(character2_display_dead_R, (1168, 30))

    # window.blit(player1.player_information, player1.text_location)
    # window.blit(player2.player_information, player2.text_location)

    for z in player1.bullets:
        z.shoot_bullet(window, 'red', player1.left)
    for z in player2.bullets:
        z.shoot_bullet(window, 'blue', player2.left)

    AAfilledRoundedRect.AAfilledRoundedRect(window, player1.bottom_health_bar_location, (255, 255, 0), 1)
    AAfilledRoundedRect.AAfilledRoundedRect(window, player2.bottom_health_bar_location, (255, 255, 0), 1)
    AAfilledRoundedRect.AAfilledRoundedRect(window, player1.health_bar_location, (255, 0, 0), 1)
    AAfilledRoundedRect.AAfilledRoundedRect(window, player2.health_bar_location, (255, 0, 0), 1)

    # AAfilledRoundedRect.AAfilledRoundedRect(window, player1.bottom_shield_bar, (255, 255, 255), 1)
    # AAfilledRoundedRect.AAfilledRoundedRect(window, player2.bottom_shield_bar, (255, 255, 255), 1)
    # AAfilledRoundedRect.AAfilledRoundedRect(window, player1.shield_bar, (0, 0, 255), 1)
    # AAfilledRoundedRect.AAfilledRoundedRect(window, player2.shield_bar, (0, 0, 255), 1)
    AAfilledRoundedRect.AAfilledRoundedRect(window, (player1.bullet_bar_bottom_x, player1.bullet_bar_y, player1.bullet_bar_bottom_w, player1.bullet_bar_h), (255, 255, 0), 1)
    AAfilledRoundedRect.AAfilledRoundedRect(window, (player2.bullet_bar_bottom_x, player2.bullet_bar_y, player2.bullet_bar_bottom_w, player2.bullet_bar_h), (255, 255, 0), 1)
    AAfilledRoundedRect.AAfilledRoundedRect(window, (player1.bullet_bar_x, player1.bullet_bar_y, player1.bullet_bar_w, player1.bullet_bar_h), (31, 117, 254), 1)
    AAfilledRoundedRect.AAfilledRoundedRect(window, (player2.bullet_bar_x, player2.bullet_bar_y, player2.bullet_bar_w, player2.bullet_bar_h), (31, 117, 254), 1)

    # pygame.draw.rect(window, (255, 255, 255), player1.bottom_health_bar_location)
    # pygame.draw.rect(window, (255, 255, 255), player2.bottom_health_bar_location)
    # pygame.draw.rect(window, (255, 0, 0), player1.health_bar_location)
    # pygame.draw.rect(window, (255, 0, 0), player2.health_bar_location)
    # pygame.draw.rect(window, (255, 255, 255), player1.bottom_shield_bar)
    # pygame.draw.rect(window, (255, 255, 255), player2.bottom_shield_bar)
    # pygame.draw.rect(window, (0, 0, 255), player1.shield_bar)
    # pygame.draw.rect(window, (0, 0, 255), player2.shield_bar)

    if bullet_seconds == 0:
        window.blit(shield_timer[3], player1.shield_timer_location)
        window.blit(shield_timer[3], player2.shield_timer_location)
    if bullet_seconds == 1:
        window.blit(shield_timer[2], player1.shield_timer_location)
        window.blit(shield_timer[2], player2.shield_timer_location)
    if bullet_seconds == 2:
        window.blit(shield_timer[1], player1.shield_timer_location)
        window.blit(shield_timer[1], player2.shield_timer_location)
    if bullet_seconds == 3:
        window.blit(shield_timer[0], player1.shield_timer_location)
        window.blit(shield_timer[0], player2.shield_timer_location)

    if player1.teleport_remain == 3:
        window.blit(teleport_label, (player1.teleport_x, player1.teleport_y))
        window.blit(teleport_label, (player1.teleport_x + 30, player1.teleport_y))
        window.blit(teleport_label, (player1.teleport_x + 60, player1.teleport_y))
    elif player1.teleport_remain == 2:
        window.blit(teleport_label, (player1.teleport_x, player1.teleport_y))
        window.blit(teleport_label, (player1.teleport_x + 30, player1.teleport_y))
    elif player1.teleport_remain == 1:
        window.blit(teleport_label, (player1.teleport_x, player1.teleport_y))
    else:
        None

    if player2.teleport_remain == 3:
        window.blit(teleport_label, (player2.teleport_x, player1.teleport_y))
        window.blit(teleport_label, (player2.teleport_x + 30, player1.teleport_y))
        window.blit(teleport_label, (player2.teleport_x + 60, player1.teleport_y))
    elif player2.teleport_remain == 2:
        window.blit(teleport_label, (player2.teleport_x, player1.teleport_y))
        window.blit(teleport_label, (player2.teleport_x + 30, player1.teleport_y))
    elif player2.teleport_remain == 1:
        window.blit(teleport_label, (player2.teleport_x, player1.teleport_y))
    else:
        None

    if not pause:
        text = font.render(str(time_seconds), True, (255, 255, 255))
        window.blit(text, (screen_x / 2 - text.get_width() / 2, 0))
        player1.draw(window, 1)
        player2.draw(window, 2)
        player1.attack(player2, window)
        player2.attack(player1, window)
        if player1.explode:
            if 0 <= ex_count < 3:
                if player2.walking:
                    window.blit(goku_explode[round(ex_count)], (int(player2.x), int(player2.y - 10)))
                else:
                    window.blit(goku_explode[round(ex_count)], (int(player2.x), int(player2.y)))
                ex_count += 0.2
            elif ex_count > 3:
                ex_count = 0
                player1.explode = False

        if player2.explode:
            if 0 <= ex_count_2 < 3:
                if player1.walking:
                    window.blit(goku_explode[round(ex_count_2)], (int(player1.x), int(player1.y - 10)))
                else:
                    window.blit(goku_explode[round(ex_count_2)], (int(player1.x), int(player1.y - 10)))
                ex_count_2 += 0.2
            elif ex_count_2 > 3:
                ex_count_2 = 0
                player2.explode = False
        pygame.display.update()
    else:
        if start_screen:
            player1.freeze(window, 1)
            player2.freeze(window, 2)
        else:
            if player2.is_dead():
                player2.freeze(window, 2)
                if 0 <= die_count < 4:
                    if player1.knock_down_direction < 0:
                        window.blit(player1_die_right[round(die_count)], (int(player1.x), int(player1.y)))
                        die_count += 0.2
                        if player1.x < screen_x - player1.vol - player1.width:
                            player1.x -= 3
                    else:
                        window.blit(player1_die_left[round(die_count)], (int(player1.x), int(player1.y)))
                        die_count += 0.2
                        if player1.x > player1.vol:
                            player1.x += 3
                elif die_count:
                    if player1.left:
                        window.blit(player1_die_right[4], (int(player1.x), int(player1.y)))
                    else:
                        window.blit(player1_die_left[4], (int(player1.x), int(player1.y)))

            if player1.is_dead():
                player1.freeze(window, 1)
                if 0 <= die_count_2 < 3:
                    if player2.knock_down_direction < 0:  # Left
                        window.blit(player2_die_right[round(die_count_2)], (int(player2.x), int(player2.y)))
                        die_count_2 += 0.2
                        if player2.x < screen_x - player2.vol - player2.width:
                            player2.x -= 1
                    else:  # Right
                        window.blit(player2_die_left[round(die_count_2)], (int(player2.x), int(player2.y)))
                        die_count_2 += 0.2
                        if player2.x > player2.vol:
                            player2.x += 1
                elif die_count_2:
                    if player2.left:
                        window.blit(player2_die_right[3], (int(player2.x), int(player2.y)))
                    else:
                        window.blit(player2_die_left[3], (int(player2.x), int(player2.y)))

            if not player1.is_dead() and not player2.is_dead():
                player1.freeze(window, 1)
                player2.freeze(window, 2)
