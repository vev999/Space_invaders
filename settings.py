##GAME
WIDTH, HEIGHT = 1100, 700
FPS = 60

##PLAYER
PLAYER_IMG = "assets/player.png"
PLAYER_HIT_IMG = "assets/player2.png"
PlAYER_SPEED = 420 #px/s
PLAYER_START_Y = HEIGHT - 20
PLAYER_LIVES = 3
PLAYER_IMMO_COOLDOWN = 0.2
HIT_FREQ = 10

#ENEMY
ENEMY_IMG ="assets/enemy.png"
ENEMY_START_Y = 0 + 100
ENEMY_STEP_DOWN = 80 

#HUD
HUD_HEIGHT = 56
HUD_BG_COLOR = (230, 70, 40)
HUD_TEXT_COLOR = (235, 235, 245)
HUD_FONT_SIZE = 32
HUD_PADDING = 16
PLAYFIELD_TOP_MARGIN = HUD_HEIGHT + 12

class LEVELUPDATE():
    def __init__(self):
        
        self.POWER_UP1 = 0
        self.POWER_UP2 = 0
        self.POWER_UP3 = 0
    
    def level_up(self):
        self.POWER_UP1 += 0.05
        self.POWER_UP2 += 0.005
        self.POWER_UP3 += 50
        
    def enemy_fire_cooldown(self):
        return max(0.25 - self.POWER_UP1, 0.10)

    def enemy_fire_chance(self):
        return 0.005 + self.POWER_UP2

    def enemy_speed(self):
        return 120 + self.POWER_UP3


##BACKGROUND
STARS_COUNT = 300
STAR_SPEED_MIN = 80
STAR_SPEED_MAX = 100
STAR_BRIGHT_MIN = 170
START_BRIGHT_MAX = 255
STAR_BLINK_CHANCE = 0.15
BG_COLOR = (10, 10, 20)
STAR_SIZE = (2,2)
SIZE_CHANCE = 0.2
MAX_SIZE = 3
MIN_SIZE = 1

##SHOTTING
BULLET_SPEED = 1200
FIRE_COOLDOWN = 0.125
BULLET_SIZE = (6,14)
BULLET_COLOR = (255,0,0)
ENEMY_BULLET_SPEED = 320
ENEMY_BULLET_SIZE = (4,14)      
ENEMY_BULLET_COLOR = (0,255,0)
