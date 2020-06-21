import pygame

blue_bullet = pygame.image.load('blue_bullet.png')  # Importing blue bullet png
red_bullet = pygame.image.load('red_bullet.png')  # Importing red bullet png

class projectile():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.vol = 14 * direction
        self.bullet_radius = 5

    def shoot_bullet(self, win, color):
        if color == 'red':
            win.blit(red_bullet, (self.x, self.y))
        elif color == 'blue':
            win.blit(blue_bullet, (self.x, self.y))