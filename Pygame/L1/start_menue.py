import pygame

pygame.init()

screen_x = 1280  # Screen dimension x
screen_y = 720  # Screen dimension y

window = pygame.display.set_mode((screen_x, screen_y))

x = input("Play? ")
if x == 'y':
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    import main

else:
    print("NOPE")

