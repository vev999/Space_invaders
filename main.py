import sys
import pygame
from settings import (
    FPS,
    HEIGHT,
    WIDTH,
    BG_COLOR,
    ENEMY_START_Y,
    LEVELUPDATE,
    HUD_BG_COLOR,
    HUD_TEXT_COLOR,
    HUD_HEIGHT,
    HUD_FONT_SIZE,
    HUD_PADDING,
)
from entities.player import Player
from effects.background import Starfield
from entities.bullet_manager import BulletManager, EnemyBulletManager
from entities.enemy import Enemy
from effects.collision import handle_collisions
from effects.game_over import print_game_over
from effects.hud import hud
from entities.cover import Cover

def main():
    pygame.init()
    pygame.display.set_caption("SPACE INVADERS")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    hud_font = pygame.font.Font(None, HUD_FONT_SIZE)
    player = Player(WIDTH // 2, (64,64))
    background = Starfield()
    lvl = LEVELUPDATE()
    bullet_manager = BulletManager()
    covers = [
        Cover((150, HEIGHT - 200)),
        Cover((WIDTH - 150, HEIGHT - 200)),
        Cover((WIDTH // 2, HEIGHT - 200)),
    ]
    enemies = []
    score = 0
    wave = 1
    for x in range(80, WIDTH, 80):
        enemies.append(Enemy(x, points=100, scale=(32,28), level=lvl))
        
    enemy_manger = EnemyBulletManager()


    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BG_COLOR)
        keys = pygame.key.get_pressed()
        score += handle_collisions(player, enemies, bullet_manager, enemy_manger, covers)
        
        ##UPDATES##
        
        player.update_XY(dt, keys)

        bullet_manager.fire((player.rect.centerx, player.rect.top - 4), dt, keys)
        bullet_manager.update(dt)
        for e in enemies:
            e.update(dt)
            e.try_fire(enemy_manger, dt)
        enemy_manger.update(dt)
        enemies = [e for e in enemies if not e.dead]
        if not enemies:  
            lvl.level_up()
            wave += 1
            enemies = [Enemy(x, points=100, scale=(30,28),level=lvl) for x in range(80, WIDTH, 80)]


        
        background.update_stars(dt)
        
        ##DRAW##
        
        background.draw(screen)

        bullet_manager.draw(screen)

        for cover in covers:
            cover.draw(screen)

        for e in enemies:
            e.draw(screen)
        
        enemy_manger.draw(screen)

        player.draw(screen)
        
        hud(screen, hud_font, score, player, wave)
       
        pygame.display.flip()

        if player.lives <= 0.0:
            running = False
        
        
        

    pygame.quit()
    print_game_over()
    print (f"YOUR SCORE IS {score}")
    sys.exit()
    
    
    
if __name__=='__main__':
    main()
    
