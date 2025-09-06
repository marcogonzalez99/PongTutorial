"""
Ball Class

Handles ball movement, bouncing physics, and drawing.

- Collides with top/bottom walls and bounces vertically.
- Collides with player and opponent paddles and bounces horizontally.
- Resets to the center if it goes past the left or right edge.
- Uses hardcoded 1280x720 bounds for simplicity.
  (In larger projects, these would be dynamic
  PolarisKit automates this.)
- Assumes all assets are correctly located in the /assets folder
"""


import pygame, random

class Ball:
    def __init__(self, surface, x_position, y_position, x_speed, y_speed):
        self.image = surface
        self.rect = self.image.get_rect(center=(x_position, y_position))

        self.x_speed = x_speed * random.choice((-1, 1))
        self.y_speed = y_speed * random.choice((-1, 1))

        self.active = False  # Ball starts inactive until the game begins

        self.paddle_hit = pygame.mixer.Sound("assets/paddle_hit.wav")
        self.wall_hit = pygame.mixer.Sound("assets/wall_hit.wav")

    def update(self, player, opponent):
        if self.active:
            self.move()
            self.check_collisions(player, opponent)
            
    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
    def check_collisions(self, player, opponent):
        # Paddle collisions (simple version only flips horizontal direction)
        if self.rect.top <= 0:
            self.rect.top = 0
            self.y_speed *= -1
            pygame.mixer.Sound.play(self.wall_hit)
        
        if self.rect.bottom >= 720:
            self.rect.bottom = 720
            self.y_speed *= -1
            pygame.mixer.Sound.play(self.wall_hit)
        
        # Paddle collisions
        if self.rect.colliderect(player.rect):
            self.x_speed *= -1
            pygame.mixer.Sound.play(self.paddle_hit)
        if self.rect.colliderect(opponent.rect):
            self.x_speed *= -1
            pygame.mixer.Sound.play(self.paddle_hit)
            
    def reset(self):
        # re-center to middle of screen
        self.rect.center = (
            1280 // 2, 
            720 // 2
        ) 
        self.active = False
        
    def start(self):
        self.active = True
        self.x_speed = abs(self.x_speed) * random.choice((-1, 1))
        self.y_speed = abs(self.y_speed) * random.choice((-1, 1))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
