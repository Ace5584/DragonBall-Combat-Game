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
width = 120
height = 60
replay = buttons.button(screen_x / 2 - width / 2 - 80, screen_y / 2 - height / 2, width, height, (0, 255, 0), "Play Again")
quit_game = buttons.button(screen_x / 2 - width / 2 + 80, screen_y / 2 - height / 2, width, height, (0, 255, 0), "Exit Game")
dim_screen = pygame.Surface((screen_x, screen_y)).convert_alpha()
dim_screen.fill((0, 0, 0, 130))

black_bg = pygame.image.load('black background 30percent.png')

run = True
game = True
loop = True

p1 = player.Player(50, 650, 64, 64, False, (0, 0), f'PLAYER 1:')
p2 = player.Player(1200, 650, 64, 64, True, (1050, 0), "PLAYER 2:")


bg_music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

while run:

    while game:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game = False

        if p1.is_dead():
            game = False
            loop = True
        elif p2.is_dead():
            game = False
            loop = True

        p1.movement(True, p2, window, screen_x, screen_y)
        p2.movement(False, p1, window, screen_x, screen_y)
        redraw_window.redraw_window(window, p1, p2, screen_x)

    if p1.health < 0 or p2.health < 0:
        while loop:
            redraw_window.redraw_window(window, p1, p2, screen_x, True)
            window.blit(dim_screen, (0, 0))
            replay.draw(window)
            quit_game.draw(window)
            if p1.is_dead():
                text = font.render('PLAYER ONE WON!', 1, (255, 255, 255))
                window.blit(text, (screen_x / 2 - text.get_width() / 2, screen_y / 2 - text.get_height() / 2 - 80))
            elif p2.is_dead():
                text = font.render('PLAYER TWO WON!', 1, (255, 255, 255))
                window.blit(text, (screen_x / 2 - text.get_width() / 2, screen_y / 2 - text.get_height() / 2 - 80))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    run = False
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if replay.is_over(pos):
                        loop = False
                        game = True
                        p1 = player.Player(50, 650, 64, 64, False, (0, 0), f'PLAYER 1:')
                        p2 = player.Player(1200, 650, 64, 64, True, (1050, 0), "PLAYER 2:")
                        break
                    if quit_game.is_over(pos):
                        loop = False
                        game = False
                        run = False
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


pygame.quit()

# start_ticks = pygame.time.get_ticks()
#
# count_down_time = 90
#
# font = pygame.font.SysFont('comicsans', 60)
# seconds = (pygame.time.get_ticks() - start_ticks) / 1000
# text = font.render(f'Time: {seconds}', 1, (255, 255, 255))
# window.blit(text, (320, 320))
# print(seconds)