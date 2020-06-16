import pygame
pygame.init()

screen_x = 1280
screen_y = 720
window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("My Game")


x = 50
y = 230
width = 50
height = 50
vol = 10
left = False
right = False
walk_count = 0

run = True
jump = False
jump_count = 10

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > vol or keys[pygame.K_LEFT] and x > vol:
        x -= vol
    if keys[pygame.K_d] and x < screen_x - vol - width or keys[pygame.K_RIGHT] and x < screen_x - vol - width:
        x += vol
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jump_count >= -10:
            n = 1
            if jump_count < 0:
                n = -1
            y -= jump_count**2 /2 * n
            jump_count -= 1
        else:
            jump = False
            jump_count = 10

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
    pygame.display.update()
pygame.quit()
