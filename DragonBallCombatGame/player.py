import pygame
import AAfilledRoundedRect
import projectile

walkRight = [pygame.image.load('goku/R.png')]
walkLeft = [pygame.image.load('goku/L.png')]
standRight = [pygame.image.load('goku/standR_1.png'), pygame.image.load('goku/standR_1.png')]
standLeft = [pygame.image.load('goku/standL_1.png'), pygame.image.load('goku/standL_1.png')]
vanish = pygame.image.load('goku/vanish.png')

c2_walkRight = [pygame.image.load('Vegeta/R.png')]
c2_walkLeft = [pygame.image.load('Vegeta/L.png')]
c2_standRight = [pygame.image.load('Vegeta/stand_R_1.png'), pygame.image.load('Vegeta/stand_R_1.png')]
c2_standLeft = [pygame.image.load('Vegeta/stand_L_1.png'), pygame.image.load('Vegeta/stand_L_1.png')]
c2_vanish = pygame.image.load('Vegeta/vanish.png')

punch_left = [pygame.image.load('goku/L_punch_1.png'), pygame.image.load('goku/L_punch_2.png'),
                 pygame.image.load('goku/L_punch_2.png'), pygame.image.load('goku/L_punch_4.png'),
                 pygame.image.load('goku/L_kick_1.png'), pygame.image.load('goku/L_kick_2.png'),
                 pygame.image.load('goku/L_kick_3.png'), pygame.image.load('goku/L_kick_4.png')]
punch_right = [pygame.image.load('goku/R_punch_1.png'), pygame.image.load('goku/R_punch_2.png'),
                  pygame.image.load('goku/R_punch_2.png'), pygame.image.load('goku/R_punch_4.png'),
                  pygame.image.load('goku/R_kick_1.png'), pygame.image.load('goku/R_kick_2.png'),
                  pygame.image.load('goku/R_kick_3.png'), pygame.image.load('goku/R_kick_4.png')]

c2_punch_left = [pygame.image.load('Vegeta/L_punch_1.png'), pygame.image.load('Vegeta/L_punch_2.png'),
              pygame.image.load('Vegeta/L_punch_2.png'), pygame.image.load('Vegeta/L_punch_4.png'),
              pygame.image.load('Vegeta/L_kick_1.png'), pygame.image.load('Vegeta/L_kick_2.png'),
              pygame.image.load('Vegeta/L_kick_3.png'), pygame.image.load('Vegeta/L_kick_4.png')]
c2_punch_right = [pygame.image.load('Vegeta/R_punch_1.png'), pygame.image.load('Vegeta/R_punch_2.png'),
               pygame.image.load('Vegeta/R_punch_2.png'), pygame.image.load('Vegeta/R_punch_4.png'),
               pygame.image.load('Vegeta/R_kick_1.png'), pygame.image.load('Vegeta/R_kick_2.png'),
               pygame.image.load('Vegeta/R_kick_3.png'), pygame.image.load('Vegeta/R_kick_4.png')]

left_move_teleport = [pygame.image.load('goku/L_move_forward.png'), pygame.image.load('goku/L_move_forward2.png')]
right_move_teleport = [pygame.image.load('goku/R_move_forward.png'), pygame.image.load('goku/R_move_forward2.png')]

c2_left_move_teleport = [pygame.image.load('Vegeta/L_move_forward.png'), pygame.image.load('Vegeta/L_move_forward_2.png')]
c2_right_move_teleport = [pygame.image.load('Vegeta/R_move_forward.png'), pygame.image.load('Vegeta/R_move_forward_2.png')]

shoot_left = [pygame.image.load('goku/L_attack_1.png'), pygame.image.load('goku/L_attack_2.png'),
              pygame.image.load('goku/L_attack_3.png')]
shoot_right = [pygame.image.load('goku/R_attack_1.png'), pygame.image.load('goku/R_attack_2.png'),
               pygame.image.load('goku/R_attack_3.png')]

