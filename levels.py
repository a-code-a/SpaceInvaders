import pygame
import random

# Level class
class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.enemies = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.create_level()

    def create_level(self):
        # Create enemies with increasing difficulty
        for i in range(8 + self.level_number):
            for j in range(3 + self.level_number // 2):
                enemy = Enemy(i * 80 + 50, j * 60 + 50)
                self.enemies.add(enemy)

        # Add power-ups
        if self.level_number % 3 == 0:
            power_up = PowerUp(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT // 2))
            self.power_ups.add(power_up)

    def update(self):
        self.enemies.update()
        self.power_ups.update()

    def draw(self, screen):
        self.enemies.draw(screen)
        self.power_ups.draw(screen)

# PowerUp class
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 2

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed_x *= -1
            self.rect.y += 40

    def shoot(self):
        if random.random() < 0.01:
            projectile = EnemyProjectile(self.rect.centerx, self.rect.bottom)
            all_sprites.add(projectile)
            enemy_projectiles.add(projectile)

# EnemyProjectile class
class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed_y = 5

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
