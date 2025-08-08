import pygame
from settings import WIDTH, HEIGHT, ENEMY_RADIUS

outter_walls = [
    pygame.Rect(0, 0, WIDTH, 10),
    pygame.Rect(0, HEIGHT - 10, WIDTH, 10),
    pygame.Rect(0, 0, 10, HEIGHT),
    pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)
]

def level_1():
    return {
        "walls": outter_walls + [
            pygame.Rect(300, 200, 200, 20),
        ],
        "num_enemies": 3,
        "powerups": 3,
        "goal": "kill_all"
    }

def level_2():
    return {
        "walls": outter_walls + [
            pygame.Rect(150, 150, 500, 20),
            pygame.Rect(400, 350, 20, 200),
        ],
        "num_enemies": 5,
        "powerups": 5,
        "goal": "kill_all"
    }

LEVELS = [level_1, level_2]
