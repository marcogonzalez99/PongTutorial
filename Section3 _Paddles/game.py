"""
Game Class

Controls the game state, ball, and paddles.

- Menu state (press 1): shows a blank screen with no ball/paddle updates.
- Game state (press 2): activates gameplay with the ball and paddles.
- Ball can also be started with the SPACE key if inactive.
- Updates and draws the ball, player paddle, and opponent paddle.
"""

import pygame
from ball import Ball
from player import Player
from opponent import Opponent

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
        
        player_paddle_surface = pygame.image.load("../assets/blue_paddle.png").convert_alpha()
        opponent_paddle_surface = pygame.transform.flip(pygame.image.load("../assets/blue_paddle.png").convert_alpha(), True, False)
        self.player = Player(
            surface = player_paddle_surface,
            starting_x_position = 10,
            starting_y_position = 720 // 2,
            speed = 10
        )
        self.opponent = Opponent(
            surface = opponent_paddle_surface,
            starting_x_position = 1280 - 10,
            starting_y_position = 720 // 2,
            speed = 10
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
            self.ball.update(self.player, self.opponent)
            self.player.update(events) # Handle human input
            self.opponent.update(events, self.ball) # Automate CPU movement
    
    def draw(self, screen):
        if self.game_state == "menu":
            screen.fill((30, 30, 30)) # Menu background (Dark Grey)
        elif self.game_state == "game":
            screen.fill((200, 85, 30)) # Game background (Orange)
            self.ball.draw(screen) # Draw the ball
            self.player.draw(screen)  # Draw player paddle
            self.opponent.draw(screen)  # Draw opponent paddle
            
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
