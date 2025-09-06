"""
Section 2: Ball Setup & Physics

This section introduces the Ball class with movement and 
simple physics.

Press 1 to switch to the Menu state.
Press 2 to switch to the Game state.
Press Space to toggle the ball state between Active/Inactive
Press R to reset the ball to the middle
"""

import pygame
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    game = Game()
    
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        game.run(events, screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()