c2_shoot_left = [pygame.image.load('Vegeta/L_attack_1.png'), pygame.image.load('Vegeta/L_attack_2.png'),
                 pygame.image.load('Vegeta/L_attack_3.png')]
c2_shoot_right = [pygame.image.load('Vegeta/R_attack_1.png'), pygame.image.load('Vegeta/R_attack_2.png'),
                  pygame.image.load('Vegeta/R_attack_3.png')]

player1_die_left = [pygame.image.load('goku/die.png'), pygame.image.load('goku/die1.png'),
                    pygame.image.load('goku/die2.png'), pygame.image.load('goku/die3.png'),
                    pygame.image.load('goku/die4.png')]
player1_die_right = [pygame.image.load('goku/R_die.png'), pygame.image.load('goku/R_die1.png'),
                     pygame.image.load('goku/R_die2.png'), pygame.image.load('goku/R_die3.png'),
                     pygame.image.load('goku/R_die4.png')]

player2_die_left = [pygame.image.load('Vegeta/die.png'), pygame.image.load('Vegeta/die1.png'),
                    pygame.image.load('Vegeta/die2.png'), pygame.image.load('Vegeta/die3.png')]
player2_die_right = [pygame.image.load('Vegeta/R_die.png'), pygame.image.load('Vegeta/R_die1.png'),
                     pygame.image.load('Vegeta/R_die2.png'), pygame.image.load('Vegeta/R_die3.png')]


blue_defend = pygame.image.load('character/blue_g.png')
red_defend = pygame.image.load('character/red_g.png')

pygame.init()
shoot_sound = pygame.mixer.Sound('sound/shoot_sound.wav')
hit = pygame.mixer.Sound('sound/get_shot.wav')
explode_sound = pygame.mixer.Sound('sound/explotion.wav')

for x in range(20):
    walkRight = walkRight + walkRight
    walkLeft = walkLeft + walkLeft
    c2_walkRight = c2_walkRight + c2_walkRight
    c2_walkLeft = c2_walkLeft + c2_walkLeft

for x in range(4):
    c2_walkRight = c2_walkRight + c2_walkRight
    c2_walkLeft = c2_walkLeft + c2_walkLeft


