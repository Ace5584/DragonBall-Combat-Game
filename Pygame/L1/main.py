import pygame
pygame.init()

clock = pygame.time.Clock()

screen_x = 1280
screen_y = 720
window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("My Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
idle = pygame.image.load('standing.png')

x = 50
y = 660
width = 64
height = 64
vol = 10
left = False
right = False
walk_count = 0

run = True
jump = False
jump_count = 10

def redraw_window():
    clock.tick(27)
    global walk_count
    window.blit(bg, (0, 0))
    if walk_count+1 >= 27:
        walk_count = 0
    elif left:
        window.blit(walkLeft[walk_count//3], (x, y))
        walk_count += 1
        print("LEFT")
    elif right:
        window.blit(walkRight[walk_count//3], (x, y))
        walk_count += 1
        print("RIGHT")
    else:
        window.blit(idle, (x, y))

    pygame.display.update()

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > vol or keys[pygame.K_LEFT] and x > vol:
        print("KEY")
        x -= vol
        left = True
        right = False
    elif keys[pygame.K_d] and x < screen_x - vol - width or keys[pygame.K_RIGHT] and x < screen_x - vol - width:
        x += vol
        left = False
        right = True
    else:
        right = False
        left = False
        walk_count = 0
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
            #right = False
            #left = False
            walk_count = 0
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
    redraw_window()

pygame.quit()
