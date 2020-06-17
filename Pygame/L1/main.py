import pygame

pygame.init()
clock = pygame.time.Clock()

walking = True
screen_x = 1280
screen_y = 720
window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("My Game")

run = True

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png'), ]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
for x in range(3):
    walkRight = walkRight + walkRight
    walkLeft = walkLeft + walkLeft
bg = pygame.image.load('bg.jpg')
idle = pygame.image.load('standing.png')

shooting_direction = 0


class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vol = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.jump = False
        self.jump_count = 10

    def draw(self, win):
        if walking:
            if self.walk_count + 1 >= 216:
                self.walk_count = 0
            elif self.left:
                win.blit(walkLeft[round(self.walk_count // 3)], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(walkRight[round(self.walk_count // 3)], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(walkRight[0], (self.x, self.y))


class projectile():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.vol = 14*direction

    def shoot_bullet(self, win):
        pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 5)


def redraw_window():
    clock.tick(27)
    window.blit(bg, (0, 0))
    p1.draw(window)
    for z in bullets:
        z.shoot_bullet(window)
    pygame.display.update()


p1 = player(50, 650, 64, 64)
bullets = []
bullet_count = 0

while run:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if 0 < bullet.x < screen_x:
            bullet.x += bullet.vol
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q] or keys[pygame.K_SPACE]:
        if p1.left:
            shooting_direction = -1
        else:
            shooting_direction = 1
        if len(bullets) < 6:
            bullets.append(projectile(round(p1.x + p1.width / 2), round(p1.y + p1.height / 2), shooting_direction))

    if keys[pygame.K_a] and p1.x > p1.vol or keys[pygame.K_LEFT] and p1.x > p1.vol:
        p1.x -= p1.vol
        p1.left = True
        p1.right = False
        walking = True
    elif keys[pygame.K_d] and p1.x < screen_x - p1.vol - p1.width or keys[pygame.K_RIGHT] and p1.x < screen_x - p1.vol - p1.width:
        p1.x += p1.vol
        p1.left = False
        p1.right = True
        walking = True
    else:
        walking = False
        p1.walk_count = 0
    if not p1.jump:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            p1.jump = True
            right = False
            left = False
            p1.walk_count = 0
    else:
        if p1.jump_count >= -10:
            n = 1
            if p1.jump_count < 0:
                n = -1
            p1.y -= p1.jump_count ** 2 / 2 * n
            p1.jump_count -= 1
        else:
            p1.jump = False
            p1.jump_count = 10
    redraw_window()

pygame.quit()
