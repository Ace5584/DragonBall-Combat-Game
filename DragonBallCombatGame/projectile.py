import pygame

blue_bullet = pygame.image.load('projectile/blue_bullet.png')  # Importing blue bullet png
red_bullet = pygame.image.load('projectile/red_bullet.png')  # Importing red bullet png
power_ball = pygame.image.load('projectile/ball_30x30.png')
power_ball_left = pygame.image.load('projectile/left_ball_30x30.png')

class projectile():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.vol = 14 * direction
        self.bullet_radius = 40

    def shoot_bullet(self, win, color, left):
        if color == 'red':
            if self.direction < 0:
                win.blit(power_ball_left, (self.x - 10, self.y - 40))
            else:
                win.blit(power_ball, (self.x + 10, self.y - 40))
        elif color == 'blue':
            if self.direction < 0:
                win.blit(power_ball_left, (self.x - 10, self.y - 40))
            else:
                win.blit(power_ball, (self.x + 10, self.y - 40))