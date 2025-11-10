import pygame
from settings import COVER_SIZE, COVER_COLOR

TILE_SIZE = 8


class Cover:
    def __init__(self, pos: tuple[int, int]):
        w, h = COVER_SIZE
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.midbottom = pos
        self.dead = False
        self.tiles = self._build_tiles()

    def _build_tiles(self) -> list[pygame.Rect]:
        tiles = []
        for y in range(self.rect.top, self.rect.bottom, TILE_SIZE):
            for x in range(self.rect.left, self.rect.right, TILE_SIZE):
                tiles.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
        return tiles

    def take_hit(self, projectile_rect: pygame.Rect) -> bool:
        hit = False
        for tile in self.tiles[:]:
            if tile.colliderect(projectile_rect):
                self.tiles.remove(tile)
                hit = True
        if hit and not self.tiles:
            self.dead = True
        return hit

    def draw(self, screen: pygame.Surface):
        for tile in self.tiles:
            screen.fill(COVER_COLOR, tile)
