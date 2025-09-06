"""
Section 1: Integrated State Management (Main Loop Approach)

This example handles game states directly inside the main loop.
Press 1 to switch to the Menu state.
Press 2 to switch to the Game state.

This works for small projects but becomes harder to scale as the game grows.

As games get more complex, keeping all logic in one loop 
becomes harder to manage.

We initialize the font OUTSIDE of the while loop, otherwise every single frame would be re-importing
the font
We re-render text each frame since it depends on the game_state.
In bigger projects, static text can be cached instead of recreated every frame.
"""

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    
    # Current state can be "menu" or "game"
    game_state = "menu"
    font = pygame.font.Font(None, 74)
    helper_font = pygame.font.Font(None, 32)
    
    # Invalid to use here, as the values are NOT static. Since code is read topdown, this will only get processed once, then enter the while loop
    # This means it will never get looked at again.
    # main = f"Menu" if game_state == "menu" else "Game"
    # main_text = font.render(main, True, (255,255,255))
    # main_text_rect = main_text.get_rect(midleft=(50,50))
    
    # helper = f"Press {"[2]" if game_state == "menu" else "[1]"} to switch scenes"
    # helper_text = helper_font.render(helper, True, (255,255,255))
    # helper_rect = helper_text.get_rect(center=(1280 / 2, 720 - 20))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # When pressing "1" on the keyboard, swap the gamestate to menu
                    game_state = "menu"
                if event.key == pygame.K_2:
                    # When pressing "2" on the keyboard, swap the gamestate to game
                    game_state = "game"
        
        main = f"Menu" if game_state == "menu" else "Game" # Dynamic Text Rendering
        main_text = font.render(main, True, (255,255,255))
        main_text_rect = main_text.get_rect(midleft=(50,50))
        
        helper = f"Press {"[2]" if game_state == "menu" else "[1]"} to switch scenes"
        helper_text = helper_font.render(helper, True, (255,255,255))
        helper_rect = helper_text.get_rect(center=(1280 / 2, 720 - 20))
        
        if game_state == "menu":
            screen.fill((30, 30, 30)) # Menu background (Dark Grey)
        elif game_state == "game":
            screen.fill((200, 85, 30)) # Game background (Orange)
        
        screen.blit(main_text, main_text_rect)
        screen.blit(helper_text, helper_rect)
            
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()