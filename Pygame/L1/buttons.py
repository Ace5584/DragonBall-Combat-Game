import pygame


class button():
    def __init__(self, x, y, width, height, color, text='', text_size=25):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont('comicsans', text_size, True)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if self.text != '':
            text = self.font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + self.width/2 - text.get_width()/2, self.y + self.height/2 - text.get_height()/2))

    def is_over(self, pos):
        if self.x < pos[0] < (self.width + self.x):
            if self.y < pos[1] < (self.height + self.y):
                return True
        else:
            return False
