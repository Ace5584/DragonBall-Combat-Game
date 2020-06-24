import pygame
import buttons

pygame.init()

screen_x = 1280  # Screen dimension x
screen_y = 720  # Screen dimension y
window = pygame.display.set_mode((screen_x, screen_y))

bg = pygame.image.load('bg.jpg')  # Importing background image
width = 120
height = 60
play_btn = buttons.button(screen_x / 2 - width / 2 - 80, screen_y / 2 - height / 2, width, height, (0, 255, 0), "Play")
quit_btn = buttons.button(screen_x / 2 - width / 2 + 80, screen_y / 2 - height / 2, width, height, (0, 255, 0), "Exit Game")
dim_screen = pygame.Surface((screen_x, screen_y)).convert_alpha()
dim_screen.fill((0, 0, 0, 130))



menu = True

while menu:
    window.blit(bg, (0, 0))
    window.blit(dim_screen, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        play_btn.draw(window)
        quit_btn.draw(window)
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn.is_over(pos):
                import main
                if main.game_quit:
                    menu = False
            if quit_btn.is_over(pos):
                menu = False
        if event.type == pygame.MOUSEMOTION:
            if play_btn.is_over(pos):
                play_btn.color = (255, 0, 0)
            elif not play_btn.is_over(pos):
                play_btn.color = (0, 255, 0)
            if quit_btn.is_over(pos):
                quit_btn.color = (255, 0, 0)
            elif not play_btn.is_over(pos):
                quit_btn.color = (0, 255, 0)
        pygame.display.update()
    else:
        None

pygame.quit()

