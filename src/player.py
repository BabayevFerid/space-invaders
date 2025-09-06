import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/player.png")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, dx):
        self.x += dx
        if self.x < 40: self.x = 40
        if self.x > 760: self.x = 760
        self.rect.centerx = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)
