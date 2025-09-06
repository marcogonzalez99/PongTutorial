"""
Player Paddle Class

Handles player-controlled paddle movement and boundary constraints.
Controlled via W/S or Up/Down keys.

- Uses pygame.key.get_pressed() for smooth, continuous movement.
- Prevents the paddle from leaving the top or bottom of the screen.
"""


import pygame

class Player():
    def __init__(self, surface, starting_x_position, starting_y_position, speed):
        self.image = surface
        self.rect = self.image.get_rect(center=(
            starting_x_position, 
            starting_y_position
        ))

        self.speed = speed
        
    def update(self, events):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Boundary constraints
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 720:
            self.rect.bottom = 720
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

