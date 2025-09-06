"""
Initializes with a ball object, checking game state
to determine whether or not to draw/update the ball

This Game class owns the Ball class, and manages and has access to all of its functions and fields

In this example, all texts are dynamic, and therefore must be rendered every frame 
to detect changes in the state
"""
import pygame
from ball import Ball

class Game:
    def __init__(self):
        self.game_state = "menu"
        self.font = pygame.font.Font(None, 74)
        self.helper_font = pygame.font.Font(None, 32)

        ball_surface = pygame.image.load("../assets/blue_ball.png").convert_alpha()
        self.ball = Ball(
            surface = ball_surface,
            x_position = 1280 // 2,
            y_position = 720 // 2,
            x_speed = 8,
            y_speed = 8
        )

    def run(self, events, screen):
        self.update(events)
        self.draw(screen)
        
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.game_state = "menu"
                    self.ball.active = False  # deactivate ball
                if event.key == pygame.K_2:
                    self.game_state = "game"
                    
                if self.game_state == "game" and event.key == pygame.K_SPACE:
                    # Toggle active state of the ball
                    self.ball.active = not self.ball.active
                
                if self.game_state == "game" and event.key == pygame.K_r:
                    # Reset ball to center
                    self.ball.reset()
        
        # Ball only updates while in game state
        if self.game_state == "game":
            self.ball.update()
    
    def draw(self, screen):        
        if self.game_state == "menu":
            screen.fill((30, 30, 30)) # Menu background (Dark Grey)
        elif self.game_state == "game":
            screen.fill((200, 85, 30)) # Game background (Orange)
            self.ball.draw(screen)
        
        main_text = self.font.render(f"Menu" if self.game_state == "menu" else "Game", True, (255,255,255))
        main_text_rect = main_text.get_rect(midleft=(
            50,
            50
        ))
        screen.blit(main_text, main_text_rect)
        
        helper = f"Press {"[2]" if self.game_state == "menu" else "[1]"} to switch scenes"
        helper_text = self.helper_font.render(helper, True, (255,255,255))
        helper_rect = helper_text.get_rect(center=(
            1280 / 2, 
            720 - 20
        ))
        screen.blit(helper_text, helper_rect)
        
        start_text = self.helper_font.render(f"Press [Space] to {"stop" if self.ball.active else "start"} the ball", True, (255,255,255))
        start_text_rect = start_text.get_rect(center=(
            1280 / 2,
            720 - 60
        ))
        if self.game_state == "game":
            screen.blit(start_text, start_text_rect)
        
        reset_text = self.helper_font.render(f"Press [R] to reset the ball", True, (255,255,255))
        reset_text_rect = reset_text.get_rect(center=(
            1280 / 2,
            20
        ))
        if self.game_state == "game":
            screen.blit(reset_text, reset_text_rect)