import pygame

screen_x = 1280  # Screen dimension x
screen_y = 720  # Screen dimension y

window = pygame.display.set_mode((screen_x, screen_y))

x = input("Play? ")
if x == 'y':
    import main
else:
    print("NOPE")

