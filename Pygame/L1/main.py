import pygame
import player
import buttons
import redraw_window

pygame.init()  # Initialize

screen_x = 1280  # Screen dimension x
screen_y = 720  # Screen dimension y

window = pygame.display.set_mode((screen_x, screen_y))  # Setting up window as screen
pygame.display.set_caption("My Game")  # window name
font = pygame.font.SysFont('comicsans', 45)
space_font = pygame.font.SysFont('comicsans', 200)
width = 120
height = 60
replay = buttons.button(screen_x / 2 - width / 2 - 80, screen_y / 2 - height / 2, width, height, (0, 255, 0), "Play Again")
quit_game = buttons.button(screen_x / 2 - width / 2 + 80, screen_y / 2 - height / 2, width, height, (0, 255, 0), "Quit Game")
dim_screen = pygame.Surface((screen_x, screen_y)).convert_alpha()
dim_screen.fill((0, 0, 0, 130))

run = True
game = True
loop = True
start = True

game_quit = False

p1 = player.Player(50, 650, 64, 64, False, (0, 0), f'PLAYER 1:')
p2 = player.Player(1200, 650, 64, 64, True, (1050, 0), "PLAYER 2:")


bg_music = pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

start_ticks = pygame.time.get_ticks()
game_start_timer = int((pygame.time.get_ticks() - start_ticks) / 1000)
original_time = 3
temp_time = 0
reset_time = True
time_print = str()

timer = pygame.USEREVENT
pygame.time.set_timer(timer, 1000)
timer_sec = 90

timer_bullet = pygame.USEREVENT + 1
pygame.time.set_timer(timer_bullet, 1000)
bullet_timer_sec = 10

while run:
    timer_sec = 90
    original_time = 3
    temp_time = 0
    reset_time = True
    time_print = str()
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game = False
                game_quit = True
                start = False
        if reset_time:
            start_ticks = pygame.time.get_ticks()
            game_start_timer = int((pygame.time.get_ticks() - start_ticks) / 1000)
            temp_time = game_start_timer
            reset_time = False
        else:
            reset_time = False
        if time_print != '0':
            redraw_window.redraw_window(window, p1, p2, screen_x, timer_sec, bullet_timer_sec, True, True)
            game_start_timer = int((pygame.time.get_ticks() - start_ticks) / 1000)
            time_print = str(original_time - (int(game_start_timer) - temp_time))
            start_countdown = space_font.render(time_print, 1, (255, 255, 255))
            window.blit(start_countdown, (int(screen_x/2 - start_countdown.get_width()/2), int(screen_y/2 - start_countdown.get_height()/2)))
            window.blit(dim_screen, (0, 0))
            pygame.display.update()
        else:
            start = False

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
                    else:
                        p1.die = True
            if event.type == timer_bullet:
                if bullet_timer_sec > 0:
                    bullet_timer_sec -= 1
                elif bullet_timer_sec == 0:
                    p1.bullet_count += 1
                    p2.bullet_count += 1
                    p1.player_bullet_count = p1.font.render(f'BULLET REMAINING: {p1.bullet_count}', False, (255, 255, 255))
                    p2.player_bullet_count = p2.font.render(f'BULLET REMAINING: {p2.bullet_count}', False, (255, 255, 255))
                    bullet_timer_sec = 10


        if p1.is_dead():
            game = False
            loop = True

        elif p2.is_dead():
            game = False
            loop = True

        p1.movement(True, p2, window, screen_x, screen_y)
        p2.movement(False, p1, window, screen_x, screen_y)
        redraw_window.redraw_window(window, p1, p2, screen_x, timer_sec, bullet_timer_sec)

    if p1.die or p2.die:
        while loop:
            redraw_window.redraw_window(window, p1, p2, screen_x, timer_sec, bullet_timer_sec, True)
            window.blit(dim_screen, (0, 0))
            replay.draw(window)
            quit_game.draw(window)
            if p1.is_dead():
                text = font.render('PLAYER ONE WON!', 1, (255, 255, 255))
                window.blit(text, (int(screen_x / 2 - text.get_width() / 2), int(screen_y / 2 - text.get_height() / 2 - 80)))
            elif p2.is_dead():
                text = font.render('PLAYER TWO WON!', 1, (255, 255, 255))
                window.blit(text, (int(screen_x / 2 - text.get_width() / 2), int(screen_y / 2 - text.get_height() / 2 - 80)))

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
                        p1 = player.Player(50, 650, 64, 64, False, (0, 0), f'PLAYER 1:')
                        p2 = player.Player(1200, 650, 64, 64, True, (1050, 0), "PLAYER 2:")
                        break
                    if quit_game.is_over(pos):
                        loop = False
                        game = False
                        run = False
                        game_quit = True
                        break
                if event.type == pygame.MOUSEMOTION:
                    if replay.is_over(pos):
                        replay.color = (255, 0, 0)
                    elif not replay.is_over(pos):
                        replay.color = (0, 255, 0)
                    if quit_game.is_over(pos):
                        quit_game.color = (255, 0, 0)
                    elif not quit_game.is_over(pos):
                        quit_game.color = (0, 255, 0)


#pygame.quit()


