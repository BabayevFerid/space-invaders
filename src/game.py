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
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Invaders 🚀")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False

        # Assets
        self.background = pygame.image.load("assets/background.png")

        # Səs faylları
        self.laser_sound = pygame.mixer.Sound("assets/laser.wav")
        self.explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
        self.gameover_sound = pygame.mixer.Sound("assets/gameover.wav")

        # Font
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)

        self.reset_game()

    def reset_game(self):
        """Oyunu sıfırlamaq üçün"""
        self.player = Player(WIDTH // 2, HEIGHT - 100)
        self.enemies = [Enemy(random.randint(50, WIDTH-50), random.randint(50, 150)) for _ in range(6)]
        self.bullets = []
        self.score = 0
        self.game_over = False

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            if not self.game_over:
                self.update()
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if not self.game_over and event.key == pygame.K_SPACE:
                    bullet = Bullet(self.player.x, self.player.y)
                    self.bullets.append(bullet)
                    self.laser_sound.play()  # 🔊 Atəş səsi

                if self.game_over and event.key == pygame.K_r:
                    self.reset_game()

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
                if not self.game_over:
                    self.gameover_sound.play()  # 🔊 Game Over səsi
                self.game_over = True

        # Toqquşma yoxlama
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    try:
                        self.bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        self.explosion_sound.play()  # 🔊 Partlayış səsi
                        self.score += 10
                    except ValueError:
                        pass
                    break

        # Əgər düşmənlər bitdisə → yeni dalğa
        if not self.enemies:
            self.enemies = [Enemy(random.randint(50, WIDTH-50), random.randint(50, 150)) for _ in range(6)]

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        for bullet in self.bullets:
            bullet.draw(self.screen)

        # Score yazısı
        score_text = self.font.render(f"Score: {self.score}", True, (255,255,255))
        self.screen.blit(score_text, (10, 10))

        # Əgər oyun bitibsə → Game Over ekranı
        if self.game_over:
            over_text = self.big_font.render("GAME OVER", True, (255, 50, 50))
            restart_text = self.font.render("Press R to Restart", True, (200, 200, 200))

            self.screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 50))
            self.screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 30))

        pygame.display.flip()
