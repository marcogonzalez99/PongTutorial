"""
Game Class State Manager

Encapsulates game logic and state inside a class.
This structure makes it easier to expand as we add 
the ball, paddles, and scoring in later sections.

By moving state into a class, we can expand this later 
without cluttering the main loop (easier to add ball, paddles, scoring).

This class now owns all of its own rendering responsibilities, as such, 
fonts, images and all assets are imported here instead of in main
"""

import pygame

class Game:
    def __init__(self):
        self.game_state = "menu"
        self.font = pygame.font.Font(None, 74)
        self.helper_font = pygame.font.Font(None, 32)

    def run(self, events, screen):
        self.update(events)
        self.draw(screen)
        
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # When pressing "1" on the keyboard, swap the gamestate to menu
                    self.game_state = "menu"
                if event.key == pygame.K_2:
                    # When pressing "2" on the keyboard, swap the gamestate to game
                    self.game_state = "game"
    
    def draw(self, screen):
        
        if self.game_state == "menu":
            screen.fill((30, 30, 30)) # Menu background (Dark Grey)
        elif self.game_state == "game":
            screen.fill((200, 85, 30)) # Game background (Orange)
        
        main = f"Menu" if self.game_state == "menu" else "Game"
        main_text = self.font.render(main, True, (255,255,255))
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

# Incorrect Method, trying to cache on init, if the values are not static
# class Game:
#     def __init__(self):
#         self.game_state = "menu"
#         self.font = pygame.font.Font(None, 74)
#         self.helper_font = pygame.font.Font(None, 32)

#         main = f"Menu" if self.game_state == "menu" else "Game"
#         self.main_text = self.font.render(main, True, (255,255,255))
#         self.main_text_rect = self.main_text.get_rect(midleft=(50,50))
        
#         helper = f"Press {"[2]" if self.game_state == "menu" else "[1]"} to switch scenes"
#         self.helper_text = self.helper_font.render(helper, True, (255,255,255))
#         self.helper_rect = self.helper_text.get_rect(center=(1280 / 2, 720 - 20))
        
#     def run(self, events, screen):
#         self.update(events)
#         self.draw(screen)
        
#     def update(self, events):
#         for event in events:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_1:
#                     # When pressing "1" on the keyboard, swap the gamestate to menu
#                     self.game_state = "menu"
#                 if event.key == pygame.K_2:
#                     # When pressing "2" on the keyboard, swap the gamestate to game
#                     self.game_state = "game"
    
#     def draw(self, screen):
        
#         if self.game_state == "menu":
#             screen.fill((30, 30, 30)) # Menu background (Dark Grey)
#         elif self.game_state == "game":
#             screen.fill((200, 85, 30)) # Game background (Orange)
        
#         screen.blit(self.main_text, self.main_text_rect)
#         screen.blit(self.helper_text, self.helper_rect)

"""
Preferred Cleaned Up Alternative:
While the solution above is not incorrect, every developer has their own preference to how to organize their
functions/responsibilities. The class below would be my preferred method to handle this Section, using a Game class
"""
# class Game:
#     def __init__(self):
#         self.game_state = "menu"
#         self.font = pygame.font.Font(None, 74)
#         self.helper_font = pygame.font.Font(None, 32)

#     def run(self, events, screen):
#         self.update(events)
#         self.draw(screen)
        
#     def update(self, events):
#         for event in events:
#             if event.type == pygame.KEYDOWN:
#                 self.handle_keydown(event)
                
#     def handle_keydown(self, event):
#         if event.key == pygame.K_1:
#             self.game_state = "menu"
#         if event.key == pygame.K_2:
#             self.game_state = "game"
    
#     def draw(self, screen):
#         if self.game_state == "menu":
#             screen.fill((30, 30, 30)) # Menu background (Dark Grey)
#         elif self.game_state == "game":
#             screen.fill((200, 85, 30)) # Game background (Orange)
        
#         self.draw_main_text(screen)
#         self.draw_helper_text(screen)
    
#     def draw_main_text(self, screen):
#         main = f"Menu" if self.game_state == "menu" else "Game"
#         main_text = self.font.render(main, True, (255,255,255))
#         main_text_rect = main_text.get_rect(midleft=(50,50))
#         screen.blit(main_text, main_text_rect)
    
#     def draw_helper_text(self, screen):
#         helper = f"Press {"[2]" if self.game_state == "menu" else "[1]"} to switch scenes"
#         helper_text = self.helper_font.render(helper, True, (255,255,255))
#         helper_rect = helper_text.get_rect(center=(1280 / 2, 720 - 20))
#         screen.blit(helper_text, helper_rect)