import pygame
from settings import PLAYER_COLOR, PLAYER_RADIUS, PLAYER_SPEED, BOOST_MULTIPLIER, INVINCIBLE_COLOR

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_RADIUS * 2, PLAYER_RADIUS * 2)
        self.speed = PLAYER_SPEED
        self.boost_timer = 0
        self.invincible_timer = 0
        # image = pygame.image.load("../game/assets/björil.PNG")
        # self.image = pygame.transform.scale(image, (self.rect.width * 8, self.rect.height * 4))
        self.image = pygame.transform.scale(pygame.image.load("../game/assets/björil.PNG"), (self.rect.width * 8, self.rect.height * 4))


    def handle_input(self, keys, walls):
        actual_speed = self.speed * BOOST_MULTIPLIER if self.boost_timer > 0 else self.speed
        dx = dy = 0
        if keys[pygame.K_a]: dx -= actual_speed
        if keys[pygame.K_d]: dx += actual_speed
        if keys[pygame.K_w]: dy -= actual_speed
        if keys[pygame.K_s]: dy += actual_speed

        new_rect = self.rect.move(dx, dy)
        if not any(new_rect.colliderect(w) for w in walls):
            self.rect = new_rect

        if self.boost_timer > 0:
            self.boost_timer -= 1
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

    def draw(self, screen):
        # color = INVINCIBLE_COLOR if self.is_invincible() else PLAYER_COLOR
        # pygame.draw.polygon(screen, color, [
        #     (self.rect.centerx, self.rect.top),      # Top
        #     (self.rect.right, self.rect.centery),    # Right
        #     (self.rect.centerx, self.rect.bottom),   # Bottom
        #     (self.rect.left, self.rect.centery)      # Left
        # ])
        screen.blit(self.image, (self.rect.x - self.rect.width * 3.5, self.rect.y - self.rect.height * 1.5))

    def get_center(self):
        return self.rect.center
    
    def is_invincible(self):
        return self.invincible_timer > 0
