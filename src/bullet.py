import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/bullet.png")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        self.y -= 10
        self.rect.centery = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
