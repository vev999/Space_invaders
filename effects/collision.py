import pygame
from entities.bullet_manager import BulletManager, EnemyBulletManager
from entities.bullets import Bullet
from entities.player import Player

def handle_collisions(player, enemies, BulletManager, EnemyBulletManager):
    ##KOLIZJE POCISKÓW GRACZA <> WRÓG
    score = 0 
    for e in enemies:
        if e.dead:
            continue
        for b in BulletManager.bullets:
            if not b.dead and b.rect.colliderect(e.rect):
                b.dead = True
                e.dead = True
                score += getattr(e, "points")
    enemies[:] = [e for e in enemies if not e.dead]

    ##KOLIZJE POCISKÓW WROGA <> GRACZ
    for eb in EnemyBulletManager.enemybullets:
        if not eb.dead and eb.rect.colliderect(player.rect):
            eb.dead = True
            player.got_hit()

    ##KOLIZJE GRACZ <> WRÓG
    for e in enemies:
        if player.rect.colliderect(e.rect):
            player.got_hit()
            e.dead = True
    enemies[:] = [e for e in enemies if not e.dead]

    return score
    

    

