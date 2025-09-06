"""
Opponent Paddle Class

Handles the CPU-controlled paddle movement and boundary constraints.

- Follows the vertical position of the ball.
- Simple AI: directly mirrors the ball’s Y position every frame.
- Prevents the paddle from leaving the top or bottom of the screen.
Difficulty scaling (slower reaction or capped speed) will be introduced in Section 5.
"""

class Opponent():
    def __init__(self, surface, starting_x_position, starting_y_position, speed):
        self.image = surface
        self.rect = self.image.get_rect(center=(
            starting_x_position, 
            starting_y_position
        ))

        self.speed = speed
        
    def update(self, ball):
        # Movement
        if self.rect.centery < ball.rect.centery:
            self.rect.y += self.speed
        elif self.rect.centery > ball.rect.centery:
            self.rect.y -= self.speed
                
        # Boundary constraints
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 720:
            self.rect.bottom = 720
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

