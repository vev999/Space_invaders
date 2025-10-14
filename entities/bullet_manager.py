import pygame
from entities.bullets import Bullet
from entities.enemy_bullet import EnemyBullet
from settings import FIRE_COOLDOWN
import random


class BulletManager:
    def __init__(self):
        self.bullets: list[Bullet] = []
        self.timer = 0.0
    
    def fire(self, origin: tuple[int,int], dt: float, keys):
        if self.timer > 0.0:
            self.timer -= dt
            return
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(origin))
            self.timer = FIRE_COOLDOWN
    
    def update(self, dt:float):
        for b in self.bullets:
            b.update(dt)
        self.bullets = [b for b in self.bullets if not b.dead]
    
    def draw(self, screen: pygame.Surface):
        for b in self.bullets:
            b.draw(screen)

class EnemyBulletManager:
    def __init__(self):
        self.enemybullets: list[EnemyBullet] = []
        
    
    def fire(self, origin: tuple[int, int]):
        self.enemybullets.append(EnemyBullet(origin))
    
    def update(self, dt:float):
        for b in self.enemybullets:
            b.update(dt)
        self.enemybullets=[b for b in self.enemybullets if not b.dead]  
    
    def draw(self,screen: pygame.Surface):
        for b in self.enemybullets:
            b.draw(screen)    
