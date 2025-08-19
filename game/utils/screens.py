import pygame
import sys
from settings import WIDTH, HEIGHT, BACKGROUND_COLOR, FONT_COLOR

def draw_text_centered(screen, text, size, y_offset=0):
    font = pygame.font.SysFont(None, size)
    rendered = font.render(text, True, FONT_COLOR)
    rect = rendered.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(rendered, rect)

def wait_for_key(target_key, allow_escape=False):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == target_key:
                    return
                elif allow_escape and event.key == pygame.K_ESCAPE:
                    sys.exit()

def home_screen(screen):
    #screen.fill(BACKGROUND_COLOR)
    homescreen = pygame.transform.scale(pygame.image.load("../game/assets/mainscreen.JPG"), (WIDTH, HEIGHT))
    screen.blit(homescreen, (0, 0))
    #draw_text_centered(screen, "Press SPACE to Start (or [ESC] to exit)", 48)
    pygame.display.flip()
    wait_for_key(pygame.K_SPACE, allow_escape=True)

def game_over_screen(screen, level):
    screen.fill((255, 0, 0))
    highscore = int(open("HIGHSCORE.txt").read())          # read integer
    draw_text_centered(screen, "Game Over", 64, y_offset=-30)
    draw_text_centered(screen, f"You made it to level {level + 1}. High Score is {highscore}", 55, y_offset=30)
    draw_text_centered(screen, "Press SPACE to Restart", 36, y_offset=90)
    pygame.display.flip()
    wait_for_key(pygame.K_SPACE)

def win_screen(screen):
    screen.fill((100, 100, 100))
    draw_text_centered(screen, "Congratulations! You won!", 64, y_offset=-30)
    draw_text_centered(screen, "Press SPACE to Restart", 36, y_offset=30)
    pygame.display.flip()
    wait_for_key(pygame.K_SPACE)

def level_screen(screen, lvl_idx):
    screen.fill(BACKGROUND_COLOR)
    draw_text_centered(screen, f"Level {lvl_idx + 1}", 128, y_offset=-30)
    draw_text_centered(screen, f"DESTROY ALL ENEMIES", 64, y_offset=30)
    draw_text_centered(screen, "Press SPACE to start the level!", 32, y_offset=90)
    pygame.display.flip()
    wait_for_key(pygame.K_SPACE)