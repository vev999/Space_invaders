import pygame
from settings import ENEMY_BULLET_SIZE, ENEMY_BULLET_COLOR, HEIGHT,ENEMY_BULLET_SPEED

class EnemyBullet:
    def __init__(self, start_y: tuple[int,int]):
        w,h = ENEMY_BULLET_SIZE
        self.image = pygame.Surface((w,h), pygame.SRCALPHA)
        self.image.fill(ENEMY_BULLET_COLOR)
        self.rect = self.image.get_rect(center=start_y)
        self.dead = False
    def update(self, dt: float):
        self.rect.y += ENEMY_BULLET_SPEED * dt
        if self.rect.y > HEIGHT:
            self.dead = True
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)