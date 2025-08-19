import pygame
from settings import WIDTH, HEIGHT, ENEMY_RADIUS

outter_walls = [
    pygame.Rect(0, 0, WIDTH, 10),
    pygame.Rect(0, HEIGHT - 10, WIDTH, 10),
    pygame.Rect(0, 0, 10, HEIGHT),
    pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)
]

outer_left_wall = [pygame.Rect(90, 190, 20, 420)]
outer_right_wall = [pygame.Rect(690, 190, 20, 420)]
outer_top_wall = [pygame.Rect(190, 90, 420, 20)]
outer_bottom_wall = [pygame.Rect(190, 690, 420, 20)]

top_left_corner = [
    pygame.Rect(190, 190, 20, 170),
    pygame.Rect(190, 190, 170, 20)
]
top_right_corner = [
    pygame.Rect(440, 190, 170, 20),
    pygame.Rect(590, 190, 20, 170)
]
bottom_left_corner = [
    pygame.Rect(190, 440, 20, 170),
    pygame.Rect(190, 590, 170, 20)
]
bottom_right_corner = [
    pygame.Rect(440, 590, 170, 20),
    pygame.Rect(590, 440, 20, 170)
]

inner_left_wall = [pygame.Rect(290, 290, 20, 220)]
inner_right_wall = [pygame.Rect(490, 290, 20, 220)]
inner_top_wall = [pygame.Rect(290, 290, 220, 20)]
inner_bottom_wall = [pygame.Rect(290, 490, 220, 20)]

