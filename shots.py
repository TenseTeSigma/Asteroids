import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, SHOT_RADIUS)

  def draw(self, screen):
    pygame.draw.circle(screen, "green", self.position, SHOT_RADIUS, 2)

  def update(self, dt):
    self.position += self.velocity * dt
  
  def remove(self):
    self.kill()
  
class Missle(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect, MISSLE_BORDER, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def remove(self):
        self.kill()