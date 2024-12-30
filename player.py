from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_COLOR, PLAYER_LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_delay = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), PLAYER_LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.shoot_delay > 0:
            self.shoot_delay -= dt
            if self.shoot_delay < 0:
                self.shoot_delay = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        elif keys[pygame.K_LEFT]:
            self.rotate(dt * -1)
        elif keys[pygame.K_RIGHT]:
            self.rotate(dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        elif keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(dt * -1)
        elif keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.shoot_delay == 0:
            self.shoot_delay = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y)
            velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            shot.velocity = velocity
