import pygame
from settings import BOOST_MULTIPLIER, INVINCIBLE_COLOR

class Bouncer:
    def __init__(self, x, y, direction, speed, radius, color, is_enemy=False):
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)
        self.pos = pygame.Vector2(x, y)
        self.radius = radius
        self.direction = direction.normalize()
        self.base_speed = speed
        self.boost_timer = 0
        self.invincible_timer = 0
        self.color = color
        self.is_enemy = is_enemy

    def update(self, walls):
        current_speed = self.base_speed * BOOST_MULTIPLIER if self.boost_timer > 0 else self.base_speed
        next_pos = self.pos + self.direction * current_speed
        next_rect = pygame.Rect(int(next_pos.x), int(next_pos.y), self.radius * 2, self.radius * 2)

        for wall in walls:
            if next_rect.colliderect(wall):
                reflect_x = self.pos + pygame.Vector2(-self.direction.x, self.direction.y) * current_speed
                reflect_y = self.pos + pygame.Vector2(self.direction.x, -self.direction.y) * current_speed
                rect_x = pygame.Rect(int(reflect_x.x), int(reflect_x.y), self.radius * 2, self.radius * 2)
                rect_y = pygame.Rect(int(reflect_y.x), int(reflect_y.y), self.radius * 2, self.radius * 2)

                if not any(rect_x.colliderect(w) for w in walls):
                    self.direction.x *= -1
                elif not any(rect_y.colliderect(w) for w in walls):
                    self.direction.y *= -1
                else:
                    self.direction *= -1
                return

        self.pos = next_pos
        self.rect.topleft = int(self.pos.x), int(self.pos.y)

        if self.boost_timer > 0:
            self.boost_timer -= 1
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

    def is_invincible(self):
        return self.invincible_timer > 0

    def draw(self, screen):
        color = INVINCIBLE_COLOR if self.is_invincible() else self.color
        pygame.draw.ellipse(screen, color, self.rect)