class Player():
    def __init__(self, x, y, width, height, left, text_location, player_name, character, screen_x, screen_y):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.health = 200
        self.shield = 100
        self.x = x  # Player coordination x
        self.y = y  # Player coordination y
        self.character = character
        if self.character == 1:
            self.hit_box = (self.x, self.y, 100, 64)
        elif self.character == 2:
            self.hit_box = (self.x, self.y, 80, 64)
        self.default_x = x  # Original Player coordination x
        self.default_y = y  # Original Player coordination y
        self.width = width  # Player width
        self.height = height  # Player height
        self.vol = 6  # Player velocity
        self.knock_down = False
        if left:
            self.left = True
            self.right = False
        else:
            self.right = True
            self.left = False
        self.walk_count = 0  # counting each frame of the character
        self.jump = False  # Determine weather the character is jumping or not
        self.jump_count = 13  # counting the frames when the character jumps
        self.first_press_jump = True
        self.double_jump = False
        self.bullets = list()  # A list of bullets for the character
        self.bullet_count = 10  # Counting the remaining bullets for the character
        self.walking = bool()  # determine weather the character is walking
        self.hit_box = (self.x + 20, self.y, 28, 60)  # hit box of the character
        self.font = pygame.font.Font('ImminentLine.ttf', 15)  # Font for the words
        self.text_location = text_location  # Location for the text printing the player name
        self.player_information = self.font.render(player_name, False, (255, 255, 255))  # Displaying player name
        self.temp = list(text_location)  # temporary list for bullet remaining text location
        self.temp[1] += 20  # changing location of the bullet remaining text
        self.bullet_count_text_location = tuple(self.temp)  # changing temporary list into bullet count text location
        # tuple
        # allocating text to bullet remaining
        self.temp1 = list(self.bullet_count_text_location)  # temporary list for health bar text location
        self.temp1[1] += 20  # changing location of the bullet remaining text
        if self.character == 1:
            self.temp1[0] += 150
        elif self.character == 2:
            self.temp1[0] -= 120
        self.bullet_damage = 30
        self.temp1.append(self.health)
        self.temp1.append(20)
        self.health_bar_location = tuple(self.temp1)  # changing temporary list into health bar text location tuple
        self.bottom_health_bar_location = tuple(self.temp1)
        temp_bullet_bar = self.temp1
        self.bullet_bar_x = temp_bullet_bar[0]
        self.bullet_bar_y = temp_bullet_bar[1] + 25
        self.bullet_bar_w = self.bullet_count * 20
        self.bullet_bar_h = temp_bullet_bar[3] / 2
        self.bullet_bar_bottom_w = self.bullet_count * 20
        self.bullet_bar_bottom_x = temp_bullet_bar[0]
        self.bullet_delay = 0  # Bullet Delay variable to prevent shooting spamming bullets
        self.bottom_health_bar = None
        self.die = False
        self.time_remaining = 90
        self.start_ticks = pygame.time.get_ticks()
        self.seconds = self.start_ticks / 1000
        self.reset_time = True
        self.temp_time = 0
        self.shield_timer = 0
        self.temp3 = list(text_location)  # temporary list for bullet remaining text location
        self.temp3[1] += 80  # changing location of the bullet remaining text
        if self.character == 1:
            self.temp3[0] += 150
        elif self.character == 2:
            self.temp3[0] += 50
        self.shield_timer_location = tuple(self.temp3)  # changing temporary list into bullet count text located
        self.stabbing = False
        self.stab_count = 0
        self.vanish = False
        self.going_down = False
        self.teleport_remain = 3
        self.teleport = False
        self.teleport_delay = 0
        self.key = None
        teleport_temp = list(text_location)
        if self.character == 1:
            self.teleport_x = teleport_temp[0] + 260
        elif self.character == 2:
            self.teleport_x = teleport_temp[0] - 120
        self.teleport_y = teleport_temp[1] + 80
        self.shoot_status = False
        self.shoot_image_count = 0
        self.explode = False
        self.get_punch_back = False
        self.death_direction = 0
        self.knock_down_count = 0
        self.knock_down_direction = 0
        self.shooting_direction = 0

        self.teleport_count = 0


    def draw(self, win, character):
        if character == 1:
            if not self.shoot_status:
                if self.teleport and self.teleport_remain > 0:
                    self.walking = False
                    if self.right:
                        print(self.teleport_count)
                        if 0 <= self.teleport_count < 1:
                            win.blit(right_move_teleport[round(self.teleport_count)], (int(self.x), int(self.y)))
                            self.teleport_count += 0.2
                            self.x += 1
                        elif 1 <= self.teleport_count < 2:
                            win.blit(vanish, (int(self.x), int(self.y)))
                            self.teleport_count += 0.2
                            self.x += 1
                        elif self.teleport_count > 2:
                            self.x = 1280 - 128
                            self.teleport_remain -= 1
                            self.teleport_count = 0
                    else:
                        if 0 <= self.teleport_count < 1:
                            win.blit(left_move_teleport[round(self.teleport_count)], (int(self.x), int(self.y)))
                            self.teleport_count += 0.2
                            self.x -= 1
                        elif 1 <= self.teleport_count < 2:
                            win.blit(vanish, (int(self.x), int(self.y)))
                            self.teleport_count += 0.2
                            self.x -= 1
                        elif self.teleport_count > 2:
                            self.x = 0
                            self.teleport_remain -= 1
                            self.teleport_count = 0
                else:
                    pass

                if not self.vanish:
                    if not self.knock_down:
                        if self.walking:
                            if self.walk_count + 1 >= len(walkLeft):
                                self.walk_count = 0
                            elif self.left:
                                win.blit(walkLeft[int(round(self.walk_count // 3))], (int(self.x), int(self.y - 10)))
                                self.walk_count += 1
                            elif self.right:
                                win.blit(walkRight[int(round(self.walk_count // 3))], (int(self.x), int(self.y - 10)))
                                self.walk_count += 1
                        elif not self.walking and not self.stabbing and not self.teleport:
                            if self.left:
                                win.blit(standLeft[0], (int(self.x), int(self.y)))
                            else:
                                win.blit(standRight[1], (int(self.x), int(self.y)))
                        self.hit_box = (self.x + 17, self.y + 11, 29, 52)
                        # pygame.draw.rect(window, (255, 0, 0), self.hit_box, 2)
                    elif self.knock_down:
                        if self.knock_down_direction > 0:  # Right
                            self.right = False
                            self.left = True

                            if 0 <= self.knock_down_count < 3:
                                win.blit(player1_die_right[round(self.knock_down_count)], (int(self.x), int(self.y)))
                                self.knock_down_count += 0.2
                                if self.x < self.screen_x - self.vol - self.width:
                                    self.x += 4
                            elif self.knock_down_count > 3:
                                self.knock_down = False
                                self.knock_down_count = 0
                        if self.knock_down_direction < 0:  # Left
                            self.right = True
                            self.left = False
                            if 0 <= self.knock_down_count < 3:
                                win.blit(player1_die_left[round(self.knock_down_count)], (int(self.x), int(self.y)))
                                self.knock_down_count += 0.2
                                if self.x > self.vol:
                                    self.x -= 4
                            elif self.knock_down_count > 3:
                                self.knock_down = False
                                self.knock_down_count = 0
                elif self.going_down:
                    win.blit(vanish, (int(self.x), int(self.y)))
                    self.walking = False
                    self.going_down = False
                    self.vanish = False
            else:
                self.walking = False
                if self.right:
                    if 0 <= self.shoot_image_count < 1:
                        win.blit(shoot_right[0], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if 1 <= self.shoot_image_count < 2:
                        win.blit(shoot_right[1], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if 2 <= self.shoot_image_count < 3:
                        win.blit(shoot_right[2], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if self.shoot_image_count >= 3:
                        self.shoot_image_count = 0
                else:
                    if 0 <= self.shoot_image_count < 1:
                        win.blit(shoot_left[0], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if 1 <= self.shoot_image_count < 2:
                        win.blit(shoot_left[1], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if 2 <= self.shoot_image_count < 3:
                        win.blit(shoot_left[2], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if self.shoot_image_count >= 3:
                        self.shoot_image_count = 0

        if character == 2:
            if not self.shoot_status:
                if self.teleport and self.teleport_remain > 0:
                    self.walking = False
                    if self.right:
                        print(self.teleport_count)
                        if 0 <= self.teleport_count < 1:
                            win.blit(c2_right_move_teleport[round(self.teleport_count)], (int(self.x), int(self.y)))
                            self.teleport_count += 0.2
                            self.x += 1
                        elif 1 <= self.teleport_count < 2:
                            win.blit(c2_vanish, (int(self.x), int(self.y)))
                            self.teleport_count += 0.2
                            self.x += 1
                        elif self.teleport_count > 2:
                            self.x = 1280 - 128
                            self.teleport_remain -= 1
                            self.teleport_count = 0
                    else:
                        if 0 <= self.teleport_count < 1:
                            win.blit(c2_left_move_teleport[round(self.teleport_count)], (int(self.x), int(self.y)))
                            self.teleport_count += 0.2
                            self.x -= 1
                        elif 1 <= self.teleport_count < 2:
                            win.blit(c2_vanish, (int(self.x), int(self.y)))
                            self.teleport_count += 0.2
                            self.x -= 1
                        elif self.teleport_count > 2:
                            self.x = 0
                            self.teleport_remain -= 1
                            self.teleport_count = 0
                else:
                    pass
                if not self.vanish:
                    if not self.knock_down:
                        if self.walking:
                            # self.y = 630
                            if self.walk_count + 1 >= len(walkLeft):
                                self.walk_count = 0
                            elif self.left:
                                win.blit(c2_walkLeft[int(round(self.walk_count // 3))], (int(self.x), int(self.y - 10)))
                                self.walk_count += 1
                            elif self.right:
                                win.blit(c2_walkRight[int(round(self.walk_count // 3))],
                                         (int(self.x), int(self.y - 10)))
                                self.walk_count += 1
                        elif not self.walking and not self.stabbing and not self.teleport:
                            if self.left:
                                win.blit(c2_standLeft[0], (int(self.x), int(self.y)))
                            else:
                                win.blit(c2_standRight[1], (int(self.x), int(self.y)))
                        self.hit_box = (self.x + 17, self.y + 11, 29, 52)
                        # pygame.draw.rect(window, (255, 0, 0), self.hit_box, 2)
                    elif self.knock_down:
                        self.walking = False
                        self.jump = False
                        self.stabbing = False
                        self.shoot_status = False
                        if self.knock_down_direction > 0:  # Right
                            if 0 <= self.knock_down_count < 3:
                                win.blit(player2_die_right[round(self.knock_down_count)], (int(self.x), int(self.y)))
                                self.knock_down_count += 0.2
                                if self.x < self.screen_x - self.vol - self.width:
                                    self.x += 4
                            elif self.knock_down_count > 3:
                                self.knock_down = False
                                self.knock_down_count = 0
                        if self.knock_down_direction < 0:  # Left
                            if 0 <= self.knock_down_count < 3:
                                win.blit(player2_die_left[round(self.knock_down_count)], (int(self.x), int(self.y)))
                                self.knock_down_count += 0.2
                                if self.x > self.vol:
                                    self.x -= 4
                            elif self.knock_down_count > 3:
                                self.knock_down = False
                                self.knock_down_count = 0
                elif self.going_down:
                    win.blit(c2_vanish, (int(self.x), int(self.y)))
                    self.walking = False
                    self.going_down = False
                    self.vanish = False
            else:
                self.walking = False
                if self.right:
                    if 0 <= self.shoot_image_count < 1:
                        win.blit(c2_shoot_right[0], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if 1 <= self.shoot_image_count < 2:
                        win.blit(c2_shoot_right[1], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if 2 <= self.shoot_image_count < 3:
                        win.blit(c2_shoot_right[2], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if self.shoot_image_count >= 3:
                        self.shoot_image_count = 0
                else:
                    if 0 <= self.shoot_image_count < 1:
                        win.blit(c2_shoot_left[0], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if 1 <= self.shoot_image_count < 2:
                        win.blit(c2_shoot_left[1], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if 2 <= self.shoot_image_count < 3:
                        win.blit(c2_shoot_left[2], (int(self.x), int(self.y)))
                        self.shoot_image_count += 0.2
                    if self.shoot_image_count >= 3:
                        self.shoot_image_count = 0

    def freeze(self, win, character):
        if character == 1:
            if self.left:
                win.blit(standLeft[0], (int(self.x), int(self.y)))
            else:
                win.blit(standRight[1], (int(self.x), int(self.y)))
        if character == 2:
            if self.left:
                win.blit(c2_standLeft[0], (int(self.x), int(self.y)))
            else:
                win.blit(c2_standRight[1], (int(self.x), int(self.y)))

    def movement(self, wasd, enemy, win):
        if self.bullet_delay >= 0:
            self.bullet_delay += 1
        if self.bullet_delay > 3:
            self.bullet_delay = 0

        if self.teleport_delay >= 0:
            self.teleport_delay += 1
        if self.teleport_delay > 3:
            self.teleport_delay = 0

        for bullet in self.bullets:
            if bullet.y + bullet.bullet_radius > enemy.hit_box[1] and bullet.y - bullet.bullet_radius < \
                    enemy.hit_box[1] + enemy.hit_box[3]:
                if bullet.x + bullet.bullet_radius > enemy.hit_box[0] and bullet.x - bullet.bullet_radius < \
                        enemy.hit_box[0] + enemy.hit_box[2]:
                    hit.play()
                    explode_sound.play()
                    if enemy.temp1[2] > 0:
                        if enemy.temp1[2] - self.bullet_damage > 0:
                            enemy.temp1[2] = enemy.temp1[2] - self.bullet_damage
                            if self.character == 2:
                                enemy.temp1[0] += self.bullet_damage
                        else:
                            enemy.temp1[2] = 0
                            self.die = True
                        enemy.knock_down = True
                        enemy.health_bar_location = tuple(enemy.temp1)
                        AAfilledRoundedRect.AAfilledRoundedRect(win, self.health_bar_location, (255, 0, 0), 1)
                        self.bullets.pop(self.bullets.index(bullet))
                        enemy.knock_down_direction = self.shooting_direction
                        self.die = False
                        self.explode = True
                        continue
                    else:
                        self.die = True


            if 0 < bullet.x < self.screen_x:
                bullet.x += bullet.vol
            else:
                self.bullets.pop(self.bullets.index(bullet))

        keys = pygame.key.get_pressed()
        if wasd:
            if self.knock_down:
                key_shoot = None
                key_left = None
                key_right = None
                key_up = None
                key_down = None
                key_stab = None
                key_vanish = keys[pygame.K_f]
            elif not self.knock_down:
                key_shoot = keys[pygame.K_q]
                key_left = keys[pygame.K_a]
                key_right = keys[pygame.K_d]
                key_up = keys[pygame.K_w]
                key_down = keys[pygame.K_s]
                key_stab = keys[pygame.K_r]
                key_vanish = keys[pygame.K_f]
        elif not wasd:
            if self.knock_down:
                key_shoot = None
                key_left = None
                key_right = None
                key_up = None
                key_down = None
                key_stab = None
                key_vanish = keys[pygame.K_b]
            elif not self.knock_down:
                key_shoot = keys[pygame.K_SPACE]
                key_left = keys[pygame.K_LEFT]
                key_right = keys[pygame.K_RIGHT]
                key_up = keys[pygame.K_UP]
                key_down = keys[pygame.K_DOWN]
                key_stab = keys[pygame.K_n]
                key_vanish = keys[pygame.K_b]

        if self.bullet_delay == 0:
            if key_shoot:
                if self.bullet_count > 0:
                    self.shoot_status = True
                    if self.left:
                        shooting_direction = -2
                        self.shooting_direction = shooting_direction
                    else:
                        shooting_direction = 2
                        self.shooting_direction = shooting_direction
                    self.death_direction = shooting_direction
                    self.bullets.append(
                        projectile.projectile(round(self.x + self.width / 2), round(self.y + self.height / 2),
                                              shooting_direction))
                    self.bullet_count -= 1
                    if self.character == 1:
                        for x in range(10):
                            if x == self.bullet_count:
                                self.bullet_bar_x += 20
                    self.bullet_bar_w = self.bullet_count * 20
                    AAfilledRoundedRect.AAfilledRoundedRect(win, (self.bullet_bar_x, self.bullet_bar_y,
                                                                  self.bullet_bar_w, self.bullet_bar_h), (31, 117, 254),
                                                            1)
                    shoot_sound.play()
                else:
                    self.shoot_status = False
            else:
                self.shoot_status = False

        if key_left and self.x > self.vol and not key_stab:
            self.x -= self.vol
            self.left = True
            self.right = False
            self.walking = True
        elif key_right and self.x < self.screen_x - self.vol - self.width and not key_stab:
            self.x += self.vol
            self.left = False
            self.right = True
            self.walking = True
        else:
            self.walking = False
            self.walk_count = 0

        if key_vanish and self.teleport_remain > 0:
            if self.left:
                if self.x != 0:
                    self.teleport = True
                    # self.knock_down_left = False
                    # self.knock_down_right = False
                else:
                    self.teleport = False
            if self.right:
                if self.x != 1280 - 128:
                    self.teleport = True
                    # self.knock_down_left = False
                    # self.knock_down_right = False
                else:
                    self.teleport = False
        else:
            self.teleport = False
            self.teleport_count = 0

        if key_down:
            if self.jump:
                self.walking = False
                self.going_down = True
                self.vanish = True
            self.y = self.default_y
            self.jump = False
            self.jump_count = 13

        if not key_down:
            self.going_down = False
            self.vanish = False
            if not self.jump:
                if key_up:
                    self.jump = True
                    self.walk_count = 0
            else:
                if key_up:
                    self.first_press_jump = False
                if self.jump_count >= -13:
                    n = 1
                    if self.jump_count < 0:
                        n = -1
                    self.y -= self.jump_count ** 2 / 2 * n
                    self.jump_count -= 1
                else:
                    self.jump = False
                    self.jump_count = 13
        if key_stab:
            self.walking = False
            self.stabbing = True
        else:
            self.stabbing = False

    def attack(self, enemy, window):
        if self.stabbing:
            if self.character == 1:
                if self.left:
                    if self.stab_count >= 0:
                        window.blit(punch_left[round(self.stab_count)], (int(self.x), int(self.y)))
                        self.stab_count += 0.2
                        if self.x - 10 > self.vol:
                            if round(self.stab_count) == 1 or round(self.stab_count) == 4:
                                self.x -= 10
                        elif self.x - 3 > self.vol:
                            self.x -= 3
                    if self.stab_count >= 6:
                        self.stab_count = 0
                elif self.right:
                    if self.stab_count >= 0:
                        window.blit(punch_right[round(self.stab_count)], (int(self.x), int(self.y)))
                        self.stab_count += 0.2
                        if self.x + 10 < self.screen_x - self.vol - self.width:
                            if round(self.stab_count) == 1 or round(self.stab_count) == 4:
                                self.x += 10
                        elif self.x + 3 < self.screen_x - self.vol - self.width:
                            self.x += 3
                    if self.stab_count >= 6:
                        self.stab_count = 0
                    # pygame.draw.rect(window, (0, 255, 0), self.hit_box, 1)
                self.hit_box = (self.x, self.y, 80, 64)

            elif self.character == 2:
                if self.left:
                    if self.stab_count >= 0:
                        window.blit(c2_punch_left[round(self.stab_count)], (int(self.x), int(self.y)))
                        self.stab_count += 0.2
                        if self.x - 10 > self.vol:
                            if round(self.stab_count) == 1 or round(self.stab_count) == 4:
                                self.x -= 10
                        elif self.x - 3 > self.vol:
                            self.x -= 3
                    if self.stab_count >= 6:
                        self.stab_count = 0
                elif self.right:
                    if self.stab_count >= 0:
                        window.blit(c2_punch_right[round(self.stab_count)], (int(self.x), int(self.y)))
                        self.stab_count += 0.2
                        if self.x + 10 < self.screen_x - self.vol - self.width:
                            if round(self.stab_count) == 1 or round(self.stab_count) == 4:
                                self.x += 10
                        elif self.x + 3 < self.screen_x - self.vol - self.width:
                            self.x += 3
                    if self.stab_count >= 6:
                        self.stab_count = 0
                    # pygame.draw.rect(window, (0, 255, 0), self.hit_box, 1)
                self.hit_box = (self.x, self.y, 80, 64)

            if enemy.hit_box[1] > self.hit_box[1] and enemy.hit_box[1] < self.hit_box[1] + self.hit_box[3]:
                if enemy.hit_box[0] > self.hit_box[0] and enemy.hit_box[0] < self.hit_box[0] + self.hit_box[2]:
                    if enemy.temp1[2] > 0:
                        if enemy.temp1[2] - 1 > 0:
                            enemy.temp1[2] = enemy.temp1[2] - 1
                        else:
                            enemy.temp1[2] = 0
                        enemy.health_bar_location = tuple(enemy.temp1)
                        AAfilledRoundedRect.AAfilledRoundedRect(window, self.health_bar_location, (255, 0, 0), 1)
                        #pygame.draw.rect(window, (255, 0, 0), self.health_bar_location)
                        # self.health -= 15
                        self.die = False
                        enemy.knock_down = True
                        if self.left:
                            enemy.knock_down_direction = -2
                        elif self.right:
                            enemy.knock_down_direction = 2

                    else:
                        self.die = True

    def is_dead(self):
        return self.die
