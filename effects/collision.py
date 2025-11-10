import pygame
from entities.bullet_manager import BulletManager, EnemyBulletManager
from entities.bullets import Bullet
from entities.player import Player
from entities.cover import Cover

def handle_collisions(player, enemies, bullet_manager, enemy_bullet_manager, covers):
    ##KOLIZJE POCISKÓW GRACZA <> WRÓG
    score = 0 
    for e in enemies:
        if e.dead:
            continue
        for b in bullet_manager.bullets:
            if not b.dead and b.rect.colliderect(e.rect):
                b.dead = True
                e.dead = True
                score += getattr(e, "points")
    enemies[:] = [e for e in enemies if not e.dead]

    ##KOLIZJE POCISKÓW WROGA <> GRACZ
    for eb in enemy_bullet_manager.enemybullets:
        if not eb.dead and eb.rect.colliderect(player.rect):
            eb.dead = True
            player.got_hit()

    ##KOLIZJE GRACZ <> WRÓG
    for e in enemies:
        if player.rect.colliderect(e.rect):
            player.got_hit()
            e.dead = True
    enemies[:] = [e for e in enemies if not e.dead]

    ##KOLIZJE POCISKÓW <> OSŁONY
    for b in bullet_manager.bullets:
        if b.dead:
            continue
        for cover in covers:
            if cover.dead:
                continue
            if not cover.rect.colliderect(b.rect):
                continue
            if cover.take_hit(b.rect):
                b.dead = True
                break

    for ec in enemy_bullet_manager.enemybullets:
        if ec.dead:
            continue
        for cover in covers:
            if cover.dead:
                continue
            if not cover.rect.colliderect(ec.rect):
                continue
            if cover.take_hit(ec.rect):
                ec.dead = True
                break

    covers[:] = [cover for cover in covers if not cover.dead]

    return score
    

    
