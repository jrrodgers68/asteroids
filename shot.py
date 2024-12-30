from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        # On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
        self.position += (self.velocity * dt)