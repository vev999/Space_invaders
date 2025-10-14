import random
import pygame
from settings import (HEIGHT, WIDTH, START_BRIGHT_MAX, STAR_BRIGHT_MIN, STAR_SPEED_MAX, STAR_SPEED_MIN,STAR_BLINK_CHANCE, STARS_COUNT, STAR_SIZE, SIZE_CHANCE, MAX_SIZE, MIN_SIZE)

def rand_brightness():
    return random.randint(STAR_BRIGHT_MIN, START_BRIGHT_MAX)

class Starfield:
    def __init__(self, count = STARS_COUNT):
        self.stars = []
        self.spawn(count)
    
    def spawn(self, count):
        for i in range(count):
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            speed = random.randint(STAR_SPEED_MIN, STAR_SPEED_MAX)
            bright = random.randint(STAR_BRIGHT_MIN, START_BRIGHT_MAX)
            size = random.randint(MIN_SIZE, MAX_SIZE)
            self.stars.append([x,y,speed,bright,size])
    
    def update_stars(self, dt: float):
        for i in self.stars:
            i[1] += i[2] * dt

            if i[1] > HEIGHT:
                i[1] = -1

            if random.random() < STAR_BLINK_CHANCE:
                delta = random.randint(-15,15)
                i[3] = max(STAR_BRIGHT_MIN, min(STAR_SPEED_MAX, i[3] + delta))

            if random.random() < SIZE_CHANCE:
                delta2 = random.randint(-1,1)
                i[4] = max(MIN_SIZE, min(MAX_SIZE, i[4] + delta2))
            
            

    def draw(self, screen: pygame.Surface):
        for x,y, _,bright, size in self.stars:
            color =(bright,bright,bright)
            screen.fill(color, rect=pygame.Rect(x,y,size,size))
                        