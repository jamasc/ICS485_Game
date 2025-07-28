import pygame
from settings import BOX_SIZE, BOX_SPEED_COLOR, BOX_INVINCIBLE_COLOR

class Box:
    def __init__(self, x, y, type="speed"):
        self.rect = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
        self.type = type

    def draw(self, screen):
        color = BOX_SPEED_COLOR if self.type == "speed" else BOX_INVINCIBLE_COLOR
        pygame.draw.rect(screen, color, self.rect)
