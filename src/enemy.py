import pygame
import random

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/enemy.png")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = random.choice([-2, 2])

    def move(self):
        self.x += self.dx
        if self.x <= 40 or self.x >= 760:
            self.dx *= -1
            self.y += 40
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
