import pygame
import sys
import random

from settings import *
from entities.player import Player
from entities.bouncer import Bouncer
from entities.box import Box
from utils.screens import home_screen, game_over_screen, win_screen, level_screen
from levels.level_data import LEVELS


def spawn_enemy(walls, enemy_type):
    for _ in range(100):
        x = random.randint(40, WIDTH - 40)
        y = random.randint(40, HEIGHT - 40)
        dir = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        enemy = Bouncer(x, y, dir, ENEMY_SPEED[enemy_type], ENEMY_RADIUS[enemy_type], ENEMY_COLOR[enemy_type], is_enemy=True, is_shooter=ENEMY_IS_SHOOTER[enemy_type], inaccuracy=ENEMY_INACCURACY[enemy_type])
        if not any(enemy.rect.colliderect(w) for w in walls):
            return enemy
    return None

def spawn_boxes(walls, num_boxes):
    boxes = []
    for _ in range(num_boxes):
        for _ in range(100):
            x = random.randint(20, WIDTH - BOX_SIZE - 20)
            y = random.randint(20, HEIGHT - BOX_SIZE - 20)
            box_type = random.choice(["speed", "invincible"])
            box = Box(x, y, type=box_type)
            if not any(box.rect.colliderect(w) for w in walls):
                boxes.append(box)
                break
    return boxes

def draw_walls(screen, walls, WALL_COLOR):
    for wall in walls:
        pygame.draw.rect(screen, WALL_COLOR, wall)

def game_loop(screen, clock, level_data):
    game_won = False
    player = Player(WIDTH // 2, HEIGHT // 2)
    background = pygame.transform.scale(pygame.image.load("../game/assets/background.JPG"), (WIDTH, HEIGHT))
    walls = level_data["walls"]
    powerups = spawn_boxes(walls, level_data["powerups"])
    projectiles = []
    for e_type in level_data["enemy_types"]:
        enemy = spawn_enemy(walls, e_type)
        if enemy:
            projectiles.append(enemy)


    while True:
        #screen.fill(BACKGROUND_COLOR)
        screen.blit(background, (0,0))
        keys = pygame.key.get_pressed()

        ### Player
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     # player shooting
                current_bullets = [p for p in projectiles if p.is_player]
                if len(current_bullets) < MAX_BULLETS:
                    px, py = player.get_center()
                    mx, my = pygame.mouse.get_pos()
                    direction = pygame.Vector2(mx - px, my - py)
                    offset_distance = PLAYER_RADIUS + BULLET_RADIUS + 10
                    spawn_pos = pygame.Vector2(px, py) + direction.normalize() * offset_distance
                    bullet = Bouncer(spawn_pos.x, spawn_pos.y, direction, BULLET_SPEED, BULLET_RADIUS, BULLET_COLOR, is_enemy=False, is_player=True)
                    projectiles.append(bullet)

        player.handle_input(keys, walls)

        ### Enemies and Bullets
        # Enemy Shooting 
        enemy_bullets = [p for p in projectiles if not p.is_enemy and not p.is_player]
        if len(enemy_bullets) < ENEMY_BULLET_LIMIT:
            for enemy in [p for p in projectiles if p.is_enemy and p.is_shooter]:
                if random.random() < ENEMY_SHOOT_CHANCE:
                    ex, ey = enemy.get_center()
                    px, py = player.get_center()
                    x_offset = (int) (random.random() * enemy.inaccuracy * 2 - enemy.inaccuracy)
                    y_offset = (int) (random.random() * enemy.inaccuracy * 2 - enemy.inaccuracy)
                    px += x_offset
                    py += y_offset
                    direction = pygame.Vector2(px - ex, py - ey)
                    if direction.length() > 0:
                        offset_distance = PLAYER_RADIUS + BULLET_RADIUS + 10
                        spawn_pos = pygame.Vector2(ex, ey) + direction.normalize() * offset_distance
                        bullet = Bouncer(
                            spawn_pos.x, spawn_pos.y,
                            direction, BULLET_SPEED, BULLET_RADIUS,
                            BULLET_COLOR, is_enemy=False, is_player=False
                        )
                        projectiles.append(bullet)

        
        for obj in projectiles:
            obj.update(walls)

        ### Handle collisions
        to_remove = set()
        # Enemies and Bullets
        for a in projectiles:
            for b in projectiles:
                if a == b or (a.is_enemy and b.is_enemy):
                    continue
                if a.rect.colliderect(b.rect) and not b.is_invincible():
                    #to_remove.add(a)     #why add this when the loop goes thru everything anyways
                    to_remove.add(b)

        projectiles = [obj for obj in projectiles if obj not in to_remove]
        
        # Powerups
        for box in powerups[:]:
            if player.rect.colliderect(box.rect):
                if box.type == "speed":
                    player.boost_timer = BOOST_DURATION
                elif box.type == "invincible":
                    player.invincible_timer = INVINCIBILITY_DURATION
                powerups.remove(box)
                continue

            for obj in projectiles:
                if obj.rect.colliderect(box.rect):
                    if box.type == "speed":
                        obj.boost_timer = BOOST_DURATION
                    elif box.type == "invincible":
                        obj.invincible_timer = INVINCIBILITY_DURATION
                    powerups.remove(box)
                    break

        ### Losing Logic
        for obj in projectiles:
            if obj.rect.colliderect(player.rect) and not player.is_invincible():
                return "lose"
        
        ### Winning logic
        remaining_enemies = [p for p in projectiles if p.is_enemy]
        px, py = player.get_center()
        if level_data["goal"] == "kill_all" and not remaining_enemies:
            return "win"
        elif level_data["goal"] == "escape" and (px < 0 or px > WIDTH or py < 0 or py > HEIGHT):
            return "win"

        ### Display
        draw_walls(screen, walls, WALL_COLOR)
        player.draw(screen)
        for obj in projectiles:
            obj.draw(screen)
        for box in powerups:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bjoeril Exit")
    clock = pygame.time.Clock()
    TRACKS = {
        "title": pygame.mixer.Sound("../game/assets/titlescreensong.mp3"),
        "gameplay": pygame.mixer.Sound("../game/assets/gameplaysong.mp3"),
        "lose": pygame.mixer.Sound("../game/assets/ohbother.mp3"),
    }

    while True:
        TRACKS['title'].play(loops=-1, fade_ms=500)
        home_screen(screen)
        for level_index, level_fn in enumerate(LEVELS):
            level_screen(screen, level_index)
            TRACKS['title'].stop()
            TRACKS['gameplay'].stop()
            TRACKS['gameplay'].play(loops=-1)
            level_data = level_fn()
            result = game_loop(screen, clock, level_data)
            if result == "lose":
                highscore = int(open("HIGHSCORE.txt").read())          # read integer
                if level_index >= highscore:
                    open("HIGHSCORE.txt", "w").write(str(level_index+1))      # store integer
                TRACKS['gameplay'].stop()
                TRACKS['lose'].play()
                game_over_screen(screen, level_index)
                TRACKS['lose'].stop()
                break
            elif result == "win":
                continue
        else:
            win_screen(screen)


if __name__ == "__main__":
    main()
