import pygame
from settings import HUD_BG_COLOR, HUD_HEIGHT, HUD_PADDING, HUD_TEXT_COLOR, WIDTH


def hud(screen, hud_font, score, player, wave):
    pygame.draw.rect(screen, HUD_BG_COLOR, pygame.Rect(0, 0, WIDTH, HUD_HEIGHT))
    hud_y = HUD_HEIGHT // 2
    score_text = hud_font.render(f"Score: {score}", True, HUD_TEXT_COLOR)
    lives_val = max(int(player.lives), 0)
    lives_text = hud_font.render(f"Lives: {lives_val}", True, HUD_TEXT_COLOR)
    wave_text = hud_font.render(f"Wave: {wave}", True, HUD_TEXT_COLOR)
    score_pos = (HUD_PADDING, hud_y - score_text.get_height() // 2)
    lives_pos = ((WIDTH - lives_text.get_width()) // 2, hud_y - lives_text.get_height() // 2)
    wave_pos = (WIDTH - wave_text.get_width() - HUD_PADDING, hud_y - wave_text.get_height() // 2)
    screen.blit(score_text, score_pos)
    screen.blit(lives_text, lives_pos)
    screen.blit(wave_text, wave_pos)