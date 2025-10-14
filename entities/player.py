import pygame
from settings import WIDTH, HEIGHT, PLAYER_IMG, PlAYER_SPEED, PLAYER_START_Y, PLAYER_IMMO_COOLDOWN, PLAYER_LIVES, PLAYER_HIT_IMG

class Player:
    
    def __init__(self, start_x: int = WIDTH // 2, scale: tuple[int, int] | None = None):
        img_normal = pygame.image.load(PLAYER_IMG)
        img_hit    = pygame.image.load(PLAYER_HIT_IMG)
        
        if scale:
            img_normal = pygame.transform.scale(img_normal, scale)
            img_hit = pygame.transform.scale(img_hit, scale)
        self.image_normal = img_normal
        self.image_hit = img_hit
        self.image = self.image_normal
        self.rect = self.image.get_rect(midbottom=(start_x, PLAYER_START_Y))
        self.speed = PlAYER_SPEED
        self.lives = PLAYER_LIVES
        self.immortal  = 0.0
        self.flash = 0.0
        self.visible = True

    def update_XY (self, dt: float, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.rect.x += self.speed * dt
        if keys[pygame.K_w]:
            self.rect.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.rect.y += self.speed * dt 
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        
        if self.immortal > 0.0:
            self.immortal -= dt
            self.flash += dt
            if self.flash >= PLAYER_IMMO_COOLDOWN:
                self.visible = False
                self.flash = 0.0
                
        else:
            self.visible = True
            self.image = self.image_normal
        
    def got_hit(self):
        if self.immortal > 0.0:
            return
        self.lives -= 1
        self.image = self.image_hit 
        self.immortal = PLAYER_IMMO_COOLDOWN
        
    
    def draw(self, screen: pygame.Surface):
        if not self.visible:
            return
        screen.blit(self.image, self.rect)