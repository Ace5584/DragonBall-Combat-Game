import pygame

sword_StabLeft = [pygame.image.load('sword/SL1.png'), pygame.image.load('sword/SL2.png'),
                  pygame.image.load('sword/SL3.png'), pygame.image.load('sword/SL4.png')]
sword_StabRight = [pygame.image.load('sword/SR1.png'), pygame.image.load('sword/SR2.png'),
                   pygame.image.load('sword/SR3.png'), pygame.image.load('sword/SR4.png')]
c2_sword_StabLeft = [pygame.image.load('sword/SL1E.png'), pygame.image.load('sword/SL2E.png'),
                     pygame.image.load('sword/SL3E.png'), pygame.image.load('sword/SL4E.png')]
c2_sword_StabRight = [pygame.image.load('sword/SR1E.png'), pygame.image.load('sword/SR2E.png'),
                      pygame.image.load('sword/SR3E.png'), pygame.image.load('sword/SR4E.png')]

class sword:
    def __init__(self, x, y, character, win):
        self.x = x
        self.y = y
        self.hit_box = (self.x, self.y, 99, 60)
        self.character = character
        self.win = win


    def attack(self, player, enemy):
        if self.character == 1:
            if enemy.hit_box[1] > self.hit_box[1]:
                #if enemy.hit_box[0]
                None