from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_COLOR
import pygame
import random
import math


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Make random asteroid sprites
        full_circle = random.uniform(18, 36)
        dist = random.uniform(self.radius / 2, self.radius)
        self.vertices = []
        while full_circle < 360:
            self.vertices.append([dist, full_circle])
            dist = random.uniform(self.radius / 2, self.radius)
            full_circle += random.uniform(18, 36)

    def draw(self, screen):
        #pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, 2)
        # Draw asteroid
        for v in range(len(self.vertices)):
            if v == len(self.vertices) - 1:
                next_v = self.vertices[0]
            else:
                next_v = self.vertices[v + 1]
            this_v = self.vertices[v]
            pygame.draw.line(screen, ASTEROID_COLOR, (self.position.x + this_v[0] * math.cos(this_v[1] * math.pi / 180),
                                                  self.position.y + this_v[0] * math.sin(this_v[1] * math.pi / 180)),
                             (self.position.x + next_v[0] * math.cos(next_v[1] * math.pi / 180),
                              self.position.y + next_v[0] * math.sin(next_v[1] * math.pi / 180)))

    def update(self, dt):
        # On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # create 2 new asteriods that are smaller and faster, moving in random direction from original
        random_angle = random.uniform(20, 50)
        direction_1 = self.velocity.rotate(random_angle)
        direction_2 = self.velocity.rotate(-1 * random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = direction_1 * 1.2
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = direction_2 * 1.2