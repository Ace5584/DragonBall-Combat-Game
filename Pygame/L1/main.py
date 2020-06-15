import pygame
pygame.init()

screen_x = 500
screen_y = 600
window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("My Game")

x = 20
y = 20
width = 50
height = 50
vol = 10

run = True
jump = False
jump_count = 10

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vol:
        x -= vol
    if keys[pygame.K_RIGHT] and x < screen_x - vol - width:
        x += vol
    if not jump:
        if keys[pygame.K_UP] and y > vol:
            y -= vol
        if keys[pygame.K_DOWN] and y < screen_y - vol - height:
            y += vol
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        #if jump_count >= -10:

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
    pygame.display.update()
pygame.quit()