def test_level():
    return {
        "walls": outter_walls + outer_left_wall + outer_right_wall + outer_top_wall + outer_bottom_wall + top_left_corner + top_right_corner + bottom_left_corner + bottom_right_corner + inner_left_wall + inner_right_wall + inner_top_wall + inner_bottom_wall,
        "enemy_types": [0],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_1():
    return {
        "walls": outter_walls + inner_right_wall + inner_bottom_wall + top_left_corner + inner_left_wall + outer_bottom_wall + outer_right_wall + bottom_left_corner + bottom_right_corner + outer_top_wall, 
        "enemy_types": [0],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_2():
    return {
        "walls": outter_walls + outer_top_wall + outer_left_wall + top_right_corner + bottom_right_corner + outer_right_wall + top_left_corner + inner_bottom_wall + inner_left_wall + bottom_left_corner + inner_right_wall + outer_bottom_wall, 
        "enemy_types": [1],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_3():
    return {
        "walls": outter_walls + outer_right_wall + outer_bottom_wall + inner_left_wall + top_right_corner + top_left_corner + inner_right_wall + outer_left_wall, 
        "enemy_types": [0, 0],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_4():
    return {
        "walls": outter_walls + outer_right_wall, 
        "enemy_types": [0, 1],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_5():
    return {
        "walls": outter_walls + inner_top_wall + top_left_corner + inner_bottom_wall + outer_top_wall + outer_bottom_wall + inner_right_wall, 
        "enemy_types": [1, 1, 0],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_6():
    return {
        "walls": outter_walls + outer_bottom_wall + bottom_right_corner + top_left_corner + top_right_corner + inner_left_wall + bottom_left_corner + inner_top_wall + inner_right_wall, 
        "enemy_types": [0, 1, 2],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_7():
    return {
        "walls": outter_walls + inner_bottom_wall + bottom_left_corner + top_left_corner, 
        "enemy_types": [1, 1, 2],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_8():
    return {
        "walls": outter_walls + outer_right_wall + inner_right_wall + outer_top_wall + top_right_corner + top_left_corner + bottom_left_corner + inner_bottom_wall + outer_bottom_wall, 
        "enemy_types": [0, 1, 2, 2],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_9():
    return {
        "walls": outter_walls + inner_right_wall + top_right_corner + bottom_left_corner + outer_bottom_wall, 
        "enemy_types": [1, 1, 2, 2],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_10():
    return {
        "walls": outter_walls + bottom_left_corner + top_left_corner + inner_left_wall + outer_top_wall, 
        "enemy_types": [1, 2, 2, 2],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_11():
    return {
        "walls": outter_walls + outer_bottom_wall + bottom_right_corner + inner_left_wall + top_right_corner, 
        "enemy_types": [1, 2, 3],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_12():
    return {
        "walls": outter_walls + inner_bottom_wall, 
        "enemy_types": [1, 2, 2, 3],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_13():
    return {
        "walls": outter_walls + top_right_corner + bottom_right_corner + inner_right_wall + outer_top_wall + bottom_left_corner + outer_bottom_wall + inner_top_wall + inner_bottom_wall + outer_left_wall, 
        "enemy_types": [2, 2, 2, 2],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_14():
    return {
        "walls": outter_walls + inner_right_wall + inner_bottom_wall + bottom_right_corner + outer_top_wall + outer_bottom_wall + top_left_corner + inner_top_wall + inner_left_wall, 
        "enemy_types": [1, 2, 3, 3],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_15():
    return {
        "walls": outter_walls + outer_right_wall, 
        "enemy_types": [1, 2, 2, 3, 3],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_16():
    return {
        "walls": outter_walls + top_right_corner + outer_left_wall + inner_left_wall + inner_bottom_wall + outer_right_wall + bottom_right_corner, 
        "enemy_types": [4, 4],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_17():
    return {
        "walls": outter_walls + outer_top_wall + top_left_corner + inner_top_wall + outer_left_wall + bottom_right_corner + top_right_corner + bottom_left_corner + inner_right_wall, 
        "enemy_types": [2, 3, 4],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_18():
    return {
        "walls": outter_walls + inner_right_wall + bottom_left_corner + outer_top_wall + outer_bottom_wall + inner_top_wall, 
        "enemy_types": [2, 3, 3, 4],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_19():
    return {
        "walls": outter_walls + inner_bottom_wall, 
        "enemy_types": [2, 3, 4, 4],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_20():
    return {
        "walls": outter_walls + outer_top_wall + top_right_corner + inner_top_wall + bottom_right_corner + inner_bottom_wall + inner_right_wall, 
        "enemy_types": [2, 3, 3, 4, 4],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_21():
    return {
        "walls": outter_walls + top_left_corner, 
        "enemy_types": [3, 4, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_22():
    return {
        "walls": outter_walls + outer_top_wall + inner_right_wall + inner_top_wall, 
        "enemy_types": [3, 4, 4, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_23():
    return {
        "walls": outter_walls + bottom_right_corner + inner_left_wall + outer_top_wall + top_right_corner + inner_bottom_wall + outer_bottom_wall + inner_top_wall + top_left_corner + bottom_left_corner + inner_right_wall + outer_left_wall, 
        "enemy_types": [2, 4, 5, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_24():
    return {
        "walls": outter_walls + bottom_right_corner + inner_top_wall + inner_bottom_wall + outer_right_wall, 
        "enemy_types": [3, 3, 4, 5, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_25():
    return {
        "walls": outter_walls + top_right_corner + bottom_left_corner + outer_bottom_wall + outer_left_wall, 
        "enemy_types": [4, 4, 4, 5, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_26():
    return {
        "walls": outter_walls + inner_right_wall + bottom_left_corner + inner_bottom_wall + outer_bottom_wall + bottom_right_corner + top_left_corner + inner_left_wall + outer_right_wall, 
        "enemy_types": [0, 1, 2, 3, 4, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_27():
    return {
        "walls": outter_walls + top_right_corner + outer_top_wall + inner_top_wall, 
        "enemy_types": [3, 4, 5, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_28():
    return {
        "walls": outter_walls + inner_left_wall + top_left_corner + outer_right_wall + inner_right_wall + bottom_left_corner, 
        "enemy_types": [5, 5, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_29():
    return {
        "walls": outter_walls + outer_left_wall + inner_right_wall + top_left_corner, 
        "enemy_types": [3, 4, 5, 5, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

def level_30():
    return {
        "walls": outter_walls,
        "enemy_types": [4, 4, 5, 5, 5],
        "powerups": 3,
        "goal": "kill_all"
    }

LEVELS = [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9, level_10, level_11, level_12, level_13, level_14, level_15, level_16, level_17, level_18, level_19, level_20, level_21, level_22, level_23, level_24, level_25, level_26, level_27, level_28, level_29, level_30]
