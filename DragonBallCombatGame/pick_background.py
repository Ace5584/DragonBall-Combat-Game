import pygame
import buttons
import redraw_window

exit_game = False

def pick_background(win):
    pygame.init()
    window = pygame.display.set_mode((1280, 720))
    city_1 = pygame.image.load('background/city_1.png')
    city_2 = pygame.image.load('background/city_2.png')
    city_3 = pygame.image.load('background/city_3.png')
    city_4 = pygame.image.load('background/city_4.png')
    bg = pygame.image.load('background/no_character_bg.png')  # Importing background image
    city_1_btn_red = pygame.image.load('background/btn/city_1_btn_red.png')
    city_1_btn_yellow = pygame.image.load('background/btn/city_1_btn_yellow.png')
    city_2_btn_red = pygame.image.load('background/btn/city_2_btn_red.png')
    city_2_btn_yellow = pygame.image.load('background/btn/city_2_btn_yellow.png')
    city_3_btn_red = pygame.image.load('background/btn/city_3_btn_red.png')
    city_3_btn_yellow = pygame.image.load('background/btn/city_3_btn_yellow.png')
    city_4_btn_red = pygame.image.load('background/btn/city_4_btn_red.png')
    city_4_btn_yellow = pygame.image.load('background/btn/city_4_btn_yellow.png')

    hover_btn = pygame.mixer.Sound('sound/hover_btn.wav')

    city_1_btn = buttons.button(250, 220, 330, 190, (255, 255, 255), '', city_1_btn_red)
    city_2_btn = buttons.button(650, 220, 330, 190, (255, 255, 255), '', city_2_btn_red)
    city_3_btn = buttons.button(250, 450, 330, 190, (255, 255, 255), '', city_3_btn_red)
    city_4_btn = buttons.button(650, 450, 330, 190, (255, 255, 255), '', city_4_btn_red)
    select = True

    play_1 = True
    play_2 = True
    play_3 = True
    play_4 = True

    while select:
        global exit_game

        window.blit(bg, (0, 0))

        city_1_btn.draw(window, False)
        city_2_btn.draw(window, False)
        city_3_btn.draw(window, False)
        city_4_btn.draw(window, False)

        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                select = False
                exit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if city_1_btn.is_over(pos):
                    redraw_window.bg = city_1
                    select = False
                if city_2_btn.is_over(pos):
                    redraw_window.bg = city_2
                    select = False
                if city_3_btn.is_over(pos):
                    redraw_window.bg = city_3
                    select = False
                if city_4_btn.is_over(pos):
                    redraw_window.bg = city_4
                    select = False

            if event.type == pygame.MOUSEMOTION:
                if city_1_btn.is_over(pos):
                    if play_1:
                        hover_btn.play()
                        play_1 = False
                    city_1_btn.image = city_1_btn_yellow
                elif not city_1_btn.is_over(pos):
                    city_1_btn.image = city_1_btn_red
                    play_1 = True
                if city_2_btn.is_over(pos):
                    if play_2:
                        hover_btn.play()
                        play_2 = False
                    city_2_btn.image = city_2_btn_yellow
                elif not city_2_btn.is_over(pos):
                    play_2 = True
                    city_2_btn.image = city_2_btn_red
                if city_3_btn.is_over(pos):
                    if play_3:
                        hover_btn.play()
                        play_3 = False
                    city_3_btn.image = city_3_btn_yellow
                elif not city_3_btn.is_over(pos):
                    play_3 = True
                    city_3_btn.image = city_3_btn_red
                if city_4_btn.is_over(pos):
                    if play_4:
                        hover_btn.play()
                        play_4 = False
                    city_4_btn.image = city_4_btn_yellow
                elif not city_2_btn.is_over(pos):
                    play_4 = True
                    city_4_btn.image = city_4_btn_red
