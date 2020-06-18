import pygame

pygame.init()
clock = pygame.time.Clock()

screen_x = 1280
screen_y = 720

window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("My Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png'), ]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
c2_walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
               pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
               pygame.image.load('L7E.png'), pygame.image.load('L8E.png')]
c2_walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                pygame.image.load('R7E.png'), pygame.image.load('R8E.png')]

for x in range(4):
    walkRight = walkRight + walkRight
    walkLeft = walkLeft + walkLeft
    c2_walkRight = c2_walkRight + c2_walkRight
    c2_walkLeft = c2_walkLeft + c2_walkLeft
    print("A")
bg = pygame.image.load('bg.jpg')


class player():
    def __init__(self, x, y, width, height, left, text_location, player_name):
        font = pygame.font.Font('freesansbold.ttf', 18)
        self.player_information = font.render(player_name, False, (255, 255, 255))
        self.text_location = text_location
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vol = 10
        if left:
            self.left = True
            self.right = False
        else:
            self.right = True
            self.left = False
        self.walk_count = 0
        self.jump = False
        self.jump_count = 10
        self.bullets = list()
        self.bullet_count = 10
        self.walking = bool()
        self.hitbox = (self.x+20, self.y, 28, 60)

    def draw(self, win, character):
        if character == 1:
            if p1.walking:
                if self.walk_count + 1 >= len(walkLeft):
                    self.walk_count = 0
                elif self.left:
                    win.blit(walkLeft[round(self.walk_count // 3)], (self.x, self.y))
                    self.walk_count += 1
                elif self.right:
                    win.blit(walkRight[round(self.walk_count // 3)], (self.x, self.y))
                    self.walk_count += 1
            else:
                if self.left:
                    win.blit(walkLeft[0], (int(self.x), int(self.y)))
                else:
                    win.blit(walkRight[0], (int(self.x), int(self.y)))
        elif character == 2:
            if p2.walking:
                if self.walk_count + 1 >= len(c2_walkLeft):
                    self.walk_count = 0
                elif self.left:
                    win.blit(c2_walkLeft[round(self.walk_count // 3)], (self.x, self.y))
                    self.walk_count += 1
                elif self.right:
                    win.blit(c2_walkRight[round(self.walk_count // 3)], (self.x, self.y))
                    self.walk_count += 1
            else:
                if self.left:
                    win.blit(c2_walkLeft[0], (int(self.x), int(self.y)))
                else:
                    win.blit(c2_walkRight[0], (int(self.x), int(self.y)))


class projectile():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.vol = 14 * direction

    def shoot_bullet(self, win, color):
        pygame.draw.circle(win, color, (self.x, self.y), 5)


def movement(player, wasd):
    global bullet_count
    shooting_direction = int()
    for bullet in player.bullets:
        if 0 < bullet.x < screen_x:
            bullet.x += bullet.vol
        else:
            player.bullets.pop(player.bullets.index(bullet))
    keys = pygame.key.get_pressed()
    if wasd:
        key_shoot = keys[pygame.K_q]
        key_left = keys[pygame.K_a]
        key_right = keys[pygame.K_d]
        key_up = keys[pygame.K_w]
    else:
        key_shoot = keys[pygame.K_SPACE]
        key_left = keys[pygame.K_LEFT]
        key_right = keys[pygame.K_RIGHT]
        key_up = keys[pygame.K_UP]

    if key_shoot:
        if player.left:
            shooting_direction = -1
        else:
            shooting_direction = 1

        player.bullets.append(projectile(round(player.x + player.width / 2), round(player.y + player.height / 2), shooting_direction))

    if key_left and player.x > player.vol:
        player.x -= player.vol
        player.left = True
        player.right = False
        walking = True
    elif key_right and player.x < screen_x - player.vol - player.width:
        player.x += player.vol
        player.left = False
        player.right = True
        walking = True
    else:
        walking = False
        p1.walk_count = 0
    if not player.jump:
        if key_up:
            player.jump = True
            player.right = False
            player.left = False
            p1.walk_count = 0
    else:
        if player.jump_count >= -10:
            n = 1
            if player.jump_count < 0:
                n = -1
            player.y -= player.jump_count ** 2 / 2 * n
            player.jump_count -= 1
        else:
            player.jump = False
            player.jump_count = 10


def redraw_window():
    clock.tick(60)
    window.blit(bg, (0, 0))
    window.blit(p1.player_information, p1.text_location)
    window.blit(p2.player_information, p2.text_location)
    p1.draw(window, 1)
    p2.draw(window, 2)
    for z in p1.bullets:
        z.shoot_bullet(window, (255, 255, 0))
    for z in p2.bullets:
        z.shoot_bullet(window, (255, 0, 0))
    pygame.display.update()


p1 = player(50, 650, 64, 64, False, (0, 0), "Player 1:")
p2 = player(1200, 650, 64, 64, True, (1200, 0), "Player 2:")
bullet_count = 0

run = True
while run:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    movement(p1, True)
    movement(p2, False)
    redraw_window()

pygame.quit()
