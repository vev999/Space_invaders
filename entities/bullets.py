import pygame
from settings import HEIGHT, BULLET_SPEED, BULLET_COLOR, BULLET_SIZE

class Bullet:
    def __init__(self, start_y: tuple[int,int]):
        w,h = BULLET_SIZE
        self.image = pygame.Surface((w,h), pygame.SRCALPHA)
        self.image.fill(BULLET_COLOR)
        self.rect = self.image.get_rect(center=start_y)
        self.dead = False
    def update(self, dt: float):
        self.rect.y -= BULLET_SPEED * dt
        if self.rect.y < 0:
            self.dead = True
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)