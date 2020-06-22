import pygame
import projectile

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png'), ]  # Important
# character 1 walking right png
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]  # Important
# character 1 walking left png
c2_walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
               pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
               pygame.image.load('L7E.png'), pygame.image.load('L8E.png')]  # Important character 2 walking left png
c2_walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                pygame.image.load('R7E.png'), pygame.image.load('R8E.png')]  # Important character 2 walking right png

pygame.init()
shoot_sound = pygame.mixer.Sound('laser_shoot.wav')
hit = pygame.mixer.Sound('get_shot.wav')


for x in range(4):
    walkRight = walkRight + walkRight
    walkLeft = walkLeft + walkLeft
    c2_walkRight = c2_walkRight + c2_walkRight
    c2_walkLeft = c2_walkLeft + c2_walkLeft


class Player():
    def __init__(self, x, y, width, height, left, text_location, player_name):
        self.health = 200
        self.x = x  # Player coordination x
        self.y = y  # Player coordination y
        self.default_x = x  # Original Player coordination x
        self.default_y = y  # Original Player coordination y
        self.width = width  # Player width
        self.height = height  # Player height
        self.vol = 6  # Player velocity
        if left:
            self.left = True
            self.right = False
        else:
            self.right = True
            self.left = False
        self.walk_count = 0  # counting each frame of the character
        self.jump = False  # Determine weather the character is jumping or not
        self.jump_count = 10  # counting the frames when the character jumps
        self.bullets = list()  # A list of bullets for the character
        self.bullet_count = 10  # Counting the remaining bullets for the character
        self.walking = bool()  # determine weather the character is walking
        self.hit_box = (self.x + 20, self.y, 28, 60)  # hit box of the character
        self.font = pygame.font.SysFont('comicsans', 25, True)  # Font for the words
        self.text_location = text_location  # Location for the text printing the player name
        self.player_information = self.font.render(player_name, False, (255, 255, 255))  # Displaying player name
        self.temp = list(text_location)  # temporary list for bullet remaining text location
        self.temp[1] += 20  # changing location of the bullet remaining text
        self.bullet_count_text_location = tuple(self.temp)  # changing temporary list into bullet count text location
        # tuple
        self.player_bullet_count = self.font.render(f'BULLET REMAINING: {self.bullet_count}', False, (255, 255, 255))
        # allocating text to bullet remaining
        self.temp1 = list(self.bullet_count_text_location)  # temporary list for health bar text location
        self.temp1[1] += 20  # changing location of the bullet remaining text
        self.bullet_damage = 30
        self.temp1.append(self.health)
        self.temp1.append(20)
        self.health_bar_location = tuple(self.temp1)  # changing temporary list into health bar text location tuple
        self.bottom_health_bar_location = tuple(self.temp1)
        self.bullet_delay = 0  # Bullet Delay variable to prevent shooting spamming bullets
        self.bottom_health_bar = None
        self.die = False
        self.time_remaining = 90

    def draw(self, win, character):
        if character == 1:
            if self.walking:
                if self.walk_count + 1 >= len(walkLeft):
                    self.walk_count = 0
                elif self.left:
                    win.blit(walkLeft[int(round(self.walk_count // 3))], (int(self.x), int(self.y)))
                    self.walk_count += 1
                elif self.right:
                    win.blit(walkRight[int(round(self.walk_count // 3))], (int(self.x), int(self.y)))
                    self.walk_count += 1
            else:
                if self.left:
                    win.blit(walkLeft[0], (int(self.x), int(self.y)))
                else:
                    win.blit(walkRight[0], (int(self.x), int(self.y)))
            self.hit_box = (self.x + 17, self.y + 11, 29, 52)
            # pygame.draw.rect(window, (255, 0, 0), self.hit_box, 2)
        if character == 2:
            if self.walking:
                if self.walk_count + 1 >= len(c2_walkLeft):
                    self.walk_count = 0
                elif self.left:
                    win.blit(c2_walkLeft[round(self.walk_count // 3)], (int(self.x), int(self.y)))
                    self.walk_count += 1
                elif self.right:
                    win.blit(c2_walkRight[round(self.walk_count // 3)], (int(self.x), int(self.y)))
                    self.walk_count += 1
            else:
                if self.left:
                    win.blit(c2_walkLeft[0], (int(self.x), int(self.y)))
                else:
                    win.blit(c2_walkRight[0], (int(self.x), int(self.y)))
            self.hit_box = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(window, (255, 0, 0), self.hit_box, 2)


    def freeze(self, win, character):
        if character == 1:
            if self.left:
                win.blit(walkLeft[0], (int(self.x), int(self.y)))
            else:
                win.blit(walkRight[0], (int(self.x), int(self.y)))
        if character == 2:
            if self.left:
                win.blit(c2_walkLeft[0], (int(self.x), int(self.y)))
            else:
                win.blit(c2_walkRight[0], (int(self.x), int(self.y)))

    def movement(self, wasd, enemy, win, screen_x, screen_y):

        if self.bullet_delay >= 0:
            self.bullet_delay += 1
        if self.bullet_delay > 3:
            self.bullet_delay = 0

        for bullet in self.bullets:
            if bullet.y + bullet.bullet_radius > enemy.hit_box[1] and bullet.y - bullet.bullet_radius < enemy.hit_box[
                1] + enemy.hit_box[3]:
                if bullet.x + bullet.bullet_radius > enemy.hit_box[0] and bullet.x - bullet.bullet_radius < \
                        enemy.hit_box[0] + enemy.hit_box[2]:
                    hit.play()
                    if enemy.temp1[2] > 0:
                        if enemy.temp1[2] - self.bullet_damage > 0:
                            enemy.temp1[2] = enemy.temp1[2] - self.bullet_damage
                        else:
                            enemy.temp1[2] = 0

                        enemy.health_bar_location = tuple(enemy.temp1)
                        pygame.draw.rect(win, (255, 0, 0), self.health_bar_location)
                        self.bullets.pop(self.bullets.index(bullet))
                        self.health -= 30
                        self.die = False
                        continue
                    else:
                        self.die = True
            if 0 < bullet.x < screen_x:
                bullet.x += bullet.vol
            else:
                self.bullets.pop(self.bullets.index(bullet))
        keys = pygame.key.get_pressed()
        if wasd:
            key_shoot = keys[pygame.K_q]
            key_left = keys[pygame.K_a]
            key_right = keys[pygame.K_d]
            key_up = keys[pygame.K_w]
            key_down = keys[pygame.K_s]
        else:
            key_shoot = keys[pygame.K_SPACE]
            key_left = keys[pygame.K_LEFT]
            key_right = keys[pygame.K_RIGHT]
            key_up = keys[pygame.K_UP]
            key_down = keys[pygame.K_DOWN]
        if self.bullet_delay == 0:
            if key_shoot:
                if self.bullet_count > 0:
                    if self.left:
                        shooting_direction = -1
                    else:
                        shooting_direction = 1
                    self.bullets.append(
                        projectile.projectile(round(self.x + self.width / 2), round(self.y + self.height / 2),
                                              shooting_direction))
                    self.bullet_count -= 1
                    self.player_bullet_count = self.font.render(f'BULLET REMAINING: {self.bullet_count}', False,
                                                                (255, 255, 255))
                    shoot_sound.play()

        if key_left and self.x > self.vol:
            self.x -= self.vol
            self.left = True
            self.right = False
            self.walking = True
        elif key_right and self.x < screen_x - self.vol - self.width:
            self.x += self.vol
            self.left = False
            self.right = True
            self.walking = True
        else:
            self.walking = False
            self.walk_count = 0
        if key_down:
            self.y = self.default_y
            self.jump = False
            self.jump_count = 10
        else:
            if not self.jump:
                if key_up:
                    self.jump = True
                    self.walk_count = 0
            else:
                if self.jump_count >= -10:
                    n = 1
                    if self.jump_count < 0:
                        n = -1
                    self.y -= self.jump_count ** 2 / 2 * n
                    self.jump_count -= 1
                else:
                    self.jump = False
                    self.jump_count = 10

    def is_dead(self):
        return self.die
