"""
Ball Class

Handles ball movement, bouncing physics, and drawing.

This example uses hardcoded screen bounds (1280x720)
for simplicity. In larger projects, these would be dynamic.
PolarisKit automates this. But you can as well by getting % based screen sizes for example
"""

import random

class Ball:
    def __init__(self, surface, x_position, y_position, x_speed, y_speed):
        self.image = surface
        self.rect = self.image.get_rect(center=(x_position, y_position))

        self.x_speed = x_speed * random.choice((-1, 1))
        self.y_speed = y_speed * random.choice((-1, 1))

        self.active = False  # Ball starts inactive until the game begins

    def update(self):
        if self.active:
            self.move()
            self.check_collisions()
            
    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
    def reset(self):
        # re-center to middle of screen
        self.rect.center = (
            1280 // 2, 
            720 // 2
        ) 
        self.active = False

    def check_collisions(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.y_speed *= -1
        
        if self.rect.bottom >= 720:
            self.rect.bottom = 720
            self.y_speed *= -1
        
        if self.rect.left <= 0:
            self.rect.left = 0
            self.x_speed *= -1
        
        if self.rect.right >= 1280:
            self.rect.right = 1280
            self.x_speed *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)