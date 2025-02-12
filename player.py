import pygame
from constants import *
from circleshape import CircleShape
from shots import Shot, Missle
from asteroid import Asteroid

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
      keys = pygame.key.get_pressed()
      self.timer = max(0, self.timer - dt)
      if keys[pygame.K_a]:
        self.rotate(-dt)
      if keys[pygame.K_d]:
        self.rotate(dt)
      if keys[pygame.K_w]:
        self.move(dt)
      if keys[pygame.K_s]:
        self.move(-dt)
      if keys[pygame.K_SPACE]:
        self.shoot()
      if keys[pygame.K_c]:
        self.mshot()
      
    def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
          shot = Shot(self.position.x, self.position.y)
          shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
          self.timer = PLAYER_SHOT_COOLDOWN

    def reset_position(self, asteroid):
      if asteroid.position == pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2):
        asteroid.kill()
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.rotation = 0
        print("Asteroid was at 0,0... asteroid removed")
      else:
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.rotation = 0
        print("No asteroid found at 0,0")

    def mshot(self):
      if self.timer <= 0:
        missle = Missle(self.position.x, self.position.y)
        missle.velocity = pygame.Vector2(0,1).rotate(self.position) * MISSLE_SPEED
        self.timer = MISSLE_COOLDOWN

