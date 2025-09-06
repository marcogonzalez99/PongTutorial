"""
Game Class – Section 5: Polish & Finishing Touches

Adds final polish to the Pong clone:
- Audio (paddle hits, wall bounces, scoring, background music).
- Helper UI text and modifier controls for paddle/ball speeds.
- Live readouts for CPU, Player, and Ball speeds.
- Win condition (first to 3) with results screen and restart.
"""

import pygame
from ball import Ball
from player import Player
from opponent import Opponent

class Game:
    def __init__(self):        
        # == Audio ==
        self.lose_point = pygame.mixer.Sound("assets/lose_point.wav")
        self.win_point = pygame.mixer.Sound("assets/win_point.wav")
        self.music = pygame.mixer.Sound("assets/music.wav")
        
        # == Fonts ==
        self.font = pygame.font.Font(None, 74)   # Main score font
        self.font_small = pygame.font.Font(None, 28) # UI/helper font

        # == Game State ==
        self.game_state = "menu"

        # == Assets ==
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
        
        opponent_paddle_surface = pygame.transform.flip(
            pygame.image.load("../assets/blue_paddle.png").convert_alpha(), 
            True, False
        )
        self.opponent = Opponent(
            surface = opponent_paddle_surface,
            starting_x_position = 1280 - 10,
            starting_y_position = 720 // 2,
            speed = 10
        )
        
        self.background = pygame.image.load("assets/background.png").convert_alpha()
        self.logo = pygame.image.load("assets/logo.png").convert_alpha()

        # == Scores ==
        self.player_score = 0
        self.opponent_score = 0
        
    def run(self, events, screen):
        self.update(events)
        self.draw(screen)
        
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event)
                
        if self.game_state == "game":
            self.ball.update(self.player, self.opponent)
            self.player.update(events)
            self.opponent.update(self.ball)

            # == Scoring ==
            if self.ball.rect.left < 0:
                self.opponent_score += 1
                pygame.mixer.Sound.play(self.lose_point)
                self.ball.reset()
            elif self.ball.rect.right > 1280:
                self.player_score += 1
                pygame.mixer.Sound.play(self.win_point)
                self.ball.reset()
                
            # == Win Condition ==
            if self.player_score == 3 or self.opponent_score == 3:
                self.game_state = "game_results"
    
    def handle_keydown(self, event):
        # == Navigation ==
        if event.key == pygame.K_1 and self.game_state != "menu":
            self.return_to_menu()
        
        if event.key == pygame.K_2 and self.game_state != "game":
            self.start_game()
        
        if not self.ball.active and event.key == pygame.K_SPACE:
            self.ball.start()
        
        # == Opponent Speed ==
        if event.key == pygame.K_3:
            self.opponent.speed = max(4, self.opponent.speed - 1)
        if event.key == pygame.K_4:
            self.opponent.speed = min(16, self.opponent.speed + 1)

        # == Player Speed ==
        if event.key == pygame.K_5:
            self.player.speed = max(4, self.player.speed - 1)
        if event.key == pygame.K_6:
            self.player.speed = min(16, self.player.speed + 1)

        # == Ball Speed (handle signs correctly) ==
        if event.key == pygame.K_7:
            self.ball.x_speed = max(4, abs(self.ball.x_speed) - 1) * (1 if self.ball.x_speed >= 0 else -1)
            self.ball.y_speed = max(4, abs(self.ball.y_speed) - 1) * (1 if self.ball.y_speed >= 0 else -1)
        if event.key == pygame.K_8:
            self.ball.x_speed = min(16, abs(self.ball.x_speed) + 1) * (1 if self.ball.x_speed >= 0 else -1)
            self.ball.y_speed = min(16, abs(self.ball.y_speed) + 1) * (1 if self.ball.y_speed >= 0 else -1)
    
    def return_to_menu(self):
        self.game_state = "menu"
        self.music.stop()
        self.ball.active = False
        self.player_score = 0
        self.opponent_score = 0
    
    def start_game(self):
        self.game_state = "game"
        self.music.play(loops=-1)

    # ================= Draw Methods ================= #
    def draw(self, screen):
        if self.game_state == "menu":
            screen.blit(self.background, (0,0))
            self.draw_logo(screen)
            self.draw_main_start_text(screen)
            
        elif self.game_state == "game":
            screen.fill((32,42,68)) 
            self.ball.draw(screen) 
            self.player.draw(screen)  
            self.opponent.draw(screen)  
            pygame.draw.rect(screen, (90,90,90), pygame.Rect((1280 // 2) - 2, 0, 4, 720))
            self.draw_player_score(screen)
            self.draw_opponent_score(screen)
            self.draw_score_helper(screen)
            self.draw_game_menu_hint(screen)
            self.draw_modifier_info(screen)
            self.draw_modifier_helper(screen)
                
        elif self.game_state == "game_results":
            screen.fill((32,42,68)) 
            self.draw_results_helper(screen)
            self.draw_results_hint(screen)
    
    # == Menu Helpers == #        
    def draw_logo(self, screen):
        logo_rect = self.logo.get_rect(center=(1280/2,720/3))
        screen.blit(self.logo, logo_rect)
    
    def draw_main_start_text(self, screen):
        press_start_text = self.font.render("Press [2] to Start", True, (255, 255, 255))
        press_start_rect = press_start_text.get_rect(center=(1280 / 2,720 / 2))
        screen.blit(press_start_text, press_start_rect)
    
    # == Game Helpers == #
    def draw_score_helper(self, screen):
        score_text = "First to 3 Wins"
        score_surface = self.font_small.render(score_text, True, (200, 200, 200))
        screen.blit(score_surface, (1280/2 + 30, 20))
    
    def draw_game_menu_hint(self, screen):
        menu_hint = self.font_small.render("[1] Menu", True, (200, 200, 200))
        screen.blit(menu_hint, (1280 - menu_hint.get_width() - 12, 12))

    def draw_modifier_info(self, screen):
        vals_text = f"CPU: {self.opponent.speed}   Player: {self.player.speed}   Ball: X:{abs(self.ball.x_speed)}/Y:{abs(self.ball.y_speed)}"
        vals_surface = self.font_small.render(vals_text, True, (185, 185, 185))
        screen.blit(vals_surface, (10, 664))
    
    def draw_modifier_helper(self, screen):
        helper_text = "[3/4] Opponent Speed +/- | [5/6] Player Speed +/- | [7/8] Ball Speed +/-"
        helper_surface = self.font_small.render(helper_text, True, (200, 200, 200))
        screen.blit(helper_surface, (10, 690))
                
    def draw_player_score(self, screen):
        player_score_text = self.font.render(str(self.player_score), True, (255, 255, 255))
        player_score_rect = player_score_text.get_rect(center=(1280//4, 50))
        screen.blit(player_score_text, player_score_rect)

    def draw_opponent_score(self, screen):
        opponent_score_text = self.font.render(str(self.opponent_score), True, (255, 255, 255))
        opponent_score_rect = opponent_score_text.get_rect(center=(1280*3//4, 50))
        screen.blit(opponent_score_text, opponent_score_rect)

    # == Results Helpers == #
    def draw_results_helper(self, screen):
        winner = "Player" if self.player_score == 3 else "CPU"
        helper_surface = self.font_small.render(f"{winner} Won", True, (200, 200, 200))
        helper_rect = helper_surface.get_rect(center=(1280/2, 720/2))
        screen.blit(helper_surface, helper_rect)
        
    def draw_results_hint(self, screen):
        menu_hint = self.font_small.render("[1] Menu", True, (200, 200, 200))
        screen.blit(menu_hint, (1280 - menu_hint.get_width() - 12, 12))