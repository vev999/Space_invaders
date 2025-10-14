import pygame
from settings import ENEMY_IMG, ENEMY_START_Y, ENEMY_STEP_DOWN, WIDTH, HEIGHT
import random
from entities.bullet_manager import EnemyBulletManager

class Enemy:
    def __init__(self, x, points, scale: tuple[int, int] | None = None, level=None):
        image = pygame.image.load(ENEMY_IMG)
        if scale:
            image = pygame.transform.scale(image, scale)
        self.image = image
        self.rect = self.image.get_rect(midbottom=(x, ENEMY_START_Y))
        self.points = points
        self.direction = 1
        self.level = level
        self.speed_x = self.level.enemy_speed()
        self.dead = False
        self.timmer = 0.0
        
    
    def update(self, dt: float):
        self.rect.x += self.direction * self.level.enemy_speed() * dt

        if self.rect.right >= WIDTH:
            self.direction = -1
            self.rect.y += ENEMY_STEP_DOWN
        if self.rect.left <= 0:
            self.direction = 1
            self.rect.y += ENEMY_STEP_DOWN
        if self.rect.bottom >= HEIGHT:
            self.dead = True
    
    def try_fire(self,EnemyBulletManager, dt: float):
        if self.timmer > 0.0:
            self.timmer -= dt
            return
        if random.random() < self.level.enemy_fire_chance():
            origin = (self.rect.centerx, self.rect.bottom + 4)
            EnemyBulletManager.fire(origin)
            self.timmer = self.level.enemy_fire_cooldown()
            
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)

