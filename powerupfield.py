import random
import pygame
from constants import *
from powerup import Powerup

class PowerupField([pygame.sprite.Sprite]):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-POWERUP_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + POWERUP_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -POWERUP_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + POWERUP_RADIUS
            ),
        ],
    ]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
    

    def spawn(radius, position, velocity):
        powerup = Powerup(position.x, position.y, radius)
        powerup.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > POWERUP_SPAWN_RATE:
            self.spawn_timer = 0

            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            self.spawn(POWERUP_RADIUS * position, velocity)

