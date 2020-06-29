import pygame



pygame.init()


class sword:
    def __init__(self, x, y, character):
        self.x = x
        self.y = y
        self.character = character
        if self.character == 1:
            #self.x = self.x - 36
            self.hit_box = (self.x, self.y, 100, 64)
        elif self.character == 2:
            #self.x = self.x - 16
            self.hit_box = (self.x, self.y, 80, 64)
        self.stab_count = 0
        self.sword_timer_sec = 2
        self.sword_timer = pygame.USEREVENT + 3
        pygame.time.set_timer(self.sword_timer, 1000)



