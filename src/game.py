import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet
import random

# Ekran ölçüləri
WIDTH, HEIGHT = 800, 600

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Invaders 🚀")
        self.clock = pygame.time.Clock()
        self.running = True

        # Assets
        self.background = pygame.image.load("assets/background.png")

        # Oyuncu
        self.player = Player(WIDTH // 2, HEIGHT - 100)

        # Düşmənlər
        self.enemies = [Enemy(random.randint(50, WIDTH-50), random.randint(50, 150)) for _ in range(6)]

        # Güllələr
        self.bullets = []

        # Font
        self.font = pygame.font.Font(None, 36)
        self.score = 0

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(self.player.x, self.player.y)
                    self.bullets.append(bullet)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-5)
        if keys[pygame.K_RIGHT]:
            self.player.move(5)

        # Güllələrin hərəkəti
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                self.bullets.remove(bullet)

        # Düşmənlərin hərəkəti
        for enemy in self.enemies:
            enemy.move()
            if enemy.y > HEIGHT - 100:
                self.running = False  # Game over

        # Toqquşma yoxlama
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 10
                    break

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        for bullet in self.bullets:
            bullet.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (255,255,255))
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()
