import pygame
import player
import buttons
import redraw_window
import AAfilledRoundedRect

game_quit = False
draw = False


def game_loop():
    pygame.init()  # Initialize

    screen_x = 1280  # Screen dimension x
    screen_y = 720  # Screen dimension y

    window = pygame.display.set_mode((screen_x, screen_y))  # Setting up window as screen
    pygame.display.set_caption("My Game")  # window name
    font = pygame.font.Font('ImminentLine.ttf', 80)
    space_font = pygame.font.Font('ImminentLine.ttf', 200)
    width = 300
    height = 95
    replay_img_red = pygame.image.load('background/btn/play_again_btn_red.png')
    quit_img_red = pygame.image.load('background/btn/exit_btn_red.png')
    menu_img_red = pygame.image.load('background/btn/menu_btn_red.png')
    replay_img_yellow = pygame.image.load('background/btn/play_again_btn_yellow.png')
    quit_img_yellow = pygame.image.load('background/btn/exit_btn_yellow.png')
    menu_img_yellow = pygame.image.load('background/btn/menu_btn_yellow.png')
    replay = buttons.button(screen_x / 2 - width / 2 - 320, screen_y / 2 - height / 2, width, height, (0, 255, 0), '', replay_img_red)
    quit_game = buttons.button(screen_x / 2 - width / 2 + 320, screen_y / 2 - height / 2, width, height, (0, 255, 0), '', quit_img_red)
    menu_btn = buttons.button(screen_x / 2 - width / 2, screen_y / 2 - height / 2, width, height, (0, 255, 0), '', menu_img_red)
    dim_screen = pygame.Surface((screen_x, screen_y)).convert_alpha()
    dim_screen.fill((0, 0, 0, 130))

    run = True
    game = True
    loop = True
    start = True
    global game_quit
    global draw

    p1 = player.Player(400, 580, 128, 128, False, (0, 0), f'PLAYER 1:', 1, screen_x, screen_y)
    p2 = player.Player(700, 580, 128, 128, True, (1050, 0), "PLAYER 2:", 2, screen_x, screen_y)

    while run:
        draw = False
        redraw_window.die_count = 0
        pygame.mixer.music.load('sound/dragon_ball_bg.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        timer = pygame.USEREVENT
        pygame.time.set_timer(timer, 1000)
        timer_sec = 90

        timer_bullet = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_bullet, 1000)
        bullet_timer_sec = 3

        start_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(start_timer, 1000)
        start_timer_sec = 3
        while start:
            redraw_window.die_count = 0
            redraw_window.die_count_2 = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    game = False
                    game_quit = True
                    start = False
                if event.type == start_timer:
                    if start_timer_sec > 1:
                        start_timer_sec -= 1
                    else:
                        pygame.time.set_timer(start_timer, 0)
                        start = False
                        game = True
            redraw_window.redraw_window(window, p1, p2, screen_x, timer_sec, bullet_timer_sec, True, True)
            start_countdown = space_font.render(str(start_timer_sec), 1, (255, 255, 255))
            window.blit(start_countdown, (int(screen_x / 2 - start_countdown.get_width() / 2), int(screen_y / 2 - start_countdown.get_height() / 2)))
            window.blit(dim_screen, (0, 0))
            pygame.display.update()

        while game:
            pygame.time.delay(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    game = False
                    start = False
                    game_quit = True
                if event.type == timer:
                    if timer_sec > 0:
                        timer_sec -= 1
                    else:
                        if p1.health > p2.health:
                            p2.die = True
                        elif p1.health < p2.health:
                            p1.die = True
                        elif p1.health == p2.health:
                            p1.die = False
                            p2.die = False
                            draw = True
                if event.type == timer_bullet:
                    if bullet_timer_sec > 0:
                        bullet_timer_sec -= 1
                    elif bullet_timer_sec == 0:
                        if p1.bullet_count < 10:
                            p1.bullet_count += 1
                            p1.bullet_bar_x -= 20
                            p1.bullet_bar_w = p1.bullet_count * 20
                        if p2.bullet_count < 10:
                            p2.bullet_count += 1

                        p1.player_bullet_count = p1.font.render(f'BULLET REMAINING: {p1.bullet_count}', False, (255, 255, 255))
                        p2.player_bullet_count = p2.font.render(f'BULLET REMAINING: {p2.bullet_count}', False, (255, 255, 255))
                        bullet_timer_sec = 3

            if p1.is_dead():
                game = False
                loop = True

            elif p2.is_dead():
                game = False
                loop = True

            elif draw:
                game = False
                loop = True

            p1.movement(True, p2, window)
            p2.movement(False, p1, window)
            redraw_window.redraw_window(window, p1, p2, screen_x, timer_sec, bullet_timer_sec)

        if p1.die or p2.die or draw:
            while loop:
                redraw_window.redraw_window(window, p1, p2, screen_x, timer_sec, bullet_timer_sec, True)
                window.blit(dim_screen, (0, 0))
                replay.draw(window, False)
                quit_game.draw(window, False)
                menu_btn.draw(window, False)
                p1.bullets = []
                p2.bullets = []
                if p1.is_dead():
                    text = font.render('PLAYER ONE WON!', 1, (255, 255, 255))
                    window.blit(text, (int(screen_x / 2 - text.get_width() / 2), int(screen_y / 2 - text.get_height() / 2 - 140)))
                elif p2.is_dead():
                    text = font.render('PLAYER TWO WON!', 1, (255, 255, 255))
                    window.blit(text, (int(screen_x / 2 - text.get_width() / 2), int(screen_y / 2 - text.get_height() / 2 - 140)))
                elif not p2.is_dead() and not p1.is_dead():
                    text = font.render('DRAW', 1, (255, 255, 255))
                    window.blit(text, (int(screen_x / 2 - text.get_width() / 2), int(screen_y / 2 - text.get_height() / 2 - 140)))

                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                        run = False
                        game_quit = True
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if replay.is_over(pos):
                            loop = False
                            game = True
                            start = True
                            p1 = player.Player(400, 580, 128, 128, False, (0, 0), f'PLAYER 1:', 1, screen_x, screen_y)
                            p2 = player.Player(700, 580, 128, 128, True, (1050, 0), "PLAYER 2:", 2, screen_x, screen_y)
                            break
                        if quit_game.is_over(pos):
                            loop = False
                            game = False
                            run = False
                            game_quit = True
                            break
                        if menu_btn.is_over(pos):
                            loop = False
                            game = False
                            run = False
                            break
                    if event.type == pygame.MOUSEMOTION:
                        if replay.is_over(pos):
                            replay.image = replay_img_yellow
                        elif not replay.is_over(pos):
                            replay.image = replay_img_red
                        if quit_game.is_over(pos):
                            quit_game.image = quit_img_yellow
                        elif not quit_game.is_over(pos):
                            quit_game.image = quit_img_red
                        if menu_btn.is_over(pos):
                            menu_btn.image = menu_img_yellow
                        elif not menu_btn.is_over(pos):
                            menu_btn.image = menu_img_red


    #pygame.quit()


