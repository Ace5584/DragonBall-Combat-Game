import pygame
import buttons
import main

pygame.init()

screen_x = 1280  # Screen dimension x
screen_y = 720  # Screen dimension y
window = pygame.display.set_mode((screen_x, screen_y))

bg = pygame.image.load('background/start_bg.png')  # Importing background image
play_btn_img = pygame.image.load('background/btn/start_btn.png')
quit_btn_img = pygame.image.load('background/btn/quit_btn.png')
play_btn_toggle_img = pygame.image.load('background/btn/start_btn_toggle.png')
quit_btn_toggle_img = pygame.image.load('background/btn/quit_btn_toggle.png')

width = 202
height = 60
play_btn = buttons.button(screen_x / 2 - width / 2 - 130, screen_y / 2 - height / 2 - 100, width, height, (0, 0, 255), '', play_btn_img)
quit_btn = buttons.button(screen_x / 2 - width / 2 + 130, screen_y / 2 - height / 2 - 100, width, height, (0, 0, 255), '', quit_btn_img)
dim_screen = pygame.Surface((screen_x, screen_y)).convert_alpha()
dim_screen.fill((0, 0, 0, 130))

menu = True

while menu:
    window.blit(bg, (0, 0))
    #window.blit(dim_screen, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        play_btn.draw(window, False)
        quit_btn.draw(window, False)
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn.is_over(pos):
                main.game_loop()
                if main.game_quit:
                    menu = False
            if quit_btn.is_over(pos):
                menu = False
        if event.type == pygame.MOUSEMOTION:
            if play_btn.is_over(pos):
                play_btn.image = play_btn_toggle_img
            elif not play_btn.is_over(pos):
                play_btn.image = play_btn_img
            if quit_btn.is_over(pos):
                quit_btn.image = quit_btn_toggle_img
            elif not play_btn.is_over(pos):
                quit_btn.image = quit_btn_img
        pygame.display.update()
    else:
        None

pygame.quit()

