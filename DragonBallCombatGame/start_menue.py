import pygame
import buttons
import main
import pick_background
import redraw_window

pygame.init()

screen_x = 1280  # Screen dimension x
screen_y = 720  # Screen dimension y
window = pygame.display.set_mode((screen_x, screen_y))

bg = pygame.image.load('background/dragon_ball_z_bg.png')  # Importing background image
play_btn_img = pygame.image.load('background/btn/play_btn_red.png')
quit_btn_img = pygame.image.load('background/btn/exit_btn_red.png')
play_btn_toggle_img = pygame.image.load('background/btn/play_btn_yellow.png')
quit_btn_toggle_img = pygame.image.load('background/btn/exit_btn_yellow.png')

width = 300
height = 95
play_btn = buttons.button(screen_x / 2 - width / 2 - 200, screen_y / 2 - height / 2 - 50, width, height, (0, 0, 255), '', play_btn_img)
quit_btn = buttons.button(screen_x / 2 - width / 2 + 200, screen_y / 2 - height / 2 - 50, width, height, (0, 0, 255), '', quit_btn_img)
dim_screen = pygame.Surface((screen_x, screen_y)).convert_alpha()
dim_screen.fill((0, 0, 0, 130))

menu = True
background = True

while menu:
    window.blit(bg, (0, 0))
    #window.blit(dim_screen, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if menu:
            play_btn.draw(window, False)
            quit_btn.draw(window, False)
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn.is_over(pos):
                pick_background.pick_background(window)
                if pick_background.exit_game:
                    menu = False
                else:
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

pygame.quit()

