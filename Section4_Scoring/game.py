"""
Game Class

Controls the game state, ball, and paddles.

Builds on Section 3 by adding scoring and displaying points for each side when the ball goes out of bounds.

- Menu state (press 1): shows a blank screen with no ball/paddle updates.
- Game state (press 2): activates gameplay with the ball and paddles.
- Ball can also be started with the SPACE key if inactive.
- Updates and draws the ball, player paddle, and opponent paddle.
- Also displays the running score for both player and opponent.
"""

import pygame
from ball import Ball
from player import Player
from opponent import Opponent

class Game:
    def __init__(self):
        self.game_state = "menu"
        self.font = pygame.font.Font(None, 74)  # None = default font, 74 = size
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
        self.player = Player(
            surface = player_paddle_surface,
            starting_x_position = 10,
            starting_y_position = 720 // 2,
            speed = 10
        )
        
        opponent_paddle_surface = pygame.transform.flip(pygame.image.load("../assets/blue_paddle.png").convert_alpha(), True, False)
        self.opponent = Opponent(
            surface = opponent_paddle_surface,
            starting_x_position = 1280 - 10,
            starting_y_position = 720 // 2,
            speed = 10
        )
        
        self.player_score = 0
        self.opponent_score = 0
        
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
            self.player.update(events)
            self.opponent.update(self.ball)

            # Update scores if the ball goes past the left or right edge.
            # Left edge = opponent scores
            # Right edge = player scores.
            if self.ball.rect.left < 0:
                self.opponent_score += 1
                self.ball.reset()
            elif self.ball.rect.right > 1280:
                self.player_score += 1
                self.ball.reset()

    
    def draw(self, screen):
        if self.game_state == "menu":
            screen.fill((30, 30, 30)) # Menu background (Dark Grey)
        elif self.game_state == "game":
            screen.fill((200, 85, 30)) # Game background (Orange)
            self.ball.draw(screen) # Draw the ball
            self.player.draw(screen)  # Draw player paddle
            self.opponent.draw(screen)  # Draw opponent paddle
            self.draw_player_score(screen)
            self.draw_opponent_score(screen)
            
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

                
    def draw_player_score(self, screen):
        player_score_text = self.font.render(str(self.player_score), True, (255, 255, 255))
        player_score_rect = player_score_text.get_rect(center=(1280//4, 50))
        screen.blit(player_score_text, player_score_rect)

    def draw_opponent_score(self, screen):
        opponent_score_text = self.font.render(str(self.opponent_score), True, (255, 255, 255))
        opponent_score_rect = opponent_score_text.get_rect(center=(1280*3//4, 50))
        screen.blit(opponent_score_text, opponent_score_rect)